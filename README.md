# Spotify Million Playlists DataSet Playlist Generator
PIC 16A, Fall 2022: Alice Lau, Alyssa Cosico, Trisha Patel
### Task:
Our goal is to use Spotify's Million Playlist Data Set to allow users to input an Artist, Album, and Song, and recieve a playlist recommendation isntead. 

## The Dataset:
The Million Playlist Dataset contains 1,000,000 playlists, including playlist titles, and track titles, created by US Spotify users on Spotify between January 2010 and October 2017. The playlists are samples from the over 4 billion plalists on Spotify, has over 2 million unique tracks by around 300,000 artists. 
Each playlist in the MPD contains the following: 
  **Name:** the name of the playlist
  **Collaborative:** bool value for whether the playlist is collaborative or not
  **Mofified_at:** the date of modification
  **Num_albums:** number of albums in the playlist
  **Num_tracks:** number of tracks in the playlist
  **Num_edits:** rounds of edits for the playlist
  **Duration_ms**: the length of the playlist timewise
  **num_artists**: the number of artists in the playlist
  **tracks:** 
    **pos:** number position of the track
    **artist_name:** the name of the artist of the track
    **track_uri:** the uri of the track
    **artist_uri:** the uri of the track
    **track_name:** name of the track
    **album_uri:** name of the album
    **duration_ms:** length of the song
    **album_name:** name of the album the song is in
    
    ##Scope and Limitations##:
    1. Due to the immense size of the Million Playlists Dataset, we were unable to use        the entire dat set, and thus some Playlists are missing during the calculations        where input data is compared to the dataset, and the playlist generated may not        be the best fit. 
    2. The Million Playlists Dataset is around 5 years ols and thus is missing much          information such as newer songs, the change in popularity of songs, and newer          playlists. 
##References:##
Project uses the Million Playlist Dataset: Ching-Wei Chen, Markus Schedl, Hamed Zamani, Paul Lamere. 
