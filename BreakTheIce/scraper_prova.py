import requests
from bs4 import BeautifulSoup
import sqlite3

# Funzione per effettuare il web scraping e inserire i dati nel database
def scrape_and_insert_data():
    # URL del sito da cui effettuare il web scraping
    url = 'https://www.bodybuilding.com/exercises/single-leg-press'

    # Effettua una richiesta HTTP GET per ottenere il contenuto della pagina web
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Estrai i dati desiderati dall'esercizio
        name = ''
        name_element = soup.find('h1', class_='ExHeading ExHeading--h2 ExDetail-h2', itemprop='name')
        if name_element:
            name = name_element.text.strip()

        overview = ''
        overview_element = soup.find('div', class_='ExDetail-shortDescription grid-10')
        if overview_element:
            overview = overview_element.text.strip()

        list_items = soup.select('ul.bb-list--plain li')
        category = ''
        category_element = list_items[0]
        if category_element:
            category = category_element.text.strip().split(":")[1].strip()

        muscle = ''
        muscle_element = list_items[1]
        if muscle_element:
            muscle = muscle_element.text.strip().split(":")[1].strip()

        equipment = ''
        equipment_element = list_items[2]
        if equipment_element:
            equipment = equipment_element.text.strip().split(":")[1].strip()

        level = ''
        level_element = list_items[3]
        if level_element:
            level = level_element.text.strip().split(":")[1].strip()

        rating = ''
        rating_element = soup.find('div', class_='ExRating-badge')
        if rating_element:
            rating = rating_element.text.strip()

        description = ''
        description_element = soup.find('div', class_='grid-8 grid-12-s grid-12-m', itemprop='description')
        if description_element:
            description = description_element.text.strip()

        alternative = ''
        alternative_element = soup.find('h3', class_='ExHeading ExResult-resultsHeading')
        if alternative_element:
            alternative = alternative_element.text.strip()

        # Connessione al database SQLite
        connection = sqlite3.connect('scraped_data.db')
        cursor = connection.cursor()

        # Inserimento dei dati nella tabella
        cursor.execute(
            'INSERT INTO scraped_data (name, overview, category, muscle, equipment, level, rating, description, alternative) '
            'VALUES '
            '(?, ?, ?, ?, ?, ?, '
            '?, ?, ?)',
            (name, overview, category, muscle, equipment, level, rating, description, alternative))

        connection.commit()
        connection.close()

        print('Dati inseriti nel database con successo.')

    else:
        print('Errore nella richiesta HTTP.')

if __name__ == '__main__':
    scrape_and_insert_data()