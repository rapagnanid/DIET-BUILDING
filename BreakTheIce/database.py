import sqlite3

def create_database():
    connection = sqlite3.connect('scraped_data.db')
    cursor = connection.cursor()

    # Crea una tabella per i dati
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            overview TEXT,
            category TEXT,
            muscle TEXT,
            equipment TEXT,
            level TEXT,
            rating TEXT,
            description TEXT,
            alternative TEXT
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_database()