# 找出一个字符串中 最短的单词 如('IM going to the school') 2

'''
def find_short(s):
    c = 0
    li1 = s.split(' ')
    li2 = []
    for i in li1:
        a = len(i)
        if c == 0:
            c = a
        elif c < a:
            pass
        elif c > a:
            c = a
    l = c
    return l
'''

def find_short(s):
    return min(len(x) for x in s.split())


if __name__ == '__main__':
    r = find_short('whats your name yet')
    print(r)
