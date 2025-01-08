import json, matplotlib
import pandas as pd
from tabulate import tabulate
from spotify_api_miner import file_path
# from spotify_api_miner import read_json

# By importing read_json, the program will send request and get the api live and save it as json in resources;
# So i made it offline for the assignment to make sure that the user can get outputs faster.
# content = read_json('MusicData/resources/artists_list.json')


# A function for reading json files and be reusing.
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


# Complete this section later !!!!!!!!!!!!!!!
def main_menu(): # Add 'option' as a parameter at the end
    option = main_menu_options()
    match option:
        case 1:
            chosen_artists_name, chosen_artists_id = choose_two_artists()
            submenu_option = submenu_option_one()
            match submenu_option:
                case 1:
                    compare_artists(chosen_artists_name, chosen_artists_id)
                case 2:
                    wikipedia_stats(chosen_artists_name, chosen_artists_id)
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
                    analyze_lyrics_emotion()
                case 2:
                    return
                case 3:
                    print("You exited the program. Goodbye!")
                case _:
                    print("Invalid option! Please try again!")
        case 3:
            submenu_option = submenu_option_three()
            match submenu_option:
                case 1:
                    get_song_recommendations()
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


# Complete this section later !!!!!!!!!!!!!!!
def main_menu_options():
    print("\n1: Choose two artists from our list.")
    print("2: Choose a song from our list.")
    print("3: Get personalized recommendations based on your favorite song.")
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
    print("2: Display Wikipedia Stats: ")
    print("3: Go Back")
    print("4: Exit the program.")

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
    print("\n1: Analyze Lyrics Emotion: ")
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


def submenu_option_three():
    print("\n1: Get Recommendations: ")
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


def compare_artists(chosen_artists_name, chosen_artists_id):
    total_albums_artist_one, total_singles_artist_one, total_albums_artist_two, total_singles_artist_two = parse_albums(chosen_artists_name, chosen_artists_id)
    total_tracks_artist_one, total_tracks_artist_two = parse_tracks(chosen_artists_name, chosen_artists_id)

    data = {
        "Data": ["Albums", "Singles", "Tracks"],
        chosen_artists_name[0] : [total_albums_artist_one, total_singles_artist_one, total_tracks_artist_one],
        chosen_artists_name[1] : [total_albums_artist_two, total_singles_artist_two, total_tracks_artist_two]
    }

    data_table = pd.DataFrame(data)
    print(tabulate(data, headers="keys", tablefmt="fancy_grid"))


def wikipedia_stats():
    pass


def analyze_lyrics_emotion():
    pass


def get_song_recommendations():
    pass


def choose_two_artists():
    chosen_artists_name = []
    chosen_artists_id = []
    index = 0
    try:
        while index < 2:
            artist = input("Choose an artists from our list: ").title()

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



if __name__ == "__main__":
    main_menu()