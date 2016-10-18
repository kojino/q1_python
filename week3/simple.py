from flask import Flask, abort, redirect, request, url_for
import json

app = Flask(__name__)
pets_data = []

# 1
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/simple_pets', methods=['POST'])
def simple_pets():
    data = request.data
    Dict = json.loads(data)
    return str(Dict)

@app.route('/pets', methods=['POST','GET'])
def pets():
    if request.method == 'POST':
        new_data = []
        data = request.data
        Dict = json.loads(data)
        for pet in Dict["pets"]:
            if all (key in pet for key in ["name","age","species"]):
                new_pet = [pet["name"],pet["age"],pet["species"]]
                pets_data.append(new_pet)
                new_data.append(new_pet)
        return "Data stored: \n" + '\n'.join([', '.join(el) for el in new_data])
    if request.method == 'GET':
        return '\n'.join([', '.join(el) for el in pets_data])


@app.route('/pets/<name>')
def page(name):
    for pet in pets_data:
        if name == pet[0]:
            return ' '.join(pet)
    abort(404)
