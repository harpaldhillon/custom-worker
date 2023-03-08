import requests

result = requests.get(
    'https://localhost:8080/',
    cert=('client.crt', 'client.key'),
    verify='ca.crt')

print(result.content)

# do something with result...
