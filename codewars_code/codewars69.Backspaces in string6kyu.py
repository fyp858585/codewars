# 假设'#'就像键盘的退格键，这意味着'a#bc#d'实际上是‘bd'
# 您的任务是处理带有'#'符号的字符串
'''
'abc#d##c' ==> 'ac'
'abc##d#####' ==> ''
'#####' ==> ''
''  ==> ''
'''
def clean_string(s):
    li = list(s)
    time = li.count('#')
    for i in range(time):
        site = li.index('#')
        del li[site]
        if site -1<0:
            pass
        else:
            del li[site-1]
    return ''.join(li)

def clean_string(s):
    stk = []
    for c in s:
        if c=='#'and stk:
            stk.pop()
        elif c!='#':
            stk.append(c)
    return ''.join(stk)

if __name__ == '__main__':
    r = clean_string('a#bc#d')
    print(r)

# 'a#bc#d'
