import requests
from bs4 import BeautifulSoup

# URL della pagina dell'esercizio
exercise_url = 'https://www.bodybuilding.com/exercises/rickshaw-carry'

# Effettua una richiesta HTTP GET per ottenere il contenuto della pagina web
response = requests.get(exercise_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Estrai il nome dell'esercizio
    name = soup.find('h1', class_='ExHeading ExHeading--h2 ExDetail-h2').text.strip()

    # Estrai la tipologia dell'esercizio
    type = soup.find('a', href='/exercises/exercise-type/strongman').text.strip()

    # Estrai il muscolo interessato dall'esercizio
    muscle = soup.find('a', href='/exercises/muscle/forearms').text.strip()

    # Estrai il livello dell'esercizio
    # level = soup.find('li').text.strip()

    print(f'name: {name}')
    print(f'type: {type}')
    print(f'muscle: {muscle}')
    # print(f'Livello dell\'esercizio: {level}')

else:
    print('Errore nella richiesta HTTP.')
