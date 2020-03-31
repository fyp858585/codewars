from functools import reduce
'''apples,pears #and bananas\ngrapes\nbananas !apples,['#','!']

# 'a #b\nc\nd $e f g',['#','$']
def solution(string,markers):
    li = []
    zhizhen = True
    for i in string:
        if i in markers:
            zhizhen = False
        elif i == '\n':
            zhizhen = True
            li.append(i)
        elif i not in markers and zhizhen ==True:
            li.append(i)
    return ''.join(''.join(li).split(' '))





def solution(string,markers):
    return '\n'.join([reduce(lambda m,n:m.split(n)[0],markers,line).strip() for line in string.split('\n')])
'''

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)


if __name__ == '__main__':
    r = solution('apples,pears #and bananas\ngrapes\nbananas !apples',['#','!'])
    print(r)
