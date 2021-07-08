import json 

def main():
    with open('./songLibrary.json','r') as library:
        songData = json.load(library)
        for index, song in enumerate(songData):
            path = f"./songs/song_{index}.json"
            song_loc = open(path,'w')
            json.dump(song,song_loc)
            song_loc.close()

    library.close()

main()
