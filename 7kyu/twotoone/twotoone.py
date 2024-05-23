def longest(a1, a2):
    str3 = ""
    a1 += a2
    for i in a1:
        if i not in str3:
            str3 += i
    return "".join(sorted(str3))