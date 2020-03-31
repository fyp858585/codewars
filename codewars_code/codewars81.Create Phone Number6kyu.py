'''
def create_phone_number(n):
    answer = '('
    for i in range(3):
        answer += str(n[i])
    answer += ')'
    for i in range(3,6):
        answer += str(n[i])
    answer += '-'
    for i in range(6,10):
        answer += str(n[i])

    return answer
'''


def create_phone_number(n):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)




if __name__ == '__main__':
    r = create_phone_number([1,2,3,4,5,6,7,8,9,0])
    print(r)
    
