import requests, json, os


artist_id = "7dGJo4pcD2V6oG8kP0tJRR"

def spotify_api():
    api_token = "https://dit009-spotify-assignment.vercel.app/api/v1/"
    url = f"{api_token}artists/{artist_id}/albums"
    response = requests.get(url)
    data = response.json()
    return data


def saving_json(data, filename=f"artist_{artist_id}"):
    with open(f'MusicData/resources/{filename}.json', "w") as file:
        json.dump(data, file, indent=4)

data = spotify_api()
saving_json(data)

# os.remove(f'MusicData/resources/artist_albums.json')