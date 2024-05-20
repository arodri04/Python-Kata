def zero(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 0
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 0
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 0 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 0 / args[0][0]
                print(int(x))
                return int(x)   

    return 0

def one(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 1
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 1
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 1 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 1 / args[0][0]
                print(int(x))
                return int(x)

    return 1

def two(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 2
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 2
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 2 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 2 / args[0][0]
                print(int(x))
                return int(x)

    return 2

def three(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 3
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 3
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 3 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 3 / args[0][0]
                print(int(x))
                return int(x)

    return 3

def four(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 4
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 4
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 4- args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 4 / args[0][0]
                print(int(x))
                return int(x)

    return 4


def five(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 5
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 5
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 5 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 5 / args[0][0]
                print(int(x))
                return int(x)
    return 5

def six(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 6
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 6
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 6 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 6 / args[0][0]
                print(int(x))
                return int(x)
    return 6

def seven(*args): 
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 7
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 7
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 7 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 7 / args[0][0]
                print(int(x))
                return int(x)

    return 7 #your code here

def eight(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 8
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 8
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 8 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 8 / args[0][0]
                print(int(x))
                return int(x)
            

    return 8

def nine(*args):#your code here
    if len(args) > 0:
        if len(args[0]) > 1:
            if args[0][1] == "times":
                x = args[0][0] * 9
                print(x)
                return x
            elif args[0][1] == "plus":
                x = args[0][0] + 9
                print(x)
                return x
            elif args[0][1] == "minus":
                x = 9 - args[0][0]
                print(x)
                return x
            elif args[0][1] == "divided":
                x = 9 / args[0][0]
                print(int(x))
                return int(x)

    return 9

def times(*args):
    larg = list(args)
    larg.append("times")
    return larg
def plus(*args):
    larg = list(args)
    larg.append("plus")
    return larg
def minus(*args):
    larg = list(args)
    larg.append("minus")
    return larg
def divided_by(*args):
    larg = list(args)
    larg.append("divided")
    return larg


eight(plus(nine()))
eight(minus(nine()))
nine(divided_by(three()))

seven(times(five()))

four(divided_by(two()))
