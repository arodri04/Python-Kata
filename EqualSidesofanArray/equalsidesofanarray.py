def find_even_index(arr):

    count = 0
    for i in arr:  
        print("Left: {}".format(arr[:i]))
        print("Right: {}".format(arr[i+1:]))
        if left(arr[:count]) == right(arr[count+1:]):
            print("nailed it")
            return count          
        count += 1
    else:
        return -1
def left(arr):
    lcount = 0
    for i in arr:
        lcount += i
    return lcount
        
def right(arr):
    rcount = 0
    for i in arr:
        rcount += i 
    return rcount

print(find_even_index([1,2,3,4,3,2,1]))