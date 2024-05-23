def fake_bin(x):
    str = ""
    for i in x:
        if int(i) >= 5:
            str += "1"
        else:
            str += "0"
    return str