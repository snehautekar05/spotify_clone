import pandas as pd
import pickle
import os

module_path = os.path.dirname(__file__) # D:\VESIT\ISTE\SpotifyClone\BackendWorkshop\SpotifyClone-Day1-Backend\SpotifyClone-Day1-Backend\recommendation\
df_songs = pd.read_csv(os.path.join(module_path, r'data/mergedFile.csv'))
loaded_model = pickle.load(open(os.path.join(module_path, r'model/recommendation_model.pkl'), 'rb'))

def getRecommendations(query_vector):
    distances, indices = loaded_model.kneighbors([query_vector])
    similarity_score = 1 - distances.flatten()
    df_recommended = df_songs.loc[indices.flatten()]
    df_recommended["similarity"] = similarity_score
    recommended_songs = df_recommended[["id", "similarity"]].to_dict(orient="records")
    return recommended_songs