# 取字符串中间的字母 单数取中间一个，双数取中间两个 例如 test 取es  testing 取t
'''
def get_middle(s):
    li = []
    a = len(s)
    for i in s:
        li.append(i)
    if (a % 2) != 0:
        answer = li[(a//2)]
    if (a % 2) == 0:
        answer = li[(a//2 - 1)] + li[(a//2)]
    return answer



'''
def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]


'''
def get_middle(s):
    return ''.join(list(s[len(s)//2]) if len(s)%2 !=0 else list(s[(len(s)//2-1)]) + list(s[len(s)//2]))
'''







if __name__ == '__main__':
    r = get_middle('middle')
    print(r)
    r = get_middle('testing')
    print(r)

