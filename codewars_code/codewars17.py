'''
def longest(s1,s2):
    answer = ''
    li = sorted(set(s1+s2))
    for i in li:
        answer += i
    return answer
'''


def longest(s1,s2):
    return "".join(sorted(set(s1+s2)))



if __name__ == '__main__':
    r = longest('wwwwww','ggggga')
    print(r)
    
