import json

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from dice.artists.models import Artist


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
            similarities.append(0)

    knn_indices = sorted(
        range(len(similarities)), key=similarities.__getitem__, reverse=True
    )[:k]
    return dataset.iloc[knn_indices].id.to_numpy()


def get_recommendation_closest_artist(k=5, user_embedding=None):
    """

    :param k: Specifies how many recommendations to generate for k users.
    :param user_embedding: User embedding
    :return: Predicted artists as list
    """
    if not user_embedding:
        user_embedding = [0] * 32

    user_embedding = np.asarray(json.loads(user_embedding))
    artist_data = pd.DataFrame(list(Artist.objects.all().values()))

    # model = joblib.load("clustering.joblib")

    return {
        "recommendations": k_nearest_neighbors(
            artist_data, user_embedding, k
        ).tolist()
    }


def get_recommendation_closest_per_cluster(k=5, user_embedding=None):
    """

    :param k: Number of neighbors
    :param user_embedding:
    :return:
    """
    if not user_embedding:
        user_embedding = [0] * 32

    model = joblib.load("rec_engine/data/clustering.joblib")
    artist_data = pd.DataFrame(list(Artist.objects.all().values()))

    user_embedding = np.asarray(json.loads(user_embedding))

    user_pred = model.predict(user_embedding.reshape(1, -1))

    cluster_artist_ids = []

    for index, data in artist_data.iterrows():
        try:
            artist_embedding = np.asarray(
                json.loads(data["embedding"])
            ).reshape(1, -1)
            if model.predict(artist_embedding) == user_pred:
                cluster_artist_ids.append(data["id"])
        except Exception:
            # Ignoring ValueError there are some empty features.
            pass

    artist_dataset = artist_data[artist_data.id.isin(cluster_artist_ids)]
    return {
        "recommendations": k_nearest_neighbors(
            artist_dataset, user_embedding, k
        ).tolist()
    }
