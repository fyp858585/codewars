
def distinct_digit_year(year):
    for i in range(year+1,9001):
        if len(set(str(i))) == 4:
            return i
'''
def distinct_digit_year(year):
    return i for i in range(year+1,9000) if len(set(str(i)))==4
'''

if __name__ == '__main__':
    r = distinct_digit_year(1987)
    print(r)

    
