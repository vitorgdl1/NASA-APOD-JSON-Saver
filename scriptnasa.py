import json
import requests

resposta = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')

try:
    if resposta.ok:
        with open("dados.json", "w") as arquivo:
            dados = resposta.json()
            json.dump(dados, arquivo)
            print('sucesso')
    else:
        print('erro ' + str(resposta.status_code))
        
except requests.exceptions.ConnectionError as x:
    print(x)
    
