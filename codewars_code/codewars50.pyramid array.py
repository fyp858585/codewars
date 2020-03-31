# pyramid(0) []
# pyramid(1) [[1]]
# pyramid(2) [[1],[1,1]]
# pyramid(3) [[1],[1,1],[1,1,1]]

'''
def pyramid(n):
    answer = []
    for i in range(1,n+1):
        answer.append(i*[1])
    return answer
'''

def pyramid(n):
    return [i*[1] for i in range(1,n+1)]



if __name__ == '__main__':
    r = pyramid(4)
    print(r)
    
