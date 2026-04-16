import numpy as np

def simulate(prob, runs=100000):

    keys = list(prob.keys())
    vals = np.array(list(prob.values()))

    vals = vals / vals.sum()

    result = np.random.choice(keys, size=runs, p=vals)

    unique, counts = np.unique(result, return_counts=True)

    return dict(zip(unique, counts / runs))


def top_pick(score):
    return max(score.items(), key=lambda x: x[1])
