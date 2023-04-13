import requests
poke_api_url='https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_details(pokemon):
    pokemon=str(pokemon).strip().lower()
    if pokemon=='':
        print('Error No pockemon specified')
        return
    print(f'Getting Information for {pokemon}...',end='')
    url=poke_api_url+pokemon
    resp_msg=requests.get(url)

    if resp_msg.status_code==requests.codes.ok:
        print('Success')
        return resp_msg.json()
    else:
        print('Faliure')
        print(f'response code: {resp_msg.status_code} ({resp_msg.reason}')
        return