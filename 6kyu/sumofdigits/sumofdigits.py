def digital_root(n):
    numlist = list(str(n))
    store = 0
    for i in numlist:
        store += int(i)
    if store > 9:
        store = digital_root(store)
    else:
        return store
    return store



print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))