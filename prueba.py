import tweepy
import psycopg2
from psycopg2 import Error

def autenticar(api_key, api_secret, access_token, access_secret):
    # Twitter authentication
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
  
    # Creating an API object 
    return tweepy.API(auth)

def conectarBD(nombreBD, userBD, pswBD, hostBD, portBD = "5432"):
    conn = None
    try:
        print("\tConectando con: ~", nombreBD, "~ de PostgreSQL...")
        conn = psycopg2.connect(database = nombreBD, user = userBD, password = pswBD, host = hostBD, port = portBD)
        cur = conn.cursor()
    
        print('Version de la base de datos PostgreSQL:')
        cur.execute('SELECT version()')

        #Se muestra la version
        db_version = cur.fetchone()
        print(db_version)

        #Se cierra la comunicacion con PostgreSQL
        cur.close()
        print("\nLa conexión a", nombreBD, "ha sido exitosa.")    


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        print("No ha sido posible conectarse a", nombreBD, ".")

    finally:
        if conn is not None:
            conn.close()
            print('\tDatabase connection closed.\n')

def crearTabla(nombreBD, userBD, pswBD, hostBD, portBD = "5432"):
    sql = (
    """
    CREATE TABLE IF NOT EXISTS tweet
    (
	id SERIAL PRIMARY KEY,
	content VARCHAR(350) NOT NULL
    )
    """)
    
    conn = None
    try:
        print("\tConectando con: ~", nombreBD, "~ de PostgreSQL...")
        conn = psycopg2.connect(database = nombreBD, user = userBD, password = pswBD, host = hostBD, port = portBD)
        cur = conn.cursor()

        #Se crea la tabla
        cur.execute(sql)

        #Se cierra la comunicacion con PostgreSQL
        cur.close()
        print("\nLa tabla ha sido creada exitosamente.")

        #Se almacenan los cambios
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('\tDatabase connection closed.\n')

def insertarInstancia(datos, nombreBD, userBD, pswBD, hostBD, portBD = "5432"):
    sql = "insert into tweet values (DEFAULT, %s)"

    conn = None
    try:
        conn = psycopg2.connect(database = nombreBD, user = userBD, password = pswBD, host = hostBD, port = portBD)
        cur = conn.cursor()

        #Se crea la tabla
        cur.execute(sql, datos)

        #Se cierra la comunicacion con PostgreSQL
        cur.close()
        print("\nEl dato ha sido insertado exitosamente.")

        #Se almacenan los cambios
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def limpiarTabla(nombreBD, userBD, pswBD, hostBD, portBD = "5432"):
    sql = (
    """
    TRUNCATE TABLE tweet
    RESTART IDENTITY;
    """)

    conn = None
    try:
        print("\tConectando con: ~", nombreBD, "~ de PostgreSQL...")
        conn = psycopg2.connect(database = nombreBD, user = userBD, password = pswBD, host = hostBD, port = portBD)
        cur = conn.cursor()

        #Se crea la tabla
        cur.execute(sql)

        #Se cierra la comunicacion con PostgreSQL
        cur.close()
        print("\nLa tabla ha sido limpiada exitosamente.")

        #Se almacenan los cambios
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('\tDatabase connection closed.\n')
    


#Llaves y Tokens
api_key = "nPwaRHFONZzeJ6EDBWbtZdBqu" #Esta se obtiene de la parte de Consumer keys
api_key_secret = "JvEJJpNPvDiicXpPP0MEFr9bfpOxKxmxCfqlkHI8S3gcjjg8lm" #Esta se obtiene de la parte de Consumer keys

access_token = "1532909672117981184-HjzNH90HN7STaT88JXDP51zhI3MSvu" #Esta se obtiene de Authentication Tokens
access_token_secret = "3cwcUHs6BUdbhFPgoKtkF6c7VcUeAQ6TW09WBWtEo46TO" #Esta se obtiene de Authentication Tokens




#Autenticacion
api = autenticar(api_key, api_key_secret, access_token, access_token_secret)




#Conexion a base de datos
    #Parametros de la BD
nombreBD = "distribuidos_twitter"
userBD = "postgres"
pswBD = "admin"
host = "localhost"

    #CONEXION a la BD
conectarBD(nombreBD, userBD, pswBD, host)

#Crear tabla base de datos
crearTabla(nombreBD, userBD, pswBD, host)


#Procedimientos
limpiarTabla(nombreBD, userBD, pswBD, host)


hashtag_tweets = tweepy.Cursor(api.search_tweets, q="#usach", tweet_mode='extended').items(3)

for tweet in hashtag_tweets:
    text = tweet._json["full_text"]
    dato = (text,)
    insertarInstancia(dato, nombreBD, userBD, pswBD, host)



