# Spotify Million Playlists DataSet Playlist Generator
PIC 16A, Fall 2022: Alice Lau, Alyssa Cosico, Trisha Patel

## Task:
Our goal is to use Spotify's Million Playlist Data Set to allow users to input an Artist and Song, and recieve a playlist recommendation isntead. 

## The Dataset:
The Million Playlist Dataset contains 1,000,000 playlists, including playlist titles, and track titles, created by US Spotify users on Spotify between January 2010 and October 2017. The playlists are samples from the over 4 billion plalists on Spotify, has over 2 million unique tracks by around 300,000 artists. 
Each playlist in the MPD contains the following:<br>
  **Name:** the name of the playlist<br>
  **Collaborative:** bool value for whether the playlist is collaborative or not<br>
  **Mofified_at:** the date of modification<br>
  **Num_albums:** number of albums in the playlist<br>
  **Num_tracks:** number of tracks in the playlist<br>
  **Num_edits:** rounds of edits for the playlist<br>
  **Duration_ms**: the length of the playlist timewise<br>
  **num_artists**: the number of artists in the playlist<br>
  **tracks:**<br> 
  **pos:** number position of the track<br>
  **artist_name:** the name of the artist of the track<br>
  **track_uri:** the uri of the track<br>
  **artist_uri:** the uri of the track<br>
  **track_name:** name of the track<br>
  **album_uri:** name of the album<br>
  **duration_ms:** length of the song<br>
  **album_name:** name of the album the song is in<br>
  
## Python Packages Used:<br>
Pandas: Version 1.4.2<br>
Json5: 0.9.6 <br>
Numpy: 1.21.5<br>

## Description of the Demo File:<br>
**Cleaning Data:**
Prior to the demo file, function JsontoCSVConverter was used to convert the data slice we acquired into csv format. This function was implemented along with other cleaning mechanisms in the SongsClearningDataFinal.ipynb final which results in the clean.csv file we have provided. <br>

**Custom Class:**
We have defined Custom Class FindPlaylists as can be seen in the FindPlaylistsFinal.py file. This class includes methods __init__(), query(), __str__(), findRecs(), and showResults that are called in the demo file. 
### Contents of the Demo File:
**1. Read data, and drop unused columns.**<br>
  In the first we load the cleaned csv file from gitHub url and display it:
   <img width="703" alt="Screen Shot 2022-12-10 at 6 14 55 PM" src="https://user-images.githubusercontent.com/114253491/206880606-9d421d32-4c65-4440-b776-8d8fb5365f06.png"><br>
   *fig 1. cleanCSV(head): the above figure shows the first few rows of the slice of the million playlists data we are working with in this project.*<br>
**2. Collect input:**<br>
  An instance of the class FindPlaylists is created, and input is prompted as per the __init__(self,data) method of the class.
  We ask for an Artist Name and Song Name from that Artist. Only one is required to generate the playlist. 
  We also call the method f.query() which returns a list of the user inputs so that the user can refer back to the artist/song they provided.<br> 
**3.str method:**<br>
We call the __str__() method that prints the list of the users inputs and notifies them that the playlist recommendation is being generated. <br>
**4.Generate Recommendations:**<br>
FindRecs() method is called where the proportion of the inputted artist and inputted song in each playlist is calculated, and the average score and index of the playlist that has the highest score is returned.<br> 
**5. Show Results:**<br>
ShowResults() method is called that prints the recommended playlist id, the playlist score, and the songs within the playlist, returning the first 10 tracks in that playlist.<br> 

<img width="464" alt="Screen Shot 2022-12-10 at 6 13 57 PM" src="https://user-images.githubusercontent.com/114253491/206880825-cb7becae-722d-4474-84ea-d72056dca27c.png"><br>
*fig 2. Playlist Recommendation: the above figure shows the output generated when the final playlist is recommended.*<br>
## Scope and Limitations:<br>
  1. Due to the immense size of the Million Playlists Dataset, we were unable to use the entire data set, and thus some Playlists are missing during the calculations where input data is compared to the dataset, and the playlist generated may not be the best fit. <br>
  2. The Million Playlists Dataset is around 5 years old and thus is missing much information such as newer songs, the change in popularity of songs, and newer playlists.<br> 


## References:
Project uses the Million Playlist Dataset: Ching-Wei Chen, Markus Schedl, Hamed Zamani, Paul Lamere.<br> 
