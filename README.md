# Spotify-Data-Analysis

As an avid Spotify user and a lover of all-things-data, the endless possibilites of what I could do with music streaming data have always been
at the forefront of my mind. This curiosity inspired me to dive head-first into a microcosmic Spotify project.

Using my personal account, I obtained the Spotify streaming history that I have accrued over the past year. I organized this data into a Pandas 
DataFrame, allowing me to perform EDA on it. Within this process, I also decided to perform hypothesis testing to determine if there was any statistical
significance between my listening habits. 

Using Spotify's Web API, I requested the audio features of the my top 1500 most listened to songs and created a new dataframe. After a round of 
data cleaning, there were about 1497 songs left; these songs along with their audio features provided the basis for my k-Means clustering model (scikit-learn). 
I employed both t-distributed stochastic neighbor embedding (t-SNE) and principal component analysis (PCA) to reduce the  higher dimensional data into a 
two-dimensional dataset. To conclude, I created a nine-part graphic that provides a visual representation of each predicted genre from my clustering models. 
