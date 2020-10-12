#########################
### Imports and Setup ###
#########################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

plt.style.use('ggplot')

df = pd.read_csv('../features/features.csv', index_col=0)
df.dropna(how='any', inplace=True)

features =['danceability','energy','key','loudness', 'mode', 
		'speechiness', 'acousticness', 'instrumentalness', 
		'liveness','valence','tempo','duration_ms', 'time_signature']

x = df.loc[:,features].values
x = StandardScaler().fit_transform(x)

########################
## k-Means Clustering ## 
##      via PCA       ##
########################

pca = PCA(n_components=2)
principal_components = pca.fit_transform(x)

principal_df = pd.DataFrame(data=principal_components, columns=['principal_component_1', 'principal_component_2'])

music_data_pca = principal_df.to_numpy()
kmeans_pca = KMeans(n_clusters=7, random_state=0, init='random').fit(music_data_pca)
predicted_pca = kmeans_pca.fit_predict(music_data_pca)

target_df_pca = principal_df.copy()
target_df_pca['prediction'] = predicted_pca
target_df_pca.set_index(keys=df.index, inplace=True)

########################
## k-Means Clustering ##
## via tSNE Reduction ##
########################

tsne = TSNE(n_components=2)
x_embedded = tsne.fit_transform(x)
x_tsne = x_embedded[:,0]
y_tsne = x_embedded[:,1]
tsne_df = pd.DataFrame(data={'tsne_1': x_tsne,'tsne_2': y_tsne})

music_data_tsne = tsne_df.to_numpy()
kmeans_tsne = KMeans(n_clusters=7, random_state=0, init='random').fit(music_data_tsne)
predicted_tsne = kmeans_tsne.fit_predict(music_data_tsne)

target_df_tsne = tsne_df.copy()
target_df_tsne['prediction'] = predicted_tsne
target_df_tsne.set_index(keys=df.index, inplace=True)

#####################
## Grouping Genres ##
#####################

pred_0_pca = target_df_pca[target_df_pca['prediction'] == 0]
pred_1_pca = target_df_pca[target_df_pca['prediction'] == 1]
pred_2_pca = target_df_pca[target_df_pca['prediction'] == 2]
pred_3_pca = target_df_pca[target_df_pca['prediction'] == 3]
pred_4_pca = target_df_pca[target_df_pca['prediction'] == 4]

pred_0_tsne = target_df_tsne[target_df_tsne['prediction'] == 0]
pred_1_tsne = target_df_tsne[target_df_tsne['prediction'] == 1]
pred_2_tsne = target_df_tsne[target_df_tsne['prediction'] == 2]
pred_3_tsne = target_df_tsne[target_df_tsne['prediction'] == 3]
pred_4_tsne = target_df_tsne[target_df_tsne['prediction'] == 4]

#####################
## Comparison Plot ##
#####################

plt.subplot(1,2,1)
sns.scatterplot(x='principal_component_1', y='principal_component_2', data=target_df_pca, 
                hue='prediction', palette=sns.color_palette('hls',7), 
                style='prediction', markers=["X","X","X","X","X","X","X"])

for center, i in zip(kmeans_pca.cluster_centers_, range(7)):
    if not i:
        plt.scatter(center[0], center[1], marker='*',s=200, c='black', label='Centroid')
    else:
        plt.scatter(center[0], center[1], marker='*',s=200, c='black')
    
plt.xlabel('First Principal Component (PCA)')
plt.ylabel('Second Principal Component (PCA)')
plt.title('k-Means Clustering via PCA', pad=20)
plt.legend(shadow=True)

plt.subplot(1,2,2)
sns.scatterplot(x='tsne_1', y='tsne_2', data=target_df_tsne, 
				hue='prediction', palette=sns.color_palette('hls',7),
				style='prediction', markers=['X','X','X','X','X','X','X'])

for center, i in zip(kmeans_tsne.cluster_centers_, range(7)):
    if not i:
        plt.scatter(center[0], center[1], marker='*',s=200, c='black', label='Centroid')
    else:
        plt.scatter(center[0], center[1], marker='*',s=200, c='black')

plt.xlabel('t-SNE One')
plt.ylabel('t-SNE Two')
plt.title('k-Means Clustering via t-SNE Reduction', pad=20)
plt.legend(shadow=True)
plt.show();

















