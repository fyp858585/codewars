'''
def solution(s):
    li = []
    if not s:
        return li
    
    if len(s)%2==0:
        zhen = 'ou'
    else:
        zhen = 'ji'
    count = 0
    if zhen == 'ou':
        for i in range(len(s)):
            if i%2 !=0:
                li.append(s[i-1]+s[i])
    elif zhen == 'ji':
        for i in range(len(s)):
            if i%2 !=0:
                if i != len(s)-1:
                    li.append(s[i-1]+s[i])
            else:
                if i == len(s)-1:
                    li.append(s[i]+'_')

    return li
    
import re
def solution(s):
    return re.findall('.{2}',s+'_')


def solution(s):
    result = []
    if len(s)%2:
        s += '_'
    for i in range(0,len(s),2):
        result.append(s[i:i+2])
    return result


def solution(s):
    li =[]
    if len(s)%2 !=0: s += '_'
    for i in range(len(s)):
        if i%2 !=0:
            li.append(s[i-1]+s[i])
    return li

'''
def solution(s):
    if len(s)%2 !=0: s+='_'
    return [s[i-1]+s[i] for i in range(len(s)) if i%2!=0]


if __name__ == '__main__':
    r = solution('asdfads')
    print(r)
    
