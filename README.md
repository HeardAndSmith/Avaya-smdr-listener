# Avaya-smdr-listener
Very basic python script that listens for AVAYA IPOffice SMDR call logs and store them to an S3 bucket using AWS Kinesis-Firehose service. 
The script opens a TCP socket and listens for the stream of data from Avaya. As data is being recevied from Avaya, the script uploads each call record to AWS via the Firehose stream.
Firehose then puts the records in S3. 
If/When the TCP socket connection between Avaya and the listener is broken, the script sends a notification to SNS for users to take action.

Pre-reqs:
- Setup IPOffice to send logs to the server/port where the py script is intended to run:
  * Oepn IOffice Manager
  * Go to System-->SMDR tab
  * Set Output to SMDR Only 
  * Set IP Address to the IP of the listener server (where py scripts will be executed)
  * Set TCP Port to the appropiate port. 
  * Records to Buffer: Default = 500. Range = 10 to 3000. The system can cache up to 3000 SMDR records if it detects a communications failure with destination address. If the cache is full, the system will begin discarding the oldest records for each new record.
- Configure Firehose delivery stream, S3 bucket, and necesssary roles in AWS... (eventually I'll put here a cloudformation script)
- Configure and subscribe to the proper SNS topic to receive notifications when the socket connection is lost


