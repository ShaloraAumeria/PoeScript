#https://www.pathofexile.com/api/trade2/search/poe2/Standard


import requests

def search_poe_trade(item_name):

    client_id = 'shaloraprice'
    client_secret = 'sjödlfkv8wdsfkuhj'
    grant_type = 'client_credentials'
    scope = 'service:psapi'
    version = '1.0.0'
    contact = 'torashelly@gmail.com'
    # Request payload

    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type,
        'scope': scope
    }

    headers = {
        'User-Agent': f'OAuth {client_id}/{version} (contact: {contact}) StrictMode'
    }

    response = requests.post('https://www.pathofexile.com/oauth/token', data=payload,headers=headers)

    if response.status_code == 200:
        # Access token obtained successfully
        response_data = response.json()
        access_token = response_data['access_token']
        expires_in = response_data['expires_in']
        token_type = response_data['token_type']
        username = response_data['username']
        sub = response_data['sub']
        scope = response_data['scope']
    else:
        print("error on access fetch")


    # URL der PoE Trade API
    url = 'https://www.pathofexile.com/api/trade2/search/poe2/Standard'
    
    # Senden Sie die Anfrage an die API
    response = requests.post(url, json={
        "query": {
            "status": {"option": "online"},
            "itemName": item_name
        }
    })

    if response.status_code == 200:
        # Die Antwort wurde erfolgreich erhalten
        data = response.json()
        print("Suchergebnisse:")
        
        # Anzeigen der Suchergebnisse
        for result in data['result']:
            print(f"Item ID: {result}")
    else:
        print(f"Fehler bei der Anfrage: {response.status_code}")

if __name__ == "__main__":
    #item_name = input("Geben Sie den Namen des Gegenstands ein, nach dem Sie suchen möchten: ")
    search_poe_trade("quill")