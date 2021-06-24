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
        except Exception as e:
            # Ignoring ValueError there are some empty features.
            print(str(e))
            similarities.append(0)

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

    # user_data = pd.read_csv("data/users.csv")
    artist_data = pd.read_csv("data/artists.csv")
    # print(artist_data.embedding)

    # model = joblib.load("data/clustering.joblib")

    # print(model.labels_[0])
    # #print(model.cluster_centers_[4])
    # # print(np.array(user_embedding))
    # cos_similarity = cosine_distances(
    #     np.array(user_embedding).reshape(1, -1), model.cluster_centers_[4].reshape(1, -1)
    # )
    # print(cos_similarity)
    # print(dir(model.cluster_centers_[4]))

    return k_nearest_neighbors(artist_data, user_embedding, k)


def get_recommendation_closest_per_cluster(k, user_embedding=None):
    """

    :param k: Number of neighbors
    :param user_embedding:
    :return:
    """
    model = joblib.load("data/clustering.joblib")
    # artist_data = pd.read_csv("data/artists.csv")
    # artist_clusters = dict(
    #     zip(model.labels_, [[]] * len(model.cluster_centers_))
    # )

    centroids_partitions = {}
    for centr in model.cluster_centers_:
        centroid_label = model.predict([centr])
        partition = []
        for k, v in zip(np.asarray(user_embedding), model.labels_):
            if v == centroid_label:
                partition.append(k.ravel())

        centroids_partitions[centroid_label[0]] = partition

    print(centroids_partitions)
    # for idx, data in enumerate(artist_data.embedding):
    #
    #     try:
    #         data = np.asarray(json.loads(data))
    #         cluster_id = model.predict(data.reshape(1, -1))[0]
    #         artist_clusters[cluster_id].append(artist_data.iloc[idx].artist_id)
    #     except Exception as e:
    #         # Ignoring ValueError there are some empty features.
    #         pass
    # user_pred_cluster_id = model.predict(user_embedding)

    similarities = []

    # for key in cluster_centers:
    #     print(key)
    #     similarities.append(
    #         cosine_similarity(user_embedding, cluster_centers[key].reshape(1, -1))
    #     )

    print(similarities)
    return similarities


user_embedding = [
    [
        11.10895869880914688,
        -0.2602915018796921,
        -0.04395834915339947,
        -0.1307745985686779,
        -0.1724811524618417,
        -0.3164519965648651,
        -0.19310849905014038,
        -0.10748984850943089,
        -0.3036009967327118,
        -2.02278240118175745,
        -0.12700890470296144,
        0.14805049449205399,
        0.019154999405145645,
        0.23256349563598633,
        0.23936499655246735,
        0.019738999661058187,
        -0.21927350014448166,
        -0.31847649812698364,
        0.04209204763174057,
        -0.04799244925379753,
        0.15914399921894073,
        -4.45256100594997406,
        -0.03203900158405304,
        0.01025055069476366,
        0.09569354820996523,
        -0.21063600480556488,
        0.21290700137615204,
        0.25212400406599045,
        0.3082814961671829,
        0.04557859990745783,
        0.13332949951291084,
        0,
    ]
]

# b = get_recommendation_with_k_nearest_neighbors(5, user_embedding)
a = get_recommendation_closest_per_cluster(5, user_embedding)
