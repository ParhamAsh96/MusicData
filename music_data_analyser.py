import json, re, random
import pandas as pd
from spotify_api_miner import *
from tabulate import tabulate
from matplotlib import pyplot as plt

'''
    NOTES: 
    Spotify api is a bit slow and i decided to make it offline by saving a prepared list of some artists.
    They data are saved as JSON in differents folders based on the data. Lyrics api is also offline and i already 
    saved some lyrics from different artists.

    Other apis that i used (Wikipedia api and Dictionary api) are online and the data saves in a JSON files during runtime.
'''

def read_json(data):
    with open(f'{data}', "r") as file:
        database = json.load(file)
    return database

database = read_json('MusicData/resources/artists_list.json')

print("\nList of the artists:")
index = 1
for artist in database.keys():
    print(f"{index}: {artist}")
    index += 1


def main_menu():
    option = main_menu_options()
    match option:
        case 1:
            chosen_artists_name, chosen_artists_id = choose_two_artists()
            submenu_option = submenu_option_one()
            match submenu_option:
                case 1:
                    compare_artists(chosen_artists_name, chosen_artists_id)
                case 3:
                    return
                case 4:
                    print("You exited the program. Goodbye!")
                case _:
                    print("Invalid option! Please try again!")
        case 2:
            submenu_option = submenu_option_two()
            match submenu_option:
                case 1:
                    artist = find_artist_wiki()
                    data = wikipedia_api(artist)
                    save_json_wikipedia(data, artist)
                    wikipedia_stats(data, artist)
                case 2:
                    return
                case 3:
                    print("You exited the program. Goodbye!")
                case _:
                    print("Invalid option! Please try again!")
        case 3:
            artist, song = choose_lyrics()
            random_word = find_random_word(artist, song)
            data, random_word = dictionary_api(random_word)
            save_json_dictionary(data, random_word)
            submenu_option = submenu_option_three()
            match submenu_option:
                case 1:
                    play_game(random_word)
                case 2:
                    return
                case 3:
                    print("You exited the program. Goodbye!")
                case _:
                    print("Invalid option! Please try again!")
        case 4:
            print("You exited the program. Goodbye!")
        case _:
            print("Invalid option! Please try again!")


def main_menu_options():
    print("\n1: Which artist is more populuar? (Choose two from our list above) ")
    print("2: How many times was the artist searched this year? (By month) ")
    print("3: Wanna learn english in a fun way? ")
    print("4: Exit the program.")

    invalid_input = False
    while not invalid_input:
        try:
            option = int(input("\nChoose one of the following options from the Main Menu (1-4): "))

            if 0 < option < 5:
                invalid_input = True
                return option
            else:
                print("The number shall be between 1 to 4.")

        except ValueError:
            print("Invalid input! Enter only numbers!")
        
        except Exception as e:
            print(f"Something went wrong: {e}")


def submenu_option_one():    
    print("\n1: Compare the Artists: ")
    print("2: Go Back")
    print("3: Exit the program.")

    invalid_input = False
    while not invalid_input:
        try:
            submenu_option = int(input("\nChoose one of the following options from the Menu (1-4): "))

            if 0 < submenu_option < 5:
                invalid_input = True
                return submenu_option
            else:
                print("The number shall be between 1 to 4.")

        except ValueError:
            print("Invalid input! Enter only numbers!")
        
        except Exception as e:
            print(f"Something went wrong: {e}")


def submenu_option_two():
    print("\n1: Choose your favorit artist: ")
    print("3: Go Back")
    print("4: Exit the program.")

    invalid_input = False
    while not invalid_input:
        try:
            submenu_option = int(input("\nChoose one of the following options from the Menu (1-3): "))

            if 0 < submenu_option < 5:
                invalid_input = True
                return submenu_option
            else:
                print("The number shall be between 1 to 3.")

        except ValueError:
            print("Invalid input! Enter only numbers!")
        
        except Exception as e:
            print(f"Something went wrong: {e}")


def submenu_option_three():
    print("\n1: Play the game: ")
    print("2: Go Back")
    print("3: Exit the program.")

    invalid_input = False
    while not invalid_input:
        try:
            submenu_option = int(input("\nChoose one of the following options from the Menu (1-3): "))

            if 0 < submenu_option < 5:
                invalid_input = True
                return submenu_option
            else:
                print("The number shall be between 1 to 3.")

        except ValueError:
            print("Invalid input! Enter only numbers!")
        
        except Exception as e:
            print(f"Something went wrong: {e}")



def compare_artists(chosen_artists_name, chosen_artists_id):
    total_albums_artist_one, total_singles_artist_one, total_albums_artist_two, total_singles_artist_two = parse_albums(chosen_artists_name, chosen_artists_id)
    total_tracks_artist_one, total_tracks_artist_two = parse_tracks(chosen_artists_name, chosen_artists_id)
    total_followers_artist_one, total_followers_artist_two = parse_followers(chosen_artists_name, chosen_artists_id)
    result_top_tracks_one, result_top_tracks_two = parse_top_tracks(chosen_artists_name, chosen_artists_id)

    data = {
        "Name": ["Albums", "Singles", "Tracks", "Followers", "Top Tracks"],
        chosen_artists_name[0] : [total_albums_artist_one, total_singles_artist_one, total_tracks_artist_one, total_followers_artist_one, result_top_tracks_one],
        chosen_artists_name[1] : [total_albums_artist_two, total_singles_artist_two, total_tracks_artist_two, total_followers_artist_two, result_top_tracks_two]
    }

    data_table = pd.DataFrame(data)
    print(tabulate(data, headers="keys", tablefmt="fancy_grid"))


def wikipedia_stats(data, artist):
    data = read_json(f'MusicData/resources/wikipedia/{artist}_wiki.json')

    views = []
    for view in data['items']:
        views.append(view['views'])

    total_views = 0
    for view in views:
        total_views += view

    plt.title(f"Chart of {artist}'s monthly views on Wikipedia")
    plt.plot(views)
    plt.show()


def choose_lyrics():
    song_list = read_json('MusicData/resources/songs_list.json')

    print("Choose an artist and one of the its song from the list.\n")

    for key, value in song_list.items():
        print(f"{key}: ", end="")
        
        for i, item in enumerate(value):
            if i == len(value) - 1:
                print(item, end="")
            else:
                print(item, end=", ")
        print("")
        
    try:
        invalid_input = False
        while not invalid_input:
            artist = input("\nEnter the name of the artist from our list above: ").title()
            if artist not in song_list:
                print(f"{artist} is not in our list. Please try again!")
            else:
                print(f"{artist} is chosen.")
                invalid_input = True

        invalid_input = False
        while not invalid_input:
            song = input("\nEnter the song from our list above: ").title()
            if song not in song_list[artist]:
                print(f"{song} is not in our list. Please try again!")
            else:
                print(f"{song} is chosen.")
                invalid_input = True

        return artist, song

    except Exception as e:
        print(f"Something went wrong: {e}")


def find_random_word(artist, song):
    lyrics_file = read_json(f'MusicData/resources/lyrics/{artist}_{song}.json')
    lyrics = (lyrics_file[0].get('lyrics', 'Key not found'))
    random_word = random.choice(re.findall(r'\b\w+\b', lyrics))

    return random_word


def play_game(random_word):
    database = read_json(f'MusicData/resources/dictionary/{random_word}_defination.json')

    for word in database:
        defination = {}
        defination = word['meanings'][0]['definitions'][0]['definition']
        
        print(f"Today's word is {random_word}\n")
        print(f"Defination of {random_word} is: {defination}\n")


def choose_two_artists():
    chosen_artists_name = []
    chosen_artists_id = []
    index = 0
    try:
        while index < 2:
            artist = input("Which artist is more populuar (Choose two)? ").title()

            if artist.title() in database.keys():
                
                if artist.title() in chosen_artists_name:
                    print(f"{artist} is already chosen!")
                
                else:
                    chosen_artists_name.append(artist)
                    chosen_artists_id.append(database[artist.title()])
                    index += 1
                    print(f"{artist} added for comparing.")
            
            else:
                print(f"{artist} is not in our list.")
        
        return chosen_artists_name, chosen_artists_id
    
    except Exception as e:
        print(f"Something went wrong: {e}")


def read_chosen_json(json_path, chosen_artists_name, chosen_artists_id):
    artist_one = read_json(f'MusicData/resources/{json_path}/{chosen_artists_name[0]}_{chosen_artists_id[0]}.json')
    artist_two = read_json(f'MusicData/resources/{json_path}/{chosen_artists_name[1]}_{chosen_artists_id[1]}.json')

    return artist_one, artist_two


def parse_albums(chosen_artists_name, chosen_artists_id):
    artist_one, artist_two = read_chosen_json('albums', chosen_artists_name, chosen_artists_id)
    
    # Analys number of albums and singles from artist 1
    total_albums_artist_one = []
    total_singles_artist_one = []
    for album in artist_one['items']:
        if album['album_type'] == 'album':
            total_albums_artist_one.append(album['album_type'])
        elif album['album_type'] == 'single':
            total_singles_artist_one.append(album['album_type'])

    # Analys number of albums and singles from artist 2
    total_albums_artist_two = []
    total_singles_artist_two = []
    for album in artist_two['items']:
        if album['album_type'] == 'album':
            total_albums_artist_two.append(album['album_type'])
        elif album['album_type'] == 'single':
            total_singles_artist_two.append(album['album_type'])

    return len(total_albums_artist_one), len(total_singles_artist_one), len(total_albums_artist_two), len(total_singles_artist_two)



def parse_tracks(chosen_artists_name, chosen_artists_id):
    artist_one, artist_two = read_chosen_json('albums', chosen_artists_name, chosen_artists_id)
    
    # Analys and calculate total number of tracks from artist 1
    total_tracks_artist_one = []

    for track in artist_one['items']:
        total_tracks_artist_one.append(track['total_tracks'])

    for i in range(len(total_tracks_artist_one)):
        total_tracks_artist_one[i] = int(total_tracks_artist_one[i])
    
    # Analys and calculate total number of tracks from artist 1
    total_tracks_artist_two = []

    for track in artist_two['items']:
        total_tracks_artist_two.append(track['total_tracks'])

    for i in range(len(total_tracks_artist_two)):
        total_tracks_artist_two[i] = int(total_tracks_artist_two[i])
        
    return sum(total_tracks_artist_one), sum(total_tracks_artist_two)



def parse_followers(chosen_artists_name, chosen_artists_id):
    artist_one, artist_two = read_chosen_json('artists', chosen_artists_name, chosen_artists_id)

    # Analys and find out total number of followers for artist 1
    total_followers_artist_one = artist_one["followers"]["total"]
        
    # Analys and find out total number of followers for artist 1
    total_followers_artist_two = artist_two["followers"]["total"]

    return total_followers_artist_one, total_followers_artist_two



def parse_top_tracks(chosen_artists_name, chosen_artists_id):
    artist_one, artist_two = read_chosen_json('tracks', chosen_artists_name, chosen_artists_id)

    # Analys and find out top tracks of artist 1 in spotify
    top_tracks_artist_one = []
    for track in artist_one['tracks']:
        top_tracks_artist_one.append(track['name'])
    
    result_top_tracks_one = ""   
    for top_track_one in top_tracks_artist_one:
        result_top_tracks_one += f"{top_track_one}\n"
        
    # Analys and find out top tracks of artist 2 in spotify    
    top_tracks_artist_two = []
    for track in artist_two['tracks']:
        top_tracks_artist_two.append(track['name'])

    result_top_tracks_two = ""
    for top_track_two in top_tracks_artist_two:
        result_top_tracks_two += f"{top_track_two}\n"
    
    return result_top_tracks_one, result_top_tracks_two


if __name__ == "__main__":
    main_menu()