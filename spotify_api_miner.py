import requests, json, os


# The list of all artists and theirs ids that user can choose between.
artists = []
ids = []


# A function for reading json files and be reused many times.
def read_json(data):
    with open(f'{data}', "r") as file:
        content = json.load(file)
    return content

content = read_json('MusicData/resources/artists_list.json')


def create_list_of_artists(content):
    for artist_name, artist_id in content.items():
        artists.append(artist_name.casefold())
        ids.append(artist_id)

    return artists, ids


''' Using zip to creating a list of tuples from my lists artists and ids to 
    make sure that thise informations never change in the program. '''
def display_main_list(artists, ids):    
    for artist, id in zip(artists, ids):
        print(f"Artist: {artist}\n    ID: {id}\n")


# User chooses his 2 favorites artists ofr getting analysis about
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


def user_interaction():
    type_of_json_list = ['artists', 'albums', 'top-tracks']
    invalid_input = False

    try:
        while not invalid_input:
            type_of_json = input("Choose one of the options: Artists -- Albums -- Top-Tracks: ").lower()
            
            if type_of_json in type_of_json_list:
                if type_of_json == "artists":
                    type_of_json = ""

                invalid_input = True
                return type_of_json
            else:
                print("Invalid input! Please choose from Artists, Albums, or Top-Tracks.")

    except Exception as e:
            print(f"Something went wrong! {e}")


def spotify_api(chosen_artists_id, type_of_json):
    data_list = []
    for i in range(len(chosen_artists_id)):
        api_token = "https://dit009-spotify-assignment.vercel.app/api/v1/"
        url = f"{api_token}artists/{chosen_artists_id[i]}/{type_of_json}"
        response = requests.get(url)
        data = response.json()
        data_list.append(data)

    return data_list


def choose_song():
    try:
        invalid_input = False
        while not invalid_input:
            artist = input("Choose your favorite artist from: ")
            title = input(f"Enter a song from {artist}: ")
            invalid_input = True

    except Exception as e:
        print(f"Something went wrong: {e}")
    
    return artist, title


def lyrics_api(artist, title):

    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)
    data = response.json()

    return data, artist, title    

'''
def find_synonyms():
    try:
        invalid_input = False
        while not invalid_input:
            word = input("Enter the word you'd like to find its synonyms: ")
            invalid_input = True

    except Exception as e:
        print(f"Something went wrong: {e}")
    
    return word
'''

def dictionary_api(random_word):
    
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{random_word}"
    response = requests.get(url)
    data = response.json()

    return data, random_word


def wikipedia_api():
    pass

def save_json_spotify(data_list, path, chosen_artists_name, chosen_artists_id):
    for i in range(len(chosen_artists_id)):
        with open(f'MusicData/resources/{path}/{chosen_artists_name[i]}_{chosen_artists_id[i]}.json', "w") as file:
            json.dump(data_list[i], file, indent=4)


def save_json_lyrics(data, artist, title):
    with open(f'MusicData/resources/lyrics/{artist}_{title}.json', "w") as file:
            json.dump(data, file, indent=4)


def save_json_dictionary(data, random_word):
    with open(f'MusicData/resources/dictionary/{random_word}_defination.json', "w") as file:
            json.dump(data, file, indent=4)


def remove_json(data_list, path, chosen_artists_name, chosen_artists_id):
    for i in range(len(chosen_artists_id)):
        os.remove(f'MusicData/resources/{path}/{chosen_artists_name[i]}_{chosen_artists_id[i]}.json')


def file_path(type_of_json):
    if type_of_json == "":
        path = "artists"
    elif type_of_json == "top-tracks":
        path = "tracks"
    elif type_of_json == "albums":
        path = "albums"

    return path


def main():
    artists, ids = create_list_of_artists(content)
    display_main_list(artists, ids)

    chosen_artists_name, chosen_artists_id = choose_artists()
    type_of_json = user_interaction()
    path = file_path(type_of_json)
    data = spotify_api(chosen_artists_id, type_of_json)
    save_json_spotify(data, path, chosen_artists_name, chosen_artists_id)

    artist, title = choose_song()
    find_lyrics = lyrics_api(artist, title)
    save_json_lyrics(find_lyrics, artist, title)

    #word = find_synonyms()
    data, random_word = dictionary_api(random_word)
    save_json_dictionary(data, random_word)

    #remove_json(data, chosen_artists_name, chosen_artists_id)


if __name__ == "__main__":
     main()