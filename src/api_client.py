import requests

url = "https://api.opendota.com/api/players/184224934"

response = requests.get(url)
data = response.json()

player_id = "184224934"

print(data)