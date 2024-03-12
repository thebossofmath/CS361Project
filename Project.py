import os
import zmq
from spotify import Spotify
from track import Track
from playlist import Playlist
import requests
import random
songs = {1: "1BxfuPKGuaTgP7aM0Bbdwr",
         2: "1qrpoAMXodY6895hGKoUpA",
         3: "1Iq8oo9XkmmvCQiGOfORiz",
         4: "0V3wPSX9ygBnCm8psDIegu",
         5: "5jQI2r1RdgtuT8S3iG8zFC",
         6: "1dGr1c8CrMLDpV6mPbImSI",
         7: "1fzAuUVbzlhZ1lJAx9PtY6",
         8: "79uDOz0zuuWS7HWxzMmTa2",
         9: "1HCdems7PQZRj42QDWLA0A",
         10: "3MytWN8L7shNYzGl4tAKRp"}
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")

artist_id = b'06HL4z0CvFAxyc27GXpf02'

auth_code = "AQAKmKPIaOoOVh4dlnBDUtNOPbujfdFOxIIo2nJ_1FNaYWGqvFO6DOP6yl2fsTJQ6P7jFJOLgILApAlTsML_x89dYd1dAjmnaQpzFE5hkQzIjpv5lIQztSXJUNhnuakrvSY81Yr1Bqo5jMTTg6Jd88OnGVhcSRjC6bx_XQo6_ImLIfzWpO0nS7ZjqaGz6HJKBw"
auth_token = "BQBWbAN5Jnw4CxnlVQJFJ7s7gCs2jEvTI8JNznPrR1eBjwyCVpJtRL64BWGzKJX3qtmKXdO4p0Q6h4AnivUtNeFZ5es6ckdxTdZWwGVueuE-TaI3T8Esx3bDdXKx2Vgzpz44FLHXYOFyKbDq9v4v0KZhOFnPyGab9Vj5Wn4eRwThyE_zCEoXQxP5j7ZdjoBjtOvboyaArvJyb1hJhYb4zIpqF4Y"
refresh_token = "AQA9iIWIH0GNR5aeQXx9wbsViGwu-wuui1jq2jaa5KfMZcO52mfEUBcZnGIq5YOfpi1YbaGWbSD13r5bxjBEWJ0h5La3g9RwOfjHpwPtF8oBGWnalE_IOnQIeXilStJkMcQ"
url = "https://accounts.spotify.com/api/token"
user_id = "1287914872"
payload = 'grant_type=client_credentials&client_id=1a4e42c6ace341bbb9ac7fd7ce9c291d&client_secret=ae86699e4eba44e1b377406a9c1ab6e5'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}
client = Spotify(auth_token, user_id)
def main():
    print("Welcome to the Taylor Swift Application")
    print("Dive into Taylor Swift's music, achievements, and life!")
    input("Press ENTER to begin...")
    quit = False
    while not quit:
        displayMenu()
        choice = getChoice()
        if choice == "7":
            quit = True
            continue
        if len(choice) == 2:
            displayHelpText(int(choice[0]))
            continue
        executeChoice(int(choice))
    print("I Hope you enjoyed your time with the Ultimate Taylor Swift App")


def displayMenu():
    os.system('cls')
    print("THE ERAS APP MAIN MENU")
    print("1. TOP HITS - Billboard Chart Toppers")
    print("2. RANDOM PLAYLIST GENERATOR - Choose Your Length")
    print("3. VIEW ALBUMS - Explore the Discography")
    print("4. VIEW LYRICS - Name a Song, See the Lyrics")
    print("5. NEXT RELEASE - Latest News on Upcoming Albums and Singles")
    print("6. DATING LIFE - Keep Up with the Hot Gossip")
    print("7. QUIT")
    return

def getChoice():
    done = False
    while not done:
        print()
        print("[Enter #? for help text for any option]")
        choice = input("Selection: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7":
            done = True
            continue
        if choice == "1?" or choice == "2?" or choice == "3?" or choice == "4?" or choice == "5?" or choice == "6?" or choice == "7?":
            done = True
            continue
        os.system('cls')
        print("Your input is invalid. Please try again.")
        input("Press ENTER to return to the menu")
        displayMenu()
    return choice

def displayHelpText(choice):
    os.system('cls')
    if choice == 1:
        print("See Taylor's best charting singles on the Billboard Charts!")
        print("Results sorted by peak charting position then by time on the chart.")
        input("Press ENTER to return to the menu")
    if choice == 2:
        print("The application will generate a Spotify Playlist of random Taylor Swift")
        print("songs for you to enjoy. Just provide the playlist length (in songs) that you want!")
        input("Press ENTER to return to the menu")
    if choice == 3:
        print("See all of Taylor Swift's Albums. You can then drill down into a specific album")
        print("and see the track listing for each of the songs. You can further drill down to")
        print("view the lyrics for a specific song.")
        input("Press ENTER to return to the menu")
    if choice == 4:
        print("Given the name of a song, the program will return the lyrics of the song")
        print("All results will be the clean version.")
        input("Press ENTER to return to the menu")
    if choice == 5:
        print("Waiting for more Taylor Swift? Choose this option to see all confirmed details")
        print("about any upcoming projects Taylor has in the works.")
        input("Press ENTER to return to the menu")
    if choice == 6:
        print("See the current relationship status of Taylor Swift as well as details")
        print("of the current (if extant) relationship.")
        input("Press ENTER to return to the menu")
    if choice == 7:
        print("Quit out of the app. It's ok. You can leave. I'll shake it off")
        input("Press ENTER to return to the menu")

def executeChoice(choice):
    os.system('cls')
    if choice == 1 or choice == 4 or choice == 5 or choice == 6:
        print("I apologize but this functionality has not been implemented yet")
        input("Press ENTER to return to the menu")
    if choice == 2:
        executePlaylistGenerator()
    if choice == 3:
        executeDisplayAlbums()


def executePlaylistGenerator():
    valid = False
    print("PLAYLIST GENERATOR")
    print()
    print("Playlist generation will take more time for longer playlists")
    while not valid:
        print("[Enter 'OPT' to return to Main Menu]")
        length = input("How many songs (1-30)?  ")
        if length == "OPT":
            return
        length = int(length)
        if 30 >= length >= 1:
            valid = True
            continue
        os.system('cls')
        print("Please enter a number between 1 and 10 for length")
    confirm = input("Are you sure? [Enter YES] to confirm: ")
    if confirm.upper() != "YES":
        return
    track_ids = []
    tracks =[]
    for i in range(length):
        new_track = False
        print(f"Requesting song #{i + 1}...")
        while not new_track:
            socket.send(artist_id)
            track_id = socket.recv()
            track_id = track_id.decode("utf-8")
            if track_id not in track_ids:
                track_ids.append(track_id)
                tracks.append(Track("",track_id,""))
                print(f"Adding Track ID: {track_id} to the playlist")
                new_track = True
    playlist = client.create_playlist()
    print(f"Playlist '{playlist.name}' was created with id = {playlist.id}")
    client.populate_playlist(playlist, tracks)
    # print(f"Playlist was successfully populated")
    print(f"Access your playlist at https://open.spotify.com/playlist/{playlist.id}")
    input("Press ENTER to return to the Main Menu")









def executeDisplayAlbums():
    done = False
    while not done:
        displayAlbums()
        album = getAlbumChoice()
        if album == "OPT":
            done = True
            continue
        displaySingleAlbum(album)

def displayAlbums():
    os.system('cls')
    print("Taylor's Albums")
    print()
    print("1. Taylor Swift          2. Fearless")
    print("3. Speak Now             4. Red")
    print("5. 1989                  6. Reputation")
    print("7. Lover                 8. folklore")
    print("9. evermore              10. Midnights")

def displaySingleAlbum(album):
    os.system('cls')
    if album == 1:
        print("Taylor Swift (2006)")
        print("1. Tim McGraw                    2. Picture To Burn")
        print("3. Teardrops On My Guitar        4. A Place In This World")
        print("5. Cold As You                   6. The Outside")
        print("7. Tied Together With A Smile    8. Stay Beautiful")
        print("9. Should've Said No             10. Mary's Song (Oh My My My)")
        print("11. Our Song")
    if album == 2:
        print("Fearless (2008) and (2021)")
        print("1. Fearless                      2. Fifteen")
        print("3. Love Story                    4. Hey Stephen")
        print("5. White Horse                   6. You Belong With Me")
        print("7. Breathe                       8. Tell Me Why")
        print("9. The Way I Loved You           10. Forever & Always")
        print("11. The Best Day                 12. The Best Day")
        print("13. Change                       14. Jump Then Fall")
        print("15. Untouchable                  16. Forever & Always (Piano Version)")
        print("17. Come In With The Rain        18. Superstar")
        print("19. The Other Side Of The Door   20. Today Was a Fairytale")
        print("21. You All Over Me              22. Mr. Perfectly Fine")
        print("23. We Were Happy                24. That's When")
        print("25. Don't You                    26. Bye Bye Baby")
    if album == 3:
        print("Speak Now (2010) and (2023)")
        print("1. Mine                          2. Sparks Fly")
        print("3. Back To December              4. Speak Now")
        print("5. Dear John                     6. Mean")
        print("7. The Story Of Us               8. Never Grow Up")
        print("9. Enchanted                     10. Better Than Revenge")
        print("11. Innocent                     12. Haunted")
        print("13. Last Kiss                    14. Long Live")
        print("15. Ours                         16. Superman")
        print("17. Electric Touch               18. When Emma Falls In Love")
        print("19. I Can See You                20. Castles Crumbling")
        print("21. Foolish One                  22. Timeless")
    if album == 4:
        print("Red (2012) and (2021)")
        print("1. State Of Grace                2. Red")
        print("3. Treacherous                   4. I Knew You Were Trouble")
        print("5. All Too Well                  6. 22")
        print("7. I Almost Do                   8. We Are Never Ever Getting Back Together")
        print("9. Stay Stay Stay                10. The Last Time")
        print("11. Holy Ground                  12. Sad Beautiful Tragic")
        print("13. The Lucky One                14. Everything Has Changed")
        print("15. Starlight                    16. Begin Again")
        print("17. The Moment I Knew            18. Come Back... Be Here")
        print("19. Girl At Home                 20. State Of Grace (Acoustic Version)")
        print("21. Ronan                        22. Better Man")
        print("23. Nothing New                  24. Babe")
        print("25. Message In A Bottle          26. I Bet You Think About Me")
        print("27. Forever Winter               28. Run")
        print("29. The Very First Night         30. All Too Well (10 Minute Version)")
    if album == 5:
        print("1989 (2014) and (2023)")
        print("1. Welcome To New York           2. Blank Space")
        print("3. Style                         4. Out Of The Woods")
        print("5. All You Had To Do Was Stay    6. Shake It Off")
        print("7. I Wish You Would              8. Bad Blood")
        print("9. Wildest Dreams                10. How You Get The Girl")
        print("11. This Love                    12. I Know Places")
        print("13. Clean                        14. Wonderland")
        print("15. You Are In Love              16. New Romantics")
        print("17. 'Slut'                       18. Say Don't Go")
        print("19. Now That We Don't Talk       20. Suburban Legends")
        print("21. Is It Over Now?")
    if album == 6:
        print("Reputation (2017)")
        print("1. ...Ready for It?              2. End Game")
        print("3. I Did Something Bad           4. Don't Blame Me")
        print("5. Delicate                      6. Look What You Made Me Do")
        print("7. So It Goes...                 8. Gorgeous")
        print("9. Getaway Car                   10. King Of My Heart")
        print("11. Dancing With Our Hands Tied  12. Dress")
        print("13. This Is Why We Can't Have Nice Things")
        print("14. Call It What You Want        15. New Year's Day")
    if album == 7:
        print("Lover (2019)")
        print("1. I Forgot That You Existed     2. Cruel Summer")
        print("3. Lover                         4. The Man")
        print("5. The Archer                    6. I Think He Knows")
        print("7. Miss Americana & The Heartbreak Prince")
        print("8. Paper Rings                   9. Cornelia Street")
        print("10. Death by A Thousand Cuts     11. London Boy")
        print("12. Soon You'll Get Better       13. False God")
        print("14. You Need To Calm Down        15. Afterglow")
        print("16. ME!                          17. It's Nice To Have A Friend")
        print("18. Daylight")
    if album == 8:
        print("folklore (2020)")
        print("1. the 1                         2. cardigan")
        print("3. the last great american dynasty")
        print("4. exile                         5. my tears ricochet")
        print("6. mirrorball                    7. seven")
        print("8. august                        9. this is me trying")
        print("10. illicit affairs              11. invisible string")
        print("12. mad woman                    13. epiphany")
        print("14. betty                        15. peace")
        print("16. hoax                         17. the lakes")
    if album == 9:
        print("evermore (2020)")
        print("1. willow                        2. champagne problems")
        print("3. gold rush                     4. 'tis the damn season")
        print("5. tolerate it                   6. no body, no crime")
        print("7. happiness                     8. dorothea")
        print("9. coney island                  10. ivy")
        print("11. cowboy like me               12. long story short")
        print("13. marjorie                     14. closure")
        print("15. evermore                     16. right where you left me")
        print("17. it's time to go")
    if album == 10:
        print("Midnights (2022)")
        print("1. Lavender Haze                 2. Maroon")
        print("3. Anti-Hero                     4. Snow On The Beach")
        print("5. You're On Your Own, Kid       6. Midnight Rain")
        print("7. Question...?                  8. Vigilante Sh*t")
        print("9. Bejeweled                     10. Labyrinth")
        print("11. Karma                        12. Sweet Nothing")
        print("13. Mastermind                   14. The Great War")
        print("15. Bigger Than The Whole Sky    16. Paris")
        print("17. High Infidelity              18. Glitch")
        print("19. Would've, Could've, Should've")
        print("20. Dear Reader                  21. Hits Different")

    print()
    print("[Enter OPT to go back to all albums]")
    input("Explore Song: ")

def getAlbumChoice():
    done = False
    while not done:
        print()
        choice = input("Selection? [Enter 'OPT' to return to the Main Menu] ")
        if choice == "OPT":
            done = True
            continue
        choice = int(choice)
        if 1 <= choice <= 10:
            done = True
            continue
        os.system('cls')
        print("Invalid selection. Please try again")
        displayAlbums()
    return choice


if __name__=="__main__":
    main()