# Echo server program
import socket
from datetime import datetime
import boto3

client = boto3.client('firehose')
notify = boto3.client('sns')
#f = open('dump.csv','bw')

HOST = '192.168.100.4'                 
PORT = 3000              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(256)
            #f.write(data)
            response = client.put_record(
                DeliveryStreamName='avaya-smdr-logs',
                Record={
                    "Data" : data
                }
            )
            
            if not data: break
print ('Connection lost at \n', datetime.now())
notify.publish(
    TargetArn='arn:aws:sns:us-east-1:XXXXXXXXXXXX:topic_name',
    Message='AVAYA/SMDR Log system - Connection lost at \n' + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)
