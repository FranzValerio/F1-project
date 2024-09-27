from urllib.request import urlopen
import json

response = urlopen('https://api.openf1.org/v1/sessions?country_name=Monaco&session_name=Race&year=2024')
data = json.loads(response.read().decode('utf-8'))
print(data)