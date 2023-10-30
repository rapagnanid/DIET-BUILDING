import requests
from bs4 import BeautifulSoup
import sqlite3

# Funzione per effettuare il web scraping e inserire i dati nel database
def scrape_and_insert_data():
    # URL del sito da cui effettuare il web scraping
    url = 'https://www.bodybuilding.com/exercises/rickshaw-carry'

    # Effettua una richiesta HTTP GET per ottenere il contenuto della pagina web
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Estrai il nome dell'esercizio
        name = soup.find('h1', class_='ExHeading ExHeading--h2 ExDetail-h2').text.strip()

        # Estrai la tipologia dell'esercizio
        type = soup.find('a', href='/exercises/exercise-type/strongman').text.strip()

        # Estrai il muscolo interessato dall'esercizio
        muscle = soup.find('a', href='/exercises/muscle/forearms').text.strip()

        # Connessione al database SQLite
        connection = sqlite3.connect('scraped_data.db')
        cursor = connection.cursor()

        # Inserimento dei dati nella tabella
        cursor.execute('INSERT INTO scraped_data (name, type, muscle) VALUES (?, ?, ?)', (name, type, muscle))

        connection.commit()
        connection.close()

        print('Dati inseriti nel database con successo.')

    else:
        print('Errore nella richiesta HTTP.')

if __name__ == '__main__':
    scrape_and_insert_data()
