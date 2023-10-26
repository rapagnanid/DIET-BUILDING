from models import NutritionalData

import mysql.connector

# Configura i dettagli di connessione
db_connection = mysql.connector.connect(
    host="localhost",  # L'indirizzo del server MySQL
    user="root",        # L'utente MySQL
    password="Cocodemer.95"  # La password dell'utente MySQL
)

if db_connection.is_connected():
    print("Connessione a MySQL riuscita!")
    db_connection.close()
else:
    print("Connessione a MySQL non riuscita.")
