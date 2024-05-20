import itertools

possible = {"1": ["1","2","4"], "2": ["1","2","3","5"], "3": ["2","3","6"], "4": ["1","4","5","7"],
             "5": ["2","5","6","8","4"], "6": ["3","5","6","9"], "7":["4","7","8"], "8": ["5","7","8","9","0"],
             "9": ["6","8","9"], "0": ["8","0"]}

list1 = ["7"]
list2 = ["1","2"]
list3 = [list1, list2]
print(list3)


def get_pins(observed):
    combos = []
    test = []
    for key, i in enumerate(observed):
        print("Key {}".format(key))
        print("Index: {}".format(i))
        test.append(possible[i])
        print(list(itertools.product(*test)))
    print(test)
    return test
get_pins("8")

