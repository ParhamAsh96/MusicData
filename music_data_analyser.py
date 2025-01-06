import json
from spotify_api_miner import *

content = reading_json('MusicData/resources/artists_list.json')
artists = []
ids = []

def creating_list_of_artists(content):
    for artist_name, artist_id in content.items():
        artists.append(artist_name.casefold())
        ids.append(artist_id)

    return artists, ids

artists, ids = creating_list_of_artists(content)
    
for artist, id in zip(artists, ids):
    print(f"Artist: {artist}\n    ID: {id}\n")

chosen_artists_name = []
chosen_artists_id = []
try:
    invalid_input = False
    while not invalid_input and len(chosen_artists_name) < 2:
        chosen_artist = input("Please choose two artists from the list above for comparing: ").casefold()
        
        if chosen_artist in artists:
            chosen_artists_name.append(chosen_artist)
            #chosen_artists_id.append(ids)
            invalid_input = True

        elif chosen_artist not in artists:
            print(f"The artist, {chosen_artist.capitalize()} that you've chosen is not in the list. Please choose an artist from the list.")

        if len(chosen_artists_name) < 2:
            invalid_input = False
            
    print(f"Your first artist: {chosen_artists_name[0].upper()} \nYour second artist: {chosen_artists_name[1].upper()}")
    print(chosen_artists_id)

except Exception as e:
    print(f"Something went wrong: {e}.")