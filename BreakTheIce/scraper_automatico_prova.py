import requests
from bs4 import BeautifulSoup
import sqlite3

# Funzione per effettuare il web scraping e inserire i dati nel database
def scrape_and_insert_data(url, connection):
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

        # Inserimento dei dati nella tabella
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO scraped_data (name, overview, category, muscle, equipment, level, rating, description, alternative) '
            'VALUES '
            '(?, ?, ?, ?, ?, ?, '
            '?, ?, ?)',
            (name, overview, category, muscle, equipment, level, rating, description, alternative))

        connection.commit()
        cursor.close()

        print(f'Dati di {name} inseriti nel database con successo.')

    else:
        print(f'Errore nella richiesta HTTP per {url}.')

# URL iniziale
base_url = "https://www.bodybuilding.com/exercises//exercises/finder"
connection = sqlite3.connect('scraped_data.db')

# Lista per memorizzare tutti i blocchi
exercise_blocks = []

while True:
    # Effettua una richiesta GET per ottenere il contenuto della pagina
    response = requests.get(base_url)

    # Verifica se la richiesta è andata a buon fine
    if response.status_code == 200:
        # Parsing del contenuto HTML della pagina
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trova tutti i blocchi con la classe "ExResult-row"
        new_blocks = soup.find_all("div", class_="ExResult-row")

        if not new_blocks:
            # Nessun altro blocco trovato, esci dal loop
            break

        # Aggiungi i nuovi blocchi alla lista
        exercise_blocks.extend(new_blocks)

        # Trova il pulsante "Load More" per la prossima pagina
        load_more_button = soup.find("button", {"data-bb-action": "next"})

        if not load_more_button:
            # Nessun altro pulsante "Load More" trovato, esci dal loop
            break

        # Estrai l'attributo data-link dal pulsante "Load More" per ottenere il link alla pagina successiva
        next_page_link = load_more_button.get("data-link")

        # Costruisci il link completo per la prossima pagina
        base_url = f"https://www.bodybuilding.com{next_page_link}"
    else:
        print(f"Errore nella richiesta GET: {response.status_code}")
        break

# Ora hai tutti i blocchi in exercise_blocks
for exercise_block in exercise_blocks:
    link = exercise_block.find("a", itemprop="name")
    if link:
        exercise_url = link.get("href")
        full_url = f"https://www.bodybuilding.com{exercise_url}"
        scrape_and_insert_data(full_url, connection)

connection.close()
