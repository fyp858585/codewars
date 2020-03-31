# 您将得到一个字符串，对于字符串内的每一个符号，如果它是第一次出现用1替换，如果已经出现过用出现的次数替换
# 例子： 'Hello, World!' == '111211121311' 'aaaaaaaaaaaa' = '123456789101112'
import time
'''
def numericals(s):
    li = []
    answer = ''
    for i in s:
        li.append(i)
        answer += str(li.count(i))
    return answer


def numericals(s):
    li = []
    answer = []
    for i in s:
        li.append(i)
        answer.append(str(li.count(i)))
    return ''.join(answer)
'''

def numericals(s):
    answer = ''
    d = dict.fromkeys(s,0)
    for i in s:
        d[i] +=1
        answer += str(d[i])
    return answer

if __name__ == '__main__':
    time1 = time.time()
    r = numericals('Hello, World!')
    print(r)
    time2 = time.time()
    print(time2-time1)
    
    
