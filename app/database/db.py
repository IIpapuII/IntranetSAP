import os
import psycopg2
from dotenv import load_dotenv
from hdbcli import dbapi

load_dotenv()
def get_db():
    db_conn = psycopg2.connect (
        host = os.getenv('hostdb'),
        database = os.getenv('database'),
        user = os.getenv('userDB'),
        password= os.getenv('passwordDB')
    )
    print("conectado")
    return db_conn.cursor()

def get_hana():
    coon = dbapi.connect(
    address= os.getenv('SERVERSAP'),
    user= os.getenv('USERSAP'),
    port= os.getenv('PORTSAP'),
    password= os.getenv('PASSWORDSAP')
    
    )
    print('conectado')

    return coon