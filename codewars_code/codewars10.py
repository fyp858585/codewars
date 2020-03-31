### 统一大小写 如果大写多于小写就全变为大写 不多于就全变成小写
# 如 code >>> code  CODe>>>CODE COde>>>code

def solve(s):
    low = [x for x in s if x.islower() == True]
    up = [y for y in s if y.isupper() == True]
    return s.lower() if len(low)>=len(up) else s.upper()

    

if __name__ == '__main__':
    a = 'COde'
    r = solve(a)
    print(r)
    
