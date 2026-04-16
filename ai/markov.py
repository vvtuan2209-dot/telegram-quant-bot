from collections import defaultdict

def build(data):

    m = defaultdict(lambda: defaultdict(int))

    for d in data:
        nums = d["mn"] + d["mt"] + d["mb"]

        for i in range(len(nums)-1):
            a = str(nums[i]).zfill(2)
            b = str(nums[i+1]).zfill(2)
            m[a][b] += 1

    return m


def predict(m):

    out = {}

    for i in range(100):
        k = str(i).zfill(2)
        nxt = m.get(k,{})

        total = sum(nxt.values()) + 1

        out[k] = sum(v/total for v in nxt.values())

    return out
