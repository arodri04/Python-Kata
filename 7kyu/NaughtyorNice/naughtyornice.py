def what_list_am_i_on(actions):
    nicecount = 0
    ncount = 0
    for action in actions:
        naughty = ["b", "k","f"]
        
        nice = ["g","s","n"]
        
        print(action[0])
        if action[0] in naughty:
            ncount += 1
        if action[0] in nice:
            nicecount += 1
            
    print(nicecount, ncount)
    if nicecount > ncount:
        return "nice"
    else:
        return "naughty"