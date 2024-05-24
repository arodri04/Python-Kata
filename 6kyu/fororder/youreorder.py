def order(sentence):
    words = []
    splitting = sentence.split()
    for i in range(1,10):
        for word in splitting:
            if str(i) in word:
                words.append(word)
    return " ".join(words)