import re
import collections
def is_pangram(st):
    pattern = '[^a-z]'
    counter = 0
    st = re.sub(pattern, "", st.lower())
    print(st)
    counter = collections.Counter(st)
    print(counter)
    if len(counter) == 26:
        return True
    else:
        return False
    
print(is_pangram("The quick brown fox jumps over the lazy dog."))