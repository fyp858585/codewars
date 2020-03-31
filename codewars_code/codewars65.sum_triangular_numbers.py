'''
def sum_triangular_numbers(n):
    and1 = 0
    end1 = 0
    answer = 0
    for i in range(n):
        and1 += 1
        end1 += and1
        answer += end1
    return answer
'''

def sum_triangular_numbers(n):
    return n*(n+1)*(n+2)//6 if n>0 else 0

if __name__ == '__main__':
    r = sum_triangular_numbers(6)
    print(r)
    
    
