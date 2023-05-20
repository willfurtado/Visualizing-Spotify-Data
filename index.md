### Carefully Crafted By: *William Furtado* | [Code Available Here](https://github.com/willfurtado/Visualizing-Spotify-Data/)

As an avid Spotify user and a lover of all-things-data, the endless possibilites of what I could do with music streaming data have always been
at the forefront of my mind. This curiosity inspired me to dive head-first into a microcosmic Spotify project.

The project is broken into four main sections -- each with its own Jupyter Notebok. The four sections are as follows:

1. **[Exploratory Data Analysis](https://htmlpreview.github.io/?https://github.com/willfurtado/Visualizing-Spotify-Data/blob/master/html_files/Spotify%20EDA.html)**: Within this section, I used my personal streaming data over a one year period in order to identify any significant listening patterns or habits. Additionally, this section walks through certain statistical tests such as A/B testing in order to determine if there was any significant statistical differences in regards to my top artists and songs.

2. **[Spotify Web API](https://htmlpreview.github.io/?https://github.com/willfurtado/Visualizing-Spotify-Data/blob/master/html_files/Spotify%20Web%20API.html)**: The primary focus of this section was to use Spotify's Web API (by means of the Python module `Spotipy`) in order to obtain the audio features of each unique song within my listening history. It uses manual filtering of "White Noise" tracks or "Podcast Tracks". After using Pandas in order to create a DataFrame of all songs, it saves them to a CSV file for easier access.

3. **[k-Means Clustering via PCA and tSNE-Reduction](https://htmlpreview.github.io/?https://github.com/willfurtado/Visualizing-Spotify-Data/blob/master/html_files/Spotify%20Music%20PCA%2C%20k-Means.html)**: The obtained songs from above, along with their audio features provided the basis for my k-Means clustering model (scikit-learn). I employed both t-distributed stochastic neighbor embedding (t-SNE) and principal component analysis (PCA) to reduce the  higher dimensional data into a 
two-dimensional dataset. To visualize my clustering model, I used Python packages Seaborn and Matplotlib in order to showcase the distinction of genres.

4. **[Playlist Analysis:](https://htmlpreview.github.io/?https://github.com/willfurtado/Visualizing-Spotify-Data/blob/master/html_files/Playlist%20Analysis.html)** Using Spotify's Web API, I constructed a series of Python Classes (CurrentUser, Playlist, Track) that stores the necessary information for a given Spotify user. A simple call to the CurrentUser constructor will extract all songs from all of the user's playlists and their associated metadata. Using this object-oriented approach, I created tools to compare two different playlists using a visualization of their audio features and a theoretical matching score.

All aforementioned visuals are included within the `images` folder, and the CSV file contain all features for my streaming history can be found in the `data/tops` folder.
