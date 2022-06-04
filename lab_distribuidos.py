import tweepy

consumer_key = "nPwaRHFONZzeJ6EDBWbtZdBqu"  #same as api key
consumer_secret = "JvEJJpNPvDiicXpPP0MEFr9bfpOxKxmxCfqlkHI8S3gcjjg8lm"  #same as api secret
access_key = "1532909672117981184-HjzNH90HN7STaT88JXDP51zhI3MSvu"
access_secret = "3cwcUHs6BUdbhFPgoKtkF6c7VcUeAQ6TW09WBWtEo46TO"

# Twitter authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)   
auth.set_access_token(access_key, access_secret) 
  
# Creating an API object 
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

# ----- Extract data for a particular user mention -----
'''
username_tweets = tweepy.Cursor(api.search_tweets, q="@usach", tweet_mode='extended').items(3)

for tweet in username_tweets:
    print("\n")
    text = tweet._json["full_text"]
    print(text)
    #using different attributes
    print(tweet.favorite_count)
    print(tweet.retweet_count)
    print(tweet.created_at)

'''

# ----- Extract data for a particular hashtag -----
'''
hashtag_tweets = tweepy.Cursor(api.search_tweets, q="#usach", tweet_mode='extended').items(5)

for tweet in hashtag_tweets:
    print("\n")
    text = tweet._json["full_text"]
    print(text)


 
# ----- Extract data tweets after a mentioned date -----

date_tweets = tweepy.Cursor(api.search_tweets, q="@usach", since="2020-5-31", tweet_mode='extended').items(5)

for tweet in date_tweets:
    print("\n")
    text = tweet._json["full_text"]
    print(text)
'''
