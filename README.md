# Amazon Managed Streaming for Apache Kafka-RDS-EC2-AWS
- Install MSK cluster, Make a note on security groups.
- EC2 instances, create a key pairs
            File format in pem. 
            Launch instance, choose a free tier. 
            Use a powershell to connect EC2
- Get the kafka binaries from the files.
  https://kafka.apache.org/downloads
- untar Kafka_2.13-2.8.0.tgz
- Install java on EC2.
- Careate a toipc on EC2 instance as, https://docs.aws.amazon.com/msk/latest/developerguide/create-topic.html
- Careate a topics using the follwoing command, bin/kafka-topics.sh --create --zookeeper "ZookeeperConnectString" --replication-factor 3 --partitions 1 --topic AWSKafkaTutorialTopic
- The ZookeeperConnectStrig looks like this, z-1.mskcsv.******.c4.kafka.eu-north-1.amazonaws.com:2181 (Find on MSK)
- Create a Postgres DB on aws
- Use this scheme to create the table,

CREATE TABLE msksc.cust_dat (
username VARCHAR(50) NOT NULL,
sub_no int NOT NULL,
city VARCHAR (50) NOT NULL,
country VARCHAR (50) NOT NULL
);

- Copy the python files to EC2 instance.
- Run the code producer and consumer codes on two different terminals,
- python3 consumer.py
- python3 producer.py

- Extra infromation, please edit inbounds on EC2 and RDS to allow traffic.
- Sometimes need editing routes and network gateways too.


