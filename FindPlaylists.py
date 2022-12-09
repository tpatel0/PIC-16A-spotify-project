import pandas as pd
        
    
class FindPlaylists():
'''
Class that finds playlists from the Million Playlists Spotify dataset that contains user input(s)
'''
    def __init__(self, data):
    '''
    Prompts user to input varaiables used in the rest of the function. Asks user for input for an artist, a song, and album of theirs. 
    At least one input is required.
    Args:
        data: instance of Million Playlist dataset as a csv file
    Returns:
        none
    '''        
        self.data = data
        
        # ask user for inputs that will be used in other functions
        print("Type in the information below, and hit enter. You can leave blank if you need to.")
        self.artist = input("Artist Name : ")
        self.track = input("Track Name : ")
        self.album = input("Album Name : ")
        
        if self.artist =='' and self.track =='' and self.album =='':
                raise ValueError("No input entered.")
        
        # variables that will be used in iteration and displaying results
        self.high_score = -1 
        self.playlist_index = -1
        
        
    def query(self):
    '''
    Create a list of nonempty input variables.
    Args:
        none
    Returns:
        querylist: a list of filled user inputs
    '''
        inputs = [self.artist, self.track, self.album]
        
        querylist = []
        querylist.append(inputs[i]) for i in range(len(inputs)) if inputs[i] != ''
        
        return querylist
        

    def __str__(self):
    '''
    Print condition of findRec function based on user input.
    Args:
        none
    Returns:
        mystring: string dependent on user input. "Finding playlists that contains {condition depending on user input}"
    '''
        q = self.querylist()
        s = ', '
        s = s.join(q)
        
        mystring = "Finding playlists that contain music from " + s
        
        return mystring
                
        
    def findRecs(self):
    '''
    Iterates through a random slice in the Million Playlists dataset and gives a score to each playlist based on how many 
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
            if(average_score > high_score):
                self.high_score = average_score
                self.playlist_index = i
                
        return self.high_score, self.playlist_index
                
    def showResults(self):
    ''' 
    Display results of playlists with most occurences of user inputs
    Args:
        none
    Returns:
        none 
    '''
        playlist_name = df.loc[self.playlist_index]['name']
            
        # Recommend and print the output
        if(maximum > 0):
            print("😃😃 You should listen to the playlist called "+str(playlist_name)+".")
            print("♫ 🎸It has the closest match to "+str(self.query())+" with a score of "+str(self.high_score)+".")
            results = pd.DataFrame(all_tracks[self.playlist_index])
            display(results[['artist_name', 'track_name','album_name']])
        else:
            print("😭😭😭 Sorry, no recommendation found.")
