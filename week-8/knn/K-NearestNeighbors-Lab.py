from scipy.spatial.distance import euclidean
import numpy as np

class KNN():
    def __init__():
        pass
    #Given: X_train -> list of values
    #       y_train -> list of different types of labels for values
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict():
        pass
    #Given: x -> a value
    #function: returns distances from that value
    def _get_distances(self, x):
        dists = []
        i = 0
        for y in self.X_train:
            dists.append(i, (euclidean(x, y)))
            i += 1
        return dists
    #Given : dists -> list of distaces from point
    #       k -> quantity of top distances wanted returned
    #get nearest neighbors
    #return k amount of them
    def _get_k_nearest(self, dists, k):
        k_nearest = sorted(dists, key = lambda x : x[1])
        return k_nearest[:k]

    #Given: none
    #Return the label that is most common from nearest neighbors
    def _get_label_prediction(self):
        nearest_index = []
        for t in dists:
            nearest_index.append(t[0])

        return np.argmax(np.bincount( |total counts for each label|))
