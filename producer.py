from time import sleep
from json import dumps
from kafka import KafkaProducer

'''
- we have created a KafkaProducer object that connects of our local instance of Kafka;
- we have defined a way to serialize the data we want to send by trasforming it into a 
  json string and then encoding it to UTF-8;
- we send an event every 0.5 seconds with topic named topic_test and the counter of the 
  iteration as data. Instead of the couter, you can send anything.
'''

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

for j in range(9999):
    print("Iteration", j)
    data = {'counter': j}
    producer.send('topic_test', value=data)
    sleep(0.5)


