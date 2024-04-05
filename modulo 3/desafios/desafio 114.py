import requests

try:
    resposta = requests.get('https://www.youtube.com.br/')
    if resposta.status_code == 200:
        print(f'\033[1;93mFoi possível acessar o YouTube.\033[m')

except:
    print(f'\033[1;91mNão foi possível acessar o YouTube.')