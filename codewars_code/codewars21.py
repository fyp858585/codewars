# 如果字符串内有 'coverage' 就换为'covfefe' 如果没有在结尾加个'covfefe' 结尾前要有空格

'''
def covfefe(s):
    a = 'covfefe'
    li = []
    for i in s.split(' '):
        if i == 'coverage':
            li.append(a)
        else:
            li.append(i)
    if a in li and a not in s:
        return ' '.join(li)
    else:
        li.append(a)
        return ' '.join(li)
'''

def covfefe(s):
    return s.replace('coverage','covfefe') if 'coverage' in s else s+' covfefe'




if __name__ == '__main__':
    q = 'coverage covfefe'
    r = covfefe(q)   
    print(r)
        

