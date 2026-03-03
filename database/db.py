import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Holymary2005**", # Your local password from source
        database="icoms"
    )