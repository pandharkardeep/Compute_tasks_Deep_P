import re

def fun(s):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    
    if re.match(pattern, s):
        return True
    else:
        return False