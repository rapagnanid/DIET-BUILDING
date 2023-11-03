import requests
from bs4 import BeautifulSoup
import sqlite3


# Funzione per effettuare il web scraping e inserire i dati nel database per un singolo esercizio
def scrape_and_insert_data(url, connection):
    # Effettua una richiesta HTTP GET per ottenere il contenuto della pagina web
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Errore nella richiesta HTTP per l\'URL: {url}')
        return

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

    category = ''
    category_element = soup.find('a', href='/exercises/exercise-type/')
    if category_element:
        category = category_element.text.strip()

    muscle = ''
    muscle_element = soup.find('a', href='/exercises/muscle/')
    if muscle_element:
        muscle = muscle_element.text.strip()

    level = ''
    li = soup.find_all('li')
    for i in li:
        text = i.text.strip()
        if "Level" in text:
            parts = text.split(':')
            if len(parts) > 1:
                level = parts[1].strip()
                break

    rating = ''
    rating_element = soup.find('div', class_='ExRating-badge')
    if rating_element:
        rating = rating_element.text.strip()

    description = ''
    description_element = soup.find('div', class_='grid-8 grid-12-s grid-12-m', itemprop='description')
    if description_element:
        description = description_element.text.strip()

    alternative = ''
    alternative_element = soup.find('h3', class_='ExHeading ExResult-resultsHeading', itemprop='name')
    if alternative_element:
        alternative = alternative_element.text.strip()


    # Inserimento dei dati nel database
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO scraped_data (name, overview, category, muscle, level, rating, description, alternative) VALUES '
        '(?, ?, ?, ?, ?, '
        '?, ?, ?)',
        (name, overview, category, muscle, level, rating, description, alternative))
    connection.commit()
    cursor.close()

    print(f'Dati dell\'esercizio {name} inseriti nel database con successo.')


def main():
    # URL della pagina principale che elenca tutti gli esercizi
    main_url = 'https://www.bodybuilding.com/exercises/'

    # Connessione al database SQLite
    connection = sqlite3.connect('scraped_data.db')
    create_database(connection)

    # Effettua una richiesta HTTP GET per ottenere il contenuto della pagina principale
    response = requests.get(main_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trova tutti i link agli esercizi sulla pagina principale
        exercise_links = soup.find_all('a', class_='ExResult-resultsView-detail')

        # Estrai gli URL degli esercizi e chiama la funzione di scraping per ciascuno di essi
        for link in exercise_links:
            exercise_url = link['href']
            full_url = f'https://www.bodybuilding.com{exercise_url}'
            print(full_url)
            scrape_and_insert_data(full_url, connection)
    else:
        print('Errore nella richiesta HTTP per la pagina principale.')

    connection.close()


def create_database(connection):
    cursor = connection.cursor()

    # Crea una tabella per i dati se non esiste
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            overview TEXT,
            category TEXT,
            muscle TEXT,
            level TEXT,
            rating TEXT,
            description TEXT,
            alternative TEXT
        )
    ''')

    connection.commit()
    cursor.close()


if __name__ == '__main__':
    main()
