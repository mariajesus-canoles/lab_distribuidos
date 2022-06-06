import tweepy
import psycopg2
from json import dumps
import time
from datetime import datetime
from psycopg2 import Error
from kafka import KafkaConsumer, KafkaProducer

def autenticar(api_key, api_secret, access_token, access_secret):
    # Twitter authentication
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
  
    # Creating an API object 
    return tweepy.API(auth)

def normalizar_marca_tiempo(time):
    mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S+00:00")
    return (mytime.strftime("%Y-%m-%d %H:%M:%S"))

def obtener_datos_twitter():
    streaming = api.search_tweets("USACH")

    for i in streaming:
        text = ''
        text += str(i.user.id_str)
        text += ';'
        text += str(normalizar_marca_tiempo(str(i.created_at)))
        text += ';'
        text += str(i.user.followers_count)
        text += ';'
        text += str(i.user.location)
        text += ';'
        text += str(i.favorite_count)
        text += ';'
        text += str(i.retweet_count)
        text += ';'
        productor.send(nombre_topico, str.encode(text))

def periodo_recoleccion(intervalo):
    while True:
        obtener_datos_twitter()
        time.sleep(intervalo)
    
#Llaves y Tokens
api_key = "nPwaRHFONZzeJ6EDBWbtZdBqu" #Esta se obtiene de la parte de Consumer keys
api_key_secret = "JvEJJpNPvDiicXpPP0MEFr9bfpOxKxmxCfqlkHI8S3gcjjg8lm" #Esta se obtiene de la parte de Consumer keys

access_token = "1532909672117981184-HjzNH90HN7STaT88JXDP51zhI3MSvu" #Esta se obtiene de Authentication Tokens
access_token_secret = "3cwcUHs6BUdbhFPgoKtkF6c7VcUeAQ6TW09WBWtEo46TO" #Esta se obtiene de Authentication Tokens

#Autenticacion
api = autenticar(api_key, api_key_secret, access_token, access_token_secret)

#Se especifican las credenciales de kafka productor
productor = KafkaProducer(
    bootstrap_servers = ["localhost:9092"]#,
    #value_serializer=lambda x: dumps(x).encode('utf-8')
)
nombre_topico = "topico_twitter_1"

#Procedimientos
cantidad_tweets = 5
#hashtag_tweets = tweepy.Cursor(api.search_tweets, q="#usach", tweet_mode='extended').items(cantidad_tweets)

obtener_datos_twitter()
periodo_recoleccion(60*0.1)