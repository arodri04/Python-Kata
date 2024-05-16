#!/usr/bin/env python3

#This is the solution I came up with without the kata site, where you can add an entry. Underneath commented is what I came up with using the kata site.
store = {'apple': "a fruit that grows on trees"}
userinput = ""

def newentry(key, desc):
    store[key] = desc
    return print("Added {}".format(key))

while userinput != "exit":
    userinput = input("Pick new, find, or exit: ")
    
    match userinput:
        case "new":
            key = input("what is the fruit: ")
            desc = input("description of the fruit: ")
            newentry(key, desc)
        
        case "find":
            key = input("What entry are you looking for: ")
            print(store[key])

        case _:
            print("Not found, Exiting")
            userinput = "exit" 

#class Dictionary():
#    def __init__(self):
#        # Your code
#        self.d = {}
#        pass
#        
#    def newentry(self, word, definition):
#        # Your code
#        self.d[word] = definition
#        pass
#        
#    def look(self, key):
        # your code
#        if key in self.d:
#            return self.d[key]
#        else:
#            return "Can't find entry for {}".format(key)
        
    