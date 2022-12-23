import requests
from flask import Flask, request
from flask_api import status

app = Flask(__name__)

def controller_poke(headers):

    _url = 'http://127.0.0.1:9001/auth'
    _headers = {'uuid':headers['uuid']}
    _token = request.cookies.get('jwt')
    _response = requests.get(url=_url, headers=_headers, cookies={'jwt':_token})

    _response = _response.json()

    if not _response['authenticated']:
        return _response
    
    try:
        endpoint_poke_api = headers['endpoint_poke_api']
        exists_ability_name = headers['ability_name']
        ability_range = headers['ability_range']

        ability_range = int(ability_range)

        response = requests.get(endpoint_poke_api)
        response = response.json()
        
        abilities = response['abilities'][ability_range]
        ability_name = abilities['ability']['name']

    except Exception as e:
        return {'error':e.args[0]}, 400
    else:
        if exists_ability_name in ability_name:
            return {'exists_ability_name':True}, 200
        return {'exists_ability_name':False}, 200

@app.route('/poke')
def poke():
    response = controller_poke(request.headers)
    return response

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000, debug=True)