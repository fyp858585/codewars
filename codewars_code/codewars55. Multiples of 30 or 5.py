def solution(number):
    answer = 0
    for i in range(number):
        if i%3 == 0 or i%5 ==0:
            answer += i
    return answer

'''

def solution(number):
    return sum(x for x in range(number) if x%3 ==0 or x%5 ==0)
'''

if __name__ == '__main__':
    r = solution(999)
    print(r)

    
