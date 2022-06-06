import tweepy
import json
from time import sleep
from json import dumps
from kafka import KafkaProducer


consumer_key = "nPwaRHFONZzeJ6EDBWbtZdBqu"  #same as api key
consumer_secret = "JvEJJpNPvDiicXpPP0MEFr9bfpOxKxmxCfqlkHI8S3gcjjg8lm"  #same as api secret
access_key = "1532909672117981184-HjzNH90HN7STaT88JXDP51zhI3MSvu"
access_secret = "3cwcUHs6BUdbhFPgoKtkF6c7VcUeAQ6TW09WBWtEo46TO"

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)   
auth.set_access_token(access_key, access_secret) 
  
# Creating an API object 
api = tweepy.API(auth)

# ----- Extract data for a particular hashtag -----

hashtag_tweets = tweepy.Cursor(api.search_tweets, q="#usach", tweet_mode='extended').items(5)

'''
for tweet in hashtag_tweets:
    print("\n")
    text = tweet._json["full_text"]
    print(text)
'''


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


j = 0
for tweet in hashtag_tweets:
    print("Iteration", j)
    data = tweet._json["full_text"]
    producer.send('topic_test2', value=data)
    sleep(0.5)
    j = j+1


