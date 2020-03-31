'''
3,2 --> '1x^3'
12,5 --> '2x^6'
20,1 --> '10x^2'
40,3 --> '10x^4'
90,2 --> '30x^3'

'''



def int1(c,e):
    first = str(c//(e + 1))
    return ('%sx^%s'%(first,str(e+1)))


if __name__ == '__main__':
    r = int1(90,2)
    print(r)
    
