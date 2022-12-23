import requests

ENDPOINT_POKEAPI = 'https://pokeapi.co/api/v2/pokemon/ditto'

response = requests.get(ENDPOINT_POKEAPI)
#print(response.status_code)
response = response.json()
# print(response)

abilities = response['abilities'][0]
ability_name = abilities['ability']['name']

if 'imposter' in ability_name:
    print('Y')
else:
    print('N')
