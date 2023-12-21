import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle

df_songs = pd.read_csv(r'./data/mergedFile.csv')

# Preprocessing
df_features = df_songs.iloc[:,4:17]
df_features.dropna(inplace=True)

# Model Training
model = NearestNeighbors(n_neighbors=15, metric='cosine') # Give me the 15 nearest people/points jo similar hai humare
model.fit(df_features.values)

# Save the model
filename = r'./model/recommendation_model.pkl'
pickle.dump(model, open(filename, 'wb'))

# Loading the model
loaded_model = pickle.load(open(filename, 'rb'))
query_vector = [0.0555,0.754,142301.0,0.663,0.0,6.0,0.101,-6.311,0.0,0.427,90.195,4.0,0.207]
distances, indices = loaded_model.kneighbors([query_vector])
print(distances)
print(indices)

recommended_songs=df_songs.loc[indices.flatten()].values
print(recommended_songs)