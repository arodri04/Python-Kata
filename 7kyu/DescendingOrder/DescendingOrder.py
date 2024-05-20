def descending_order(num):
    numbers = list(str(num))
    numbers = [ int(i) for i in numbers ]
    numbers.sort(reverse = True)
    numbers = map(str, numbers)
    numbers = ''.join(numbers)
    numbers = int(numbers)
    return numbers
descending_order(51)