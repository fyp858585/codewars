# firstcharacter that repeats




'''
def first_dup(s):
    a = []
    for i in s:
        if i in a:
            return i
        else:
            a.append(i)
'''

def first_dup(s):
    for i in s:
        if s.count(i) > 1:
            return i
    return None


if __name__ == '__main__':
    r = first_dup('like')
    print(r)
