import random

def com(length : int):
    string = ''
    for _ in range(length):
        try:
            string += chr(random.randint(0,65355)).encode('utf8', 'replace').decode()
        except:
            pass

    return string

def a():
    string = ''
    for i in range(65355):
        string += chr(random.randint(i)).encode('utf8', 'replace').decode()
        

    return string



print(com(99999))