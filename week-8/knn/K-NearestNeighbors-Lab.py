from scipy.spatial.distance import euclidean
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

class KNN():
    def __init__(self):
        self.X_train = None
        self.y_train = None
    #Given: X_train -> list of values
    #       y_train -> list of different types of labels for values
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    #Given: x -> a value
    #function: returns distances from that value
    def _get_distances(self, x):
        dists = []
        i = 0
        for y in self.X_train:
            dists.append((i, euclidean(x, y)))
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
    def _get_label_prediction(self, k_nearest):
        labels = [self.y_train[i] for i, _ in k_nearest]
        return np.argmax(np.bincount(labels))

    #Given: X_test -> test values
    #      k -> number of nearest neighbors
    #return list of labels for nearest neighbors at each test point
    def predict(self, X_test, k = 3):
        preds = []
        for x in X_test:
            dists = self._get_distances(x)
            nearest = self._get_k_nearest(dists, k)
            preds.append(self._get_label_prediction(nearest))
        return preds


iris = load_iris()
data = iris.data
target = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state = 0, train_size = 0.25)

knn = KNN()
knn.fit(X_train, y_train)
preds = knn.predict(X_test, 3)

print("Testing Accuracy: {}".format(accuracy_score(preds, y_test)))
