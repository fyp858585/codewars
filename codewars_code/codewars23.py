'''
def capitalize(s):
    li = []
    li2 = []    
    for i in range(len(s)):
        if i%2 ==0:
            li.append(s[i].upper())
            li2.append(s[i].lower())
        else:
            li.append(s[i].lower())
            li2.append(s[i].upper())
    return [li,li2]
'''


def capitalize(s):

    li = [s[i].upper() for i in range(len(s)) if i%2==0 else s[i]]
    li2 = [s[i] for i in range(len(s)) if i%2==0 else s[i].upper()]
    return [li,li2]



if __name__ == '__main__':
    r = capitalize('abcdef')
    print(r)
    
