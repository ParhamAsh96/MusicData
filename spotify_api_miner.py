import requests
import json

service = "https://dit009-spotify-assignment.vercel.app/api/v1"
url = f"{service}/artists/1HY2Jd0NmPuamShAr6KMms/albums"
response = requests.get(url)
data = response.json()

def saving_json(data, filename="artist.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

with open(data, "r") as json_file:
    data =  json.load(json_file)
    saving_json(data)