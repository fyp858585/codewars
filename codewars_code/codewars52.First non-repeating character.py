# 第一个非重复字符
# 例如 stress 返回 t
# 大小写都被认为一个字符 例如 sTreSS 返回 T



def f(s):    
    low = s.lower()
    for i in range(len(low)):
        if low.count(low[i]) ==1:
            return s[i]
    return None

if __name__ == '__main__':
    r = f('')
    print(r)

        
