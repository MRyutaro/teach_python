from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import math


class FindTheMostSimilarHouse():
    def __init__(self, data, target, given_index=0):
        self.normalized_data = self.normalize_data(data)
        self.target = target
        self.given_index = given_index

    def normalize_data(self, data):
        scaler = MinMaxScaler([-1, 1])
        scaler.fit(data)
        return scaler.transform(data)

    def find_the_most_similar_house(self):
        i, distance = self.find_min_distance()
        print(
            f"自分が求めているのに最も似ている家：{self.house_info(self.given_index, self.normalized_data, self.target)}")
        print(
            f"自分が求めているのに最も似ている家：{self.house_info(i, self.normalized_data, self.target)}")
        # 類似度じゃないので納得してない。本当は%であらわせる数字にしたい。
        print(f"距離:{distance}")

    def find_min_distance(self):
        print("探索中...")
        the_most_similar_house_index = 0
        distance_min = float('inf')
        for i in range(len(self.normalized_data)):
            if i != self.given_index:
                distance = self.CalcDist(
                    self.normalized_data, self.given_index, i)
                if distance <= distance_min:
                    the_most_similar_house_index = i
                    distance_min = distance
                    print(distance_min)
        return the_most_similar_house_index, distance_min

    def CalcDist(self, data, idx1, idx2):
        vec1 = data[idx1, :]
        vec2 = data[idx2, :]
        return self.CalcEuclideanDistanceByNumpy(vec1, vec2)

    def CalcEuclideanDistanceByNumpy(self, vec1, vec2):
        euclidean_distance = math.sqrt(np.sum((vec1 - vec2)**2))
        return euclidean_distance

    def house_info(self, index, data, target):
        house_info = {"インデックス": index,
                      "属性": data[index, :],
                      "価格": target[index]}
        return house_info


if __name__ == "__main__":
    california = fetch_california_housing()
    ftmsh = FindTheMostSimilarHouse(california.data, california.target, 12981)
    ftmsh.find_the_most_similar_house()
