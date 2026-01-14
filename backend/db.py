import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="DB_HOST",
        user="DB_USER",
        password="DB_PASSWORD",
        database="ticket_rising"
    )