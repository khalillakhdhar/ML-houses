from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    # Récupération des paramètres d'entrée
    montant = float(request.json['montant'])
    devise_depart = request.json['devise_depart']
    devise_cible = request.json['devise_cible']

    # Appel à l'API tierce pour récupérer le taux de change
    url = f'https://api.exchangeratesapi.io/latest?base={devise_depart}&symbols={devise_cible}'
    response = requests.get(url)
    taux_de_change = response.json()['rates'][devise_cible]

    # Calcul de la conversion
    montant_converti = montant * taux_de_change

    # Création du résultat JSON
    result = {
        'montant': montant,
        'devise_depart': devise_depart,
        'devise_cible': devise_cible,
        'montant_converti': montant_converti
    }

    return result, 200

if __name__ == '__main__':
    app.run(debug=True)
