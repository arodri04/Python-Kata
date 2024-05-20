import re

def domain_name(url):
    pattern = r"([\w_-])+(\.)"
    results = re.sub(r'www.', '', url)
    results = re.search(pattern, results)
    return results[0].rstrip(".")

print(domain_name("http://google.com"))