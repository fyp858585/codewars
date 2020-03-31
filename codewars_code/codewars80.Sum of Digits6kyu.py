# 数字根是数字中所有数字的递归和，给定n，取n的数字之和，如果该值超过一位，则
# 继续以这种方式减小 直到产生一位数字，这仅适用于自然数
# 16 返回 7  因为 1+6 =7  456返回6 因为 4+5+6=15 1+5=6 所以返回6


'''
def digital_root(n):
    while n>=10:
        n = sum(int(i) for i in str(n))
    return n


def digital_root(n):
    if n <=10:
        return n
    else:
        return  digital_root(sum(int(i) for i in str(n)))
'''
def digital_root(n):
    if n <=10:
        return n
    else:
        n = sum(int(i) for i in str(n))
        return digital_root(n)
    
if __name__ == '__main__':
    r = digital_root(456)
    print(r)
