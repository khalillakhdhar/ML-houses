from flask import Flask,jsonify,request
app = Flask(__name__)
personnes=[
    { "nom":"Lakhdhar","prenom":"Khalil","email":"khalil@gmail.com","telephone":"20999888" },
    { "nom":"Lakhdhar","prenom":"ali","email":"ali@gmail.com","telephone":"20999111" },
    { "nom":"Sami","prenom":"Slim","email":"salimS@gmail.com","telephone":"20999800" },
           ]
#affichage de la liste des personnes
@app.route('/personnes', methods=['GET'])
def get_personnes():
    return jsonify(personnes)
@app.route('/personnes', methods=['POST'])
def add_personnes():
    nouvelle_personne=request.get_json()
    personnes.append(nouvelle_personne)
    return jsonify(nouvelle_personne)
@app.route('/personnes/<int:index>', methods=['GET'])
def get_personne(index):
    return jsonify(personnes[index])
@app.route('/personnes/<int:index>', methods=['DELETE'])
def delete_personne(index):
    personne_supprimee=personnes.pop(index)
    return jsonify(personne_supprimee)
if __name__ == '__main__':
    app.run(debug=True)