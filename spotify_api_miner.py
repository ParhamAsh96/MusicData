import requests, json, os


playlist_gym_hits = "artists/7dGJo4pcD2V6oG8kP0tJRR/albums"

service = "https://dit009-spotify-assignment.vercel.app/api/v1/"
url = f"{service}{playlist_gym_hits}"
response = requests.get(url)
data = response.json()
print(data)


# Save extracted data to JSON file
def saving_json(data, filename="artist_albums"):
    with open(f'MusicData/resources/{filename}.json', "w") as file:
        json.dump(data, file, indent=4)

saving_json(data)

# os.remove(f'MusicData/resources/artist_albums.json')