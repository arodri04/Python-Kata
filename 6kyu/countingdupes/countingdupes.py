def duplicate_count(text):
    list = []
    text = text.lower()
    for i in text:
        if text.count(i) > 1:
            if i not in list:
                list.append(i)
        
    return len(list)