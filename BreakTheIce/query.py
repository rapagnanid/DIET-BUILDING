import sqlite3

def retrieve_data():
    connection = sqlite3.connect('scraped_data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM scraped_data')
    data = cursor.fetchall()

    connection.close()

    return data

if __name__ == '__main__':
    data = retrieve_data()
    for row in data:
        print(f'name: {row[1]}')
        print(f'type: {row[2]}')
        print(f'muscle: {row[3]}')
        print(f'rating: {row[4]}')
        print(f'description: {row[5]}')
        print(f'level: {row[6]}')
        print(f'alternative: {row[7]}')
