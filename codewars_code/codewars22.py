'''
def abc(d):
    li = []
    for i in d:
        if i not in li:
            li.append(str(i))
    return int(''.join(li))
'''


#def min_value(digits):
#    return int(''.join(map(str,sorted(set(digits)))))

def min_value(digits):
    return int(''.join(str(x) for x in sorted(set(digits))))




if __name__ == '__main__':
    r = min_value([1,3,4])
    print(r)
    

