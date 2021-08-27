from kafka import KafkaConsumer
import psycopg2
from json import loads

consumer = KafkaConsumer('awskafkatopic1',bootstrap_servers=['b-1.mskcsv.lk7gvq.c4.kafka.eu-north-1.amazonaws.com:9092'],consumer_timeout_ms=10000)


#conn = psycopg2.connect(
#            database = "mskdatabase",
#            user = "postgres",
#            password = "Admin1234",
#            host = "database-1.c93rjjowwu18.eu-north-1.rds.amazonaws.com",
#            port = "5432"
#            )

conn = psycopg2.connect(dbname='mskdatabase',user='postgres',host='16.170.138.152',password='Admin1234',port='5432')

#conn.close()
#def postgres_test():
#    try:
#        conn = psycopg2.connect(dbname='mskdatabase',user='postgres',host='base-1.c93rjjowwu18.eu-north-1.rds.amazonaws.com',
#                password='Admin1234',port='5432')
#conn.close()
#        return print("Connected to DB successfully")
#    except:
#        return print("Connection failed")

#postgres_test()

cur = conn.cursor()


try:
cur.execute("SELECT * FROM msksc.cust_dat")
except psycopg2.Error as e:
print(e)
num = 0
for msg in consumer:
#consumer.commit()
num = num + 1
rec_data = msg.value.decode('utf-8')
r = rec_data.replace('"','')
record = r.strip('\\n')
f_rec = record.split(",")
name = f_rec[0]
city = f_rec[1]
country = f_rec[2]
print(name)
print(city)
print(record)
query = "INSERT INTO msksc.cust_dat(username, sub_no, city,country) VALUES (%s,%s, %s, %s);"
data = (name, num, city, country)
cur.execute(query, data)
#cur.fetchall()

consumer.close()
conn.commit()
cur.fetchall()
conn.close()