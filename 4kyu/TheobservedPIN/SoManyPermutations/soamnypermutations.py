import itertools


def permutations(s):
    # Code Away!
    store = []
    combinations = list(itertools.permutations(s))
    for i in combinations:
        comb = "".join(i)
        store.append(comb)
    store = list(dict.fromkeys(store))
    return store