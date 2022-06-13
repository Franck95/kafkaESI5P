import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.56.13:9092')
with open('demographieEurope_v.csv') as file:
    line = file.readline()
    while line: 
        producer.send('demographieEuropa', line.rstrip().encode('utf-8'))
        time.sleep(1)
        line = file.readline()

    