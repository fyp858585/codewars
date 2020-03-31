def countBits(n):
    return str(bin(n)).count('1')



if __name__ == '__main__':
    r = countBits(1234)
    print(r)

