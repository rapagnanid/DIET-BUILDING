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

from googletrans import Translator

def translate_to_english(food_name):
    translator = Translator()
    translated = translator.translate(food_name, src='it', dest='en')
    return translated.text

def get_nutritional_data_in_real_time(food_name_italian):
    # Traduci il nome dell'alimento in italiano in inglese
    food_name_english = translate_to_english(food_name_italian)

    # Cerca se i dati sono già presenti nel database
    existing_data = session.query(NutritionalData).filter_by(food_name=food_name_english).all()

    if existing_data:
        # Se i dati esistono nel database, restituiscili
        nutritional_data = [{
            'nutrientName': entry.nutrient_name,
            'value': entry.nutrient_value,
            'unitName': entry.unit_name
        } for entry in existing_data]
    else:
        # Se i dati non sono presenti, effettua la richiesta all'API con il nome in inglese
        search_url = f"{base_url}foods/search?query={food_name_english}&api_key={api_key}"

        try:
            response = requests.get(search_url)
            response.raise_for_status()
            data = response.json()

            nutritional_data = data['foods'][0]['foodNutrients']

            # Salva i dati nel database con il nome in inglese
            for nutrient in nutritional_data:
                db_entry = NutritionalData(
                    food_name=food_name_english,
                    nutrient_name=nutrient['nutrientName'],
                    nutrient_value=nutrient['value'],
                    unit_name=nutrient['unitName']
                )
                session.add(db_entry)

            session.commit()
        except requests.exceptions.HTTPError as err:
            print(f"Errore nella richiesta all'API: {err}")
            nutritional_data = []

    return nutritional_data
