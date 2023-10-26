import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import NutritionalData

# Definisci l'URL base dell'API dell'USDA Food Composition Database
base_url = "https://api.nal.usda.gov/fdc/v1/"

# Definisci il tuo API key dell'USDA Food Composition Database (è necessario registrarsi per ottenerlo)
api_key = "mNATibUlWvIOuWV8jcbPA186fzcFW2efUA921Lra"  # Sostituisci con la tua chiave API USDA

# Connetti al tuo database
engine = create_engine('mysql://root:Cocodemer.95@localhost/FooD')  # Sostituisci con la tua configurazione di database

# Crea una sessione per interagire con il database
Session = sessionmaker(bind=engine)
session = Session()

# Crea una funzione per ottenere i dati nutrizionali di un alimento per nome
def get_nutritional_data(food_name):
    # Costruisci l'URL completo per la richiesta all'API
    search_url = f"{base_url}foods/search?query={food_name}&api_key={api_key}"

    try:
        # Esegui la richiesta GET all'API
        response = requests.get(search_url)
        response.raise_for_status()  # Controlla se la richiesta ha avuto successo
        data = response.json()  # Estrai i dati JSON dalla risposta

        # Estrai i dati nutrizionali desiderati dalla risposta JSON
        nutritional_data = data['foods'][0]['foodNutrients']

        # Salva i dati nel database
        for nutrient in nutritional_data:
            db_entry = NutritionalData(
                food_name=food_name,
                nutrient_name=nutrient['nutrientName'],
                nutrient_value=nutrient['value'],
                unit_name=nutrient['unitName']
            )
            session.add(db_entry)

        # Conferma le modifiche nel database
        session.commit()

        return nutritional_data

    except requests.exceptions.HTTPError as err:
        print(f"Errore nella richiesta all'API: {err}")
        return None

# Esempio: ottieni i dati nutrizionali per una mela e salvali nel database
nutritional_data = get_nutritional_data("apple")
if nutritional_data:
    for nutrient in nutritional_data:
        print(f"{nutrient['nutrientName']}: {nutrient['value']} {nutrient['unitName']}")
