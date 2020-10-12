# Spotify-Data-Analysis

Using my personal Spotify Account, I obtained my streaming history over the past year. I organized this data into a Pandas 
DataFrame, allowing me to perform EDA on it. Using Spotify's Web API, I requested the audio features of the my top 1500 most 
listened to songs and created a new dataframe. After a round of data cleaning, there were about 1497 songs left; these songs 
along with their audio features provided the basis for my k-Means clustering model (scikit-learn). I employed both t-distributed 
stochastic neighbor embedding (t-SNE) and principal component analysis (PCA) to reduce the  higher dimensional data into a 
two-dimensional dataset. 
