import json

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def k_nearest_neighbors(dataset, embedding, k):
    """
    Gets k nearest neighbors from dataset from user embedding.
    :param dataset: Artist dataset
    :param embedding: User embedding
    :param k: Number of neighbors
    :return: List of artist_ids
    """
    similarities = []
    for data in dataset.embedding:
        try:
            data = np.asarray(json.loads(data))
            similarities.append(
                cosine_similarity(embedding, data.reshape(1, -1))
            )
        except Exception:
            # Ignoring ValueError there are some empty features.
            pass

    knn_indices = sorted(
        range(len(similarities)), key=similarities.__getitem__, reverse=True
    )[:k]

    return dataset.iloc[knn_indices].artist_id.to_numpy()


def get_recommendation_with_k_nearest_neighbors(k=5, user_embedding=None):
    """

    :param k: Specifies how many recommendations to generate for k users.
    :param user_embedding: User embedding
    :return: Predicted artists as list
    """
    if not user_embedding:
        user_embedding = [0] * 32

    artist_data = pd.read_csv("artists.csv")

    # model = joblib.load("clustering.joblib")

    return k_nearest_neighbors(artist_data, user_embedding, k)


def get_recommendation_closest_per_cluster(k, user_embedding=None):
    """

    :param k: Number of neighbors
    :param user_embedding:
    :return:
    """

    model = joblib.load("clustering.joblib")
    artist_data = pd.read_csv("artists.csv")
    user_pred = model.predict(user_embedding)

    cluster_artist_ids = []

    for index, data in artist_data.iterrows():
        try:
            artist_embedding = np.asarray(
                json.loads(data["embedding"])
            ).reshape(1, -1)
            if model.predict(artist_embedding) == user_pred:
                cluster_artist_ids.append(data["artist_id"])
        except Exception:
            # Ignoring ValueError there are some empty features.
            pass
    artist_dataset = artist_data[
        artist_data.artist_id.isin(cluster_artist_ids)
    ]
    return k_nearest_neighbors(artist_dataset, user_embedding, k)
