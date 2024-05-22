import itertools

possible = {"1": ["1","2","4"], "2": ["1","2","3","5"], "3": ["2","3","6"], "4": ["1","4","5","7"],
             "5": ["2","5","6","8","4"], "6": ["3","5","6","9"], "7":["4","7","8"], "8": ["5","7","8","9","0"],
             "9": ["6","8","9"], "0": ["8","0"]}

def join_tuple_string(strings_tuple) -> str:
   return ''.join(strings_tuple)

def get_pins(observed):
    combos = []
    test = []
    for key, i in enumerate(observed):
        test.append(possible[i])

    final = list(itertools.product(*test))
    final2 = map(join_tuple_string, final)
    print(list(final2))
    return list(final2)
get_pins("369")

