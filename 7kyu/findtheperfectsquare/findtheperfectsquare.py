from math import sqrt
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    print(sqrt(sq).is_integer())
    if sqrt(sq).is_integer():
        return ((sqrt(sq)+1)**2)
    return -1