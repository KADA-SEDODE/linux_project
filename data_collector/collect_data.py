import pandas as pd
import requests

def fetch_data_from_api(limit=100, offset=0):
    url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/dans-ma-rue/records?"
    response = requests.get(url, params={'limit': limit, 'offset': offset})
    print(f"Requête envoyée : {response.url}")
    print(f"Statut de la réponse : {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Détails de l'erreur : {response.text}")
        return []

def fetch_all_data(limit=100):
    all_data = []
    offset = 0
    max_records = 10000

    while offset < max_records:
        records = fetch_data_from_api(limit=limit, offset=offset)
        if records:
            all_data.extend(records)
            offset += limit
        else:
            break

    df = pd.DataFrame(all_data)
    df.to_csv("raw_data.csv", index=False)
    print("Les données brutes ont été enregistrées dans raw_data.csv")

if __name__ == "__main__":
    fetch_all_data()
