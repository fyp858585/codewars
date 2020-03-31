# [1, 5, 6, 25, 76, 376, 625, 9376, 90625, 109376, 890625] 的方末尾是该数字
import time

time1 = time.time()

def green():
    li = []
    for i in range(1,9999999):
        long = len(str(i))
        answer = str(i**2)
        str1 = ''
        for j in range(long,0,-1):
            str1+= answer[-j]
        if str1==str(i):
            li.append(i)
    return li

'''

def green():
    li = []
    for i in range(1,9999999):
        answer = str(i**2)
        if str(i) == answer[len(answer)-len(str(i)):len(answer)]:
            li.append(i)
    return li

'''
if __name__ == '__main__':
    r = green()
    print(r)
    time2 = time.time()
    print('耗时为：',time2-time1)
