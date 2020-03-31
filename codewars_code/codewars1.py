# 除了后四位都变为#号  如 abcdefg 变为 ###defg 123 变为 123 12345 变为 #2345
'''
def maskify(cc):
    li1 = list(cc)
    answer = ''
    long = len(cc)
    for i in range(long,0,-1):
        if i > 4:
            answer = answer + '#'
        elif i <= 4:
            answer = answer + li1[long-i]
    return answer
'''

#def maskify(cc):
#    if len(cc) <
def maskify(cc):
    li1 = list(cc)
    li2 = []
    if len(cc) >=5:
        for i in range(len(cc)-5,len(cc)-1):
            li2.append(li1[i])
    return cc if len(cc)<= 4 else '#'*(len(cc)-4) + ''.join(li2)




if __name__ == '__main__':
    cc = 'abcdefg'
    r = maskify(cc)
    print(r)


            
            
        
