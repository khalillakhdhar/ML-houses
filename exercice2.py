from flask import Flask, jsonify, request

app = Flask(__name__)

# Define some initial products
products = [
    {'id': 1, 'nom': 'Chaise', 'prix': 50.0, 'quantite': 10},
    {'id': 2, 'nom': 'Table', 'prix': 100.0, 'quantite': 5},
    {'id': 3, 'nom': 'Canapé', 'prix': 200.0, 'quantite': 2}
]

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})

# Get one product by id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    return jsonify({'product': product[0]})

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    if not request.json or not 'nom' in request.json or not 'prix' in request.json or not 'quantite' in request.json:
        abort(400)
    product = {
        'id': products[-1]['id'] + 1,
        'nom': request.json['nom'],
        'prix': request.json['prix'],
        'quantite': request.json['quantite']
    }
    products.append(product)
    return jsonify({'product': product}), 201

# Update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'nom' in request.json and not isinstance(request.json['nom'], str):
        abort(400)
    if 'prix' in request.json and not isinstance(request.json['prix'], float):
        abort(400)
    if 'quantite' in request.json and not isinstance(request.json['quantite'], int):
        abort(400)
    product[0]['nom'] = request.json.get('nom', product[0]['nom'])
    product[0]['prix'] = request.json.get('prix', product[0]['prix'])
    product[0]['quantite'] = request.json.get('quantite', product[0]['quantite'])
    return jsonify({'product': product[0]})

# Delete a product by id
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
