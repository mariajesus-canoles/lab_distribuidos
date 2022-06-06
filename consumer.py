from kafka import KafkaConsumer
from json import loads
from time import sleep

'''
In the script above we are defining a KafkaConsumer that contacts the server “localhost:9092 ” 
and is subscribed to the topic “topic_test”. Since in the producer script the message is 
jsonfied and encoded, here we decode it by using a lambda function in value_deserializer. 
In addition, -auto_offset_reset is a parameter that sets the policy for resetting offsets 
on OffsetOutOfRange errors; if we set “earliest” then it will move to the oldest available 
message, if “latest” is set then it will move to the most recent;
-enable_auto_commit is a boolean parameter that states whether the offset will be 
periodically committed in the background;
-group_id is the name of the consumer group to join.
In the loop we print the content of the event consumed every 2 seconds. Instead of printing, 
we can perfom any task like writing it to a database or performing some real time analysis.
'''

consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    sleep(2)