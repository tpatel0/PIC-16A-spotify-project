import pandas as pd
        
    
class FindPlaylists():
    '''
    Class that finds playlist from a slice of the Million Playlists dataset that contains user input(s)
    '''
    def __init__(self, data):
        '''
        Prompts user to input varaiables used in the rest of the function. Asks user for input for an artist, a song, and album of theirs. 
        At least one input is required.
        Args:
            data: an instance of Million Playlist dataset as a csv file
        Returns:
            none
        '''        
        self.data = data
        
        # ask user for inputs that will be used in other functions
        print("Type in an artist and/or song below, and hit enter. You can leave blank if you need to.")
        self.artist = input("Artist Name : ")
        self.track = input("Track Name : ")
        
        if self.artist =='' and self.track =='':
            raise ValueError("No input entered. Please fill out at least one field.")
        
        
    def query(self):
        '''
        Create a list of nonempty input variables.
        Args:
            none
        Returns:
            querylist: a list of filled user inputs
        '''
        # assign list objects regardless of user input 
        inputs = [self.artist, self.track]
        
        querylist = []
        
        for i in range(len(inputs)):
            if inputs[i] != '':
                querylist.append(inputs[i])
        
        return querylist
        

    def __str__(self):
        '''
        Print condition of findRec function based on user input.
        Args:
            none
        Returns:
            mystring: string dependent on user input. "Finding playlists that contain {condition depending on user input}"
        '''
        q = self.query()
        # s = ', '
        # s = s.join(q)
        
        mystring = "Finding playlists that contain " + str(q) + "."
        
        return mystring
                
        
    def findRecs(self):
        '''
        Iterates through a slice in the Million Playlists dataset and gives a score to each playlist based on how many 
        times an artist and/or track is present in a playlist.
        Args:
            self: the variables initialized in the __init__ function
        Returns:
            high_score: the highest occurence of artist and/or track
            plyalist_index: index of playlist ID that coincides with playlist with high score
        '''
        # all_tracks = self.data['track_name']
        
        # average scores to compare each playlist 
        high_score = -1 
        playlist_index = -1
        
        
        for pid, df_pid in self.data.groupby("pid"):
            
            artist_score = 0.0
            track_score = 0.0
            
            if(self.artist != ""): # if there was a user input for `self.artist`
                # find percentage of artist occurence in a particular playlist
                artist_score = df_pid['artist_name'].str.contains(self.artist).sum()/len(df_pid)
                
            if(self.track != ""):
                track_score = df_pid['track_name'].str.contains(self.track).sum()/len(df_pid)
                
            average_score = ((artist_score + track_score)/2)*100
            
            if(average_score > high_score):
                high_score = average_score
                playlist_index = pid
                
        return high_score, playlist_index

                
    def showResults(self):
        ''' 
        Display results of playlist with most occurences of user inputs. Display the first couple songs in this playlist
        Args:
            none
        Returns:
            self.data[songs_df].head(10): the first 10 songs in recommended playlist
        '''
        high_score = round(self.findRecs()[0], 2)
        playlist_index = self.findRecs()[1]
        # playlist_name = self.data.loc[playlist_index] there is no name in playlist available
            
        # Recommend and print the output
        if(high_score > 0):
            print("😃😃 You should listen to playlist with ID "+str(playlist_index)+".")
            print("♫🎸 It has the closest match to "+str(self.query())+" with a score of "+str(high_score)+".")
            print("🎶🎼 This playlist includes songs such as: ")
            
            songs_df = self.data['pid'] == playlist_index
            return self.data[songs_df].head(10)
        else:
            raise KeyError("😭😭😭 Sorry, no recommendation found.")
