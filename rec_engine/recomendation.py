import joblib
import pandas as pd


user_data = pd.read_csv("data/users.csv", nrows=1)

model = joblib.load('data/clustering.joblib')

embedding = [
    [0.10895869880914688, -0.2602915018796921, -0.04395834915339947,
     -0.1307745985686779, -0.1724811524618417, -0.3164519965648651,
     -0.19310849905014038, -0.10748984850943089, -0.3036009967327118,
     -0.02278240118175745, -0.12700890470296144, 0.14805049449205399,
     0.019154999405145645, 0.23256349563598633, 0.23936499655246735,
     0.019738999661058187, -0.21927350014448166, -0.31847649812698364,
     0.04209204763174057, -0.04799244925379753, 0.15914399921894073,
     -0.45256100594997406, -0.03203900158405304, 0.01025055069476366,
     0.09569354820996523, -0.21063600480556488, 0.21290700137615204,
     0.25212400406599045, 0.3082814961671829, 0.04557859990745783,
     0.13332949951291084, -0.24659249931573868]
]

print("-------------")
model.predict(embedding)



