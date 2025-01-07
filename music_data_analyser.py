import json

def read_json(data):
    with open(f'{data}', "r") as file:
        content = json.load(file)
    return content


artists = []
ids = []

def creating_list_of_artists(content):
    for artist_name, artist_id in content.items():
        artists.append(artist_name.casefold())
        ids.append(artist_id)

    return artists, ids


content = read_json('MusicData/resources/artists_list.json')
artists, ids = creating_list_of_artists(content)
    
for artist, id in zip(artists, ids):
    print(f"Artist: {artist}\n    ID: {id}\n")


def choose_artists():
    chosen_artists_name = []
    chosen_artists_id = []
    try:
        invalid_input = False
        while not invalid_input and len(chosen_artists_name) < 2:
            chosen_artist = input("Please choose two artists from the list above for comparing: ").casefold()
            
            if chosen_artist in chosen_artists_name:
                print(f"{chosen_artist.capitalize()} is already chosen. Please choose another artis.")

            elif chosen_artist not in artists:
                print(f"The artist, {chosen_artist.capitalize()} that you've chosen is not in the list. Please choose an artist from the list.")
        
            elif chosen_artist in artists and chosen_artist not in chosen_artists_name:
                index = artists.index(chosen_artist)
                chosen_artists_name.append(chosen_artist)
                chosen_artists_id.append(ids[index])
                print(f"Your choice: {chosen_artist.capitalize()}")
                invalid_input = True

            if len(chosen_artists_name) < 2:
                invalid_input = False
                
        print(f"Your first artist: {chosen_artists_name[0].upper()} \nYour second artist: {chosen_artists_name[1].upper()}")

    except Exception as e:
        print(f"Something went wrong: {e}.")

    return chosen_artists_name, chosen_artists_id


def read_chosen_json():
    chosen_artists_name, chosen_artists_id = choose_artists()
    artist_one = read_json(f'MusicData/resources/{chosen_artists_name[0]}_{chosen_artists_id[0]}.json')
    artist_two = read_json(f'MusicData/resources/{chosen_artists_name[1]}_{chosen_artists_id[1]}.json')

    return artist_one, artist_two


def parse_json():
    pass


#def main():
#    chosen_artists_name, chosen_artists_id = choose_artists()
#    from spotify_api_miner import main as miner_main
#    miner_main()

#if __name__ == "__main__":
#    main()