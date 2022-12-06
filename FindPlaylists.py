import random # idk if it's needed but just in case
import pandas as pd
        
    
class FindPlaylists(Playlists):
'''
Class that finds playlists from the Million Playlists Spotify dataset that contains user input(s)
'''
    def __init__(self):
    '''
    Prompts user to input varaiables used in the rest of the function. Asks user for input for a song and the optional artist and album of theirs.
    Arg:
        none
    Returns:
        none
    '''        
        print("Type in the information below, and hit enter. You can leave blank if you need to.")
        self.artist = input("Track Name : ")
        self.track = input("Artist Name : ")
        self.album = input("Album Name : ")
        
        # variables that will be used in iteration and displaying results
        self.maximum = -1 # the highest score
        self.playlist_index = -1

    def __str__(self):
    '''
    Args:
        none
    Returns:
        mystring: string dependent on user input. "Finding playlists that contains {condition depending on user input}"
    '''
        if self.artist == "" and self.track == "" and self.album == "":
            raise ValueError("No input found.")
        elif self.track == "" and self.album == "":
            mystring = "Finding playlists that contains songs by " + self.artist "."
        elif self.album == "":
            mystring = "Finding playlist that contains " + self.track + " by " + self.artist + "."
        else
            mystring = "Finding playlists that contains " + self.track + " by " + self.artist + " from the album " + self.album "."
        
        return mystring
                
        
    def findRecs(self):
    '''
    Iterates through a random slice in Million Playlists dataset and gives a score to each playlist based on how many 
    times an artist, track, and/or album is present in a playlist.
    
    Args:
        self: the variables initialized in the __init__ function
    Returns:
        
    
    '''
        # Main Code for recommendation
        # Select the tracks column in our data for all playlists
        all_tracks = df['tracks']
        
        
        tracks = range(len(all_tracks))
        for i in tracks:
            # Choose current track
            current_track = pd.DataFrame(all_tracks[i]) 
            
            # Calculate number of matches for artist, tracks and albums for a score
            # And divides by the number of tracks to normalize for fair comparison
            artist_score = 0.0
            track_score = 0.0
            album_score = 0.0
            
            if(self.artist != ""):
                artist_score = current_track['artist_name'].str.contains(artist_name).sum()/len(current_track)
            if(self.track != ""):
                track_score = current_track['track_name'].str.contains(track_name).sum()/len(current_track)
            if(self.album != ""):
                album_score = current_track['album_name'].str.contains(album_name).sum()/len(current_track)
            
            # Use the average score as a metric 
            average_score = ((artist_score + track_score + album_score)/3)*100
            
            # create new score
            if(average_score > maximum):
                self.maximum = average_score
                self.playlist_index = i
                
        return artist_score, track_score, album_score
                
    def showResults(self):
    ''' 
    Display results of playlists with most occurences of user inputs
    Args:
        none
    Returns:
        none 
    '''
        # And finally recommend the playlist from that json
        playlist_name = df.loc[playlist_index]['name']
        query_string = []
        if(artist_name != ""):
            query_string.append(artist_name)
        if(track_name != ""):
            query_string.append(track_name)
        if(album_name != ""):
            query_string.append(album_name)
            
        # Recommend and print the output
        if(maximum > 0):
            print("😃😃 You should listen to the playlist called "+str(playlist_name)+".")
            print("♫ 🎸It has the closest match to "+str(query_string)+" with a score of "+str(maximum)+".")
            results = pd.DataFrame(all_tracks[playlist_index])
            display(results[['artist_name', 'track_name','album_name']])
        else:
            print("😭😭😭 Sorry, no recommendation found.")