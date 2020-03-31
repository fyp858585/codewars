# 返回长度（N）的列表，其倍数为（X） 如 (x=1,n=5) 返回[1,2,3,4,5])
# (x=3,n=5) 返回 [3, 6, 9, 12, 15] (x=50,n=5) 返回 [50, 100, 150, 200, 250]
def count_by(x,n):
    return list(range(x,x*n+1,x))

if __name__ == '__main__':
    r = count_by(3,5)
    print(r)
    
