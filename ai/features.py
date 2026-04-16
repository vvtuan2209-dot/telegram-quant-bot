import numpy as np

def build_features(data):

    flat = []

    for d in data:
        for k in ["mn","mt","mb"]:
            flat += d[k]

    X, y = [], []

    for i in range(len(flat)-10):
        window = flat[i:i+10]

        freq = {x:window.count(x) for x in set(window)}
        entropy = len(set(window)) / 10

        X.append([
            np.mean(window),
            np.std(window),
            entropy
        ])

        y.append(flat[i+10])

    return np.array(X), np.array(y)
