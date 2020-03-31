'''
      1
    3  5
   7  9 11
 13 15 17 19
21 23 25 27 29
'''

'''
def odd_row(n):
    li = []
    n1 = n+(n-1)**2
    for i in range(n):
        li.append(n1)
        n1 += 2
    return li

'''
def odd_row(n):
    return list(range(n**2 -n +1,n**2+n,2))



if __name__ == '__main__':
    r = odd_row(10)
    print(r)
