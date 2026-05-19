# ROC-AUC via Ranking

# here we need to understand that how much of the values in positive is greater than negatives 
# and then rank them based on that.

import numpy as np

def simple_auc(y_true, y_scores):
    pos = y_scores[y_true==1]       # get positives
    neg = y_scores[y_true==0]       # get negatives

    correct = 0
    total = 0

    for p in pos:
        for n in neg:           # count total pairs
            total+=1

            if p>n:         # count correct pairs
                correct+=1

            elif p==n:
                correct+=0.5

    return correct/total

# Example
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
auc = simple_auc(y_true, y_scores)
print(f"ROC-AUC: {auc:.3f}")

# Imagine:

# Positives = good students
# Negatives = weak students

# We check:

# “Did good student score higher than weak student?”

# If YES → +1 point
# If SAME → +0.5 point
# If NO → +0 point


#  <----------------------------------------------------->


# Top-k Feature Selection by Variance

# variance means how much values spread out like the difference

X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

import numpy as np

def topk_variance_features(X: np.ndarray, k: int) -> np.ndarray:
    variance = np.var(X, axis=0)        # compute variance of each column

    sorted_indices = np.argsort(variance)[::-1]     # get indices that would sort the variance using argsort in desding
                                                    # order and then reversing it

    topk_indices = sorted_indices[:k]               # find the top k elements

    return topk_indices


def topk_variance_features(X: np.ndarray, k: int) -> np.ndarray:
    return np.argsort(np.var(X, axis=0))[::-1[:k]]


#  <----------------------------------------------------->


# K nearest neighbour

# goal is to find the closet path to the query
# example the points are [1,1] , [0,0], [2,2], [3,3] and the point nearest to [1,1] is [1,1] obvisiouly and
# the second nearest is [0,0]. we do it using eucledian distance


def knn_retrieval(embeddings, query, k):

    distance = np.linalg.norm(embeddings-query, axis=1) # it calculates the eucledian distance on the points

    return np.argsort(distance)[:k]             # it will sort the indices   [1,0,2,3]

#     embeddings = np.array([                  and             query = np.array([1,1])

#     0 -- [0,0],                   square root([0-1]) ^2 + ([0-1]) ^2 = [square root (2)] = 1.4
#     1 -- [1,1],                    same for all of these  0
#     2 -- [2,2],                                            1.41
#     3 -- [3,3]                                             2.82
# ])      

# query = [1,1] so which points are closet to [1,1] think like that


#   here k is 2 so we calculate only [0,0] and [1,1] and we see closet is [1,1] and second closet is [0,0]
#   next is to sort the distances using argsort and then print the kth element here it is [1,0] 


#  <----------------------------------------------------->

# Logistic regression

import numpy as np

def logistic_regression(X, y, lr=0.1, T=100):

    n_samples, n_features = X.shape

    weights = np.zeros(n_features)

    loss_history = []

    for i in range(T):

        z = X @ weights

        predictions = 1 / (1 + np.exp(-z))

        loss = -np.mean(
            y*np.log(predictions + 1e-9) +
            (1-y)*np.log(1-predictions + 1e-9)
        )

        loss_history.append(loss)

        gradient = (X.T @ (predictions - y)) / n_samples

        weights = weights - lr * gradient

    return {
        "weights": weights,
        "loss_history": loss_history,
        "final_loss": loss_history[-1]
    }




