def count_vegetables(string):
    list = string.split()
    list2 = []
    dict = {}  
    for i in list:
        if i not in dict:
            if i == "chopsticks":
                pass
            else:
                dict[i] = 1
        else:
            dict[i] += 1
    sdict = sorted(dict.items(), reverse=True)
    sdict = sorted(sdict, key=lambda x: x[1], reverse=True)
    for i in sdict:
        tup = (i[1], i[0])
        list2.append(tup)
    return list2
    