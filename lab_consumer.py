from kafka import KafkaConsumer
from json import loads
from time import sleep
import tweepy
import psycopg2
from psycopg2 import Error

def crearTabla(nombreBD, userBD, pswBD, hostBD, portBD = "5432"):
    sql = (
    """
    CREATE TABLE IF NOT EXISTS tweet
    (
	id SERIAL PRIMARY KEY,
	content VARCHAR(500) NOT NULL,
    retweets INT NOT NULL,
    favorites INT NOT NULL
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
    sql = "insert into tweet values (DEFAULT, %s, %s, %s)"

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
    'topic_test2',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

#Conexion a base de datos
    #Parametros de la BD
nombreBD = "distribuidos_twitter"
userBD = "postgres"
pswBD = "admin"
host = "localhost"

#Crear tabla base de datos
crearTabla(nombreBD, userBD, pswBD, host)

#Procedimientos
limpiarTabla(nombreBD, userBD, pswBD, host)


for event in consumer:
    dato = (event.value['content'], event.value['retweets'], event.value['favorites'],) #ESTA COMA ES IMPORTANTE PARA QUE EL INSERT FUNCIONE AUTOINCREMENTABLE
    insertarInstancia(dato, nombreBD, userBD, pswBD, host)
    #sleep(0.1)