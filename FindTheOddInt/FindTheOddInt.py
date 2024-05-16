def find_it(seq):
    store = {}
    for i in seq:
        if i not in store:
            store[i] = int(seq.count(i))
    for i in store:
        if store[i] % 2 != 0:
            return i


find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])