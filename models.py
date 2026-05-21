# Models

# KNN
# find distance to the points, sort distances, pick k closest to the value and majority vote


import numpy as np

def knn_predict(X_train, y_train, X_test, k):
    preds = []

    for x in X_test:
        distances = np.sum(np.abs(X_train-x), axis=1) # manhattan
                                     # subtract query from all points

        idx = np.argsort(distances)[:k] # sort nearest points

        labels = y_train[idx]
        preds.append(np.bincount(labels).argmax())  # majority vote

    return np.array(preds)
#  <----------------------------------------------------->

# Decision tree
# is it rainy? -- yes (stay home), no (go play)

# Entropy : messiness/uncertainity
# H = -sigma summation of [plog2basep]

# Information Gain
# how much uncertainty reduced
# tree chooses split with highest information gain

# problem of trees : overfitting, unstable
# to fix : pruning/limiting depth


#  <----------------------------------------------------->

# ACTIVITY 3: NAIVE BAYES

# probability based clasifier
# example : spam detection 

# here the features are independent [calculates probabilities, multiply and choose highest]

# Gaussian Process 
# it predicts distribution and gives prediction, uncertanity
# good for small data and shows confidence


# | Model            | Idea                     |
# | ---------------- | ------------------------ |
# | KNN              | nearest points vote      |
# | Tree             | if-else rules            |
# | Naive Bayes      | probability              |
# | Gaussian Process | prediction + uncertainty |



import numpy as np

class KNN:

    def __init__(self, k=3, mode="classification"):
        self.k , self.mode = k, mode

    def fit(self, X, y):        
        self.X_train , self.y_train = X, y

    def predict(self, X):
        pred = []

        for x in X:
            d = np.sqrt(np.sum((self.X_train - x)**2, axis=1))
            # computes eucledian distance

            idx = np.argsort(d)[:self.k]

            y = self.y_train[idx]
            pred.append(np.bincount(y).argmax()
                        if self.mode=="classification"
                        else np.mean(y))
            # most common label and counts frequency

        return np.array(pred)


#  <----------------------------------------------------->


# Navie Bayes Gaussian

# | Word     | Meaning                      |
# | -------- | ---------------------------- |
# | Naive    | assumes features independent |
# | Bayes    | probability rule             |
# | Gaussian | bell-curve distribution      |

# for each class we compute mean and variance and check likely
# new point belongs there.

# model learns where the mean learns average feature values
# and the vsriance learns spread of values

import numpy as np
class GaussianNB:
    def __init__(self, mode="classification"):
        self.mode = mode

    def fit(self, X, y):
        if self.mode == "classification":
            self.classes = np.unique(y)

            self.mean = {}
            self.var = {}

            for c in self.classes:
                X_c = X[y == c] # get class data
                self.mean[c] = np.mean(X_c, axis=0) # feature wise average
                self.var[c] = np.var(X_c, axis=0) # measure spread
        else:
            self.mean_y = np.mean(y)      # simplified regression

    def predict(self, X):       # predict new data
        preds = []

        if self.mode == "classification":
            for x in X:
                probs = []

                for c in self.classes:      # compute probability for every class
                    mean = self.mean[c]
                    var = self.var[c]         # get stored values

                    prob = -np.sum((x-mean)**2 / (2*var+1e-9))      # gaussian prob.
                    # measures how close is x to class center
                    # closer meaning higher probability

                    probs.append(prob)      # append probability
                preds.append(self.classes[np.argmax(probs)])    # largest prob. index

        else:
            preds = [self.mean_y] * len(X)      # predict average values everywhere
        return np.array(preds)
