import pandas as pd
import numpy as np
import json

def jsonToCSV():
    '''
        loads and opens the particular slice of the million dollar playlist to be used, and converts the json file to csv
       Args: no argument parameters, loads json file within the body of the function
       Returns: no return paramters, saves csv file within the body of the funciton.
    '''
    songPlaylistArray = [] #create empty array for the playlist
    d = json.load(open('mpd.slice.1000-1999.json')) #open json file

    #create data frame out of playlists feature of json file
    thisSlice = pd.DataFrame.from_dict(d['playlists'], orient='columns')
    #iterate through data frame
    for index, row in thisSlice.iterrows():
        for track in row['tracks']:
            #add the track parameter to the specific row of the data frame
            songPlaylistArray.append([track['track_uri'], track['artist_name'], track['track_name'], row['pid']])
    #convert the other track data into a data frame
    songPlaylist = pd.DataFrame(songPlaylistArray, columns=['trackid', 'artist_name', 'track_name', 'pid'])
    #save as csv file
    songPlaylist.to_csv('toclean.csv')
        