'''
def count_sheep(n):
    answer = ''
    for i in range(1,n+1):
        answer += str(i)+' sheep...'
    return answer
'''

def count_sheep(n):
    return ' sheep...'.join(str(i) for i in range(1,n+1)) + ' sheep...'
