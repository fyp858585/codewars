# 'abc' 返回 {'a':2,'b':1}
# {} 返回 {}

from collections import Counter
'''
def count(string):
    return Counter(string)

def count(string):
    return {i:string.count(i) for i in string}



'''


def count(string):
    dic = {}
    for i in string:
        if i not in dic:
            dic[i] = string.count(i)
    return dic


if __name__ == '__main__':
    r = count('abcaaa')
    print(r)



