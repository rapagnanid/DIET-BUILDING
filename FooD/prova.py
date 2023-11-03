import requests

def get_all_fields_for_food(food_id):
    # Sostituisci 'YOUR_API_KEY' con la tua chiave API dell'USDA
    api_key = 'YmNATibUlWvIOuWV8jcbPA186fzcFW2efUA921Lra'
    base_url = 'https://api.nal.usda.gov/fdc/v1/foods'

    try:
        response = requests.get(f"{base_url}/{food_id}?api_key={api_key}")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        print(f"Errore nella richiesta all'API: {err}")
        return None

get_all_fields_for_food(1)