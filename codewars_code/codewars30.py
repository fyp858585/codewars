numbers = 'abcdefghijklmnopqrstuvwxyz'
'''
def add_letters(*letters):
    x = 0
    for i in letters:
        a = numbers.index(i) + 1
        x += a
    while x-1 > 25:
        x -= 26

    return numbers[x-1]
'''


def add_letters(*letters):
    ind = sum([numbers.index(i)+1 for i in letters])%26-1
    return numbers[ind]

        


if __name__ == '__main__':
    r = add_letters('z','a')
    print(r)
    
