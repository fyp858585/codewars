'''
def stringy(size):
    if size%2 ==0:
        return '10'*(size//2)
    else:
        return '10'*(size//2)+'1'


def stringy(size):
    return '10'*(size//2) if size%2 ==0 else '10'*(size//2)+'1'

def stringy(size):
    return '10' * (size//2) + '1' *(size % 2)

'''

def stringy(size):
    return ('10' * size)[:size]


    


if __name__ == '__main__':
    r = stringy(11)
    print(r)

