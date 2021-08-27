from kafka import KafkaProducer
import json
from time import sleep

prod = KafkaProducer(bootstrap_servers=['b-1.mskcsv.lk7gvq.c4.kafka.eu-north-1.amazonaws.com:9092'])

f = open("/home/ec2-user/Data.csv","r")

for msg in f:
    data=msg
    prod.send('awskafkatopic1',json.dumps(data).encode('utf-8'))
    sleep(2)
    print(data)
    #prod.flush()
    #print("Hello world")