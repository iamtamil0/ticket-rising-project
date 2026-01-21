import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="aws-rds-endpoint.amazonaws.com",  # MySQL LAN IP
        user="ticket_user",
        password="StrongPass",
        database="ticket_rising"
    )