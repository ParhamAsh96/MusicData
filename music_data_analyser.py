import json, pandas, matplotlib


# A function for reading json files and be reused many times.
def read_json(data):
    with open(f'{data}', "r") as file:
        content = json.load(file)
    return content


# The list of all artists and theirs ids that user can choose between.
artists = []
ids = []

def create_list_of_artists(content):
    for artist_name, artist_id in content.items():
        artists.append(artist_name.casefold())
        ids.append(artist_id)

    return artists, ids

content = read_json('MusicData/resources/artists_list.json')
artists, ids = create_list_of_artists(content)

# Using zip to creating a list of tuples from my lists artists and ids to 
# make sure that thise informations never change in the program.     
for artist, id in zip(artists, ids):
    print(f"Artist: {artist}\n    ID: {id}\n")


# OBS !!! I think i have to move it to miner.py and then import it here so that everything runs from analyser !!!!!
# User choose his 2 favorites artists ofr getting analysis about
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

chosen_artists_name, chosen_artists_id =choose_artists()

def read_chosen_json():
    artist_one = read_json(f'MusicData/resources/{chosen_artists_name[0]}_{chosen_artists_id[0]}.json')
    artist_two = read_json(f'MusicData/resources/{chosen_artists_name[1]}_{chosen_artists_id[1]}.json')

    return artist_one, artist_two


# Counts amount of the albums !!!
def parse_albums():
    artist_one, artist_two = read_chosen_json()
    
    # Analys number of albums from artist 1
    total_albums_artist_one = []
    total_singles_artist_one = []
    for album in artist_one['items']:
        if album['album_type'] == 'album':
            total_albums_artist_one.append(album['album_type'])
        elif album['album_type'] == 'single':
            total_singles_artist_one.append(album['album_type'])

    print(f"\n{chosen_artists_name[0].capitalize()} has total {len(total_albums_artist_one)} albums and {len(total_singles_artist_one)} singles.")

    # Analys number of albums from artist 2
    total_albums_artist_two = []
    total_singles_artist_two = []
    for album in artist_two['items']:
        if album['album_type'] == 'album':
            total_albums_artist_two.append(album['album_type'])
        elif album['album_type'] == 'single':
            total_singles_artist_two.append(album['album_type'])

    print(f"\n{chosen_artists_name[1].capitalize()} has total {len(total_albums_artist_two)} albums and {len(total_singles_artist_two)} singles.")

# Things i want user to choose:
# JSON --> items --> [0] --> {total_tracks:x}
#    print(artist_one['items'][0]['total_tracks'])
def parse_tracks():
    artist_one, artist_two = read_chosen_json()

    total_tracks_artist_one = []
    for track in artist_one['items']:
        total_tracks_artist_one.append(track['total_tracks'])
        #print(track['total_tracks'])
    for i in range(len(total_tracks_artist_one)):
        total_tracks_artist_one[i] = int(total_tracks_artist_one[i])
        
    print(f"\n{chosen_artists_name[0].capitalize()} has total {sum(total_tracks_artist_one)} tracks.")

    total_tracks_artist_two = []
    for track in artist_two['items']:
        total_tracks_artist_two.append(track['total_tracks'])
        #print(track['total_tracks'])
    for i in range(len(total_tracks_artist_two)):
        total_tracks_artist_two[i] = int(total_tracks_artist_two[i])
        
    print(f"\n{chosen_artists_name[1].capitalize()} has total {sum(total_tracks_artist_two)} tracks.")


#parse_albums()
#parse_tracks()

#def main():
#    chosen_artists_name, chosen_artists_id = choose_artists()
#    from spotify_api_miner import main as miner_main
#    miner_main()

#if __name__ == "__main__":
#    main()