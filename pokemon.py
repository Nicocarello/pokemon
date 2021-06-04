from flask import Flask, request
import json
import requests

def load_data(limit=-1, offset=None, pokemon=""):
    base_url = 'https://pokeapi.co/api/v2/pokemon/{p}'.format(p=pokemon)
    url = f"{base_url}?limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return {"message": "Service not available"}

app = Flask(__name__)

@app.route('/pokemon', methods=['GET'])
def search_pokemon():
    q = request.args.get("q") or ""
    limit = request.args.get("limit")
    offset = request.args.get("offset")
    pokemons = load_data(limit, offset)
    found = (pokemon for pokemon in pokemons["results"] if q in str(pokemon["name"]))
    return str({"total": pokemons["count"], "limit": limit, "offset": offset, "data": list(found)}), 200


@app.route('/pokemon/<nombreDelPokemon>', methods=['GET'])
def get_pokemon(nombreDelPokemon):
    pokemons = load_data(pokemon=nombreDelPokemon)
    return pokemons

if __name__ == '__main__':
    app.run(debug=True)