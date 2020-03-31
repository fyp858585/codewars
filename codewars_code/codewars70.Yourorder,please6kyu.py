# 输入 4of Fo1r pe6ople g3ood th5e the2 输出 Fo1r the2 g3ood 4of th5e pe6ople
# 按单词中的数字顺序排序


'''
def order(sentence):
    answer = ''
    li = sentence.split(' ')
    dic = {}
    for i in li:
        for j in range(1,len(li)+1):
            if str(j) in i:
                dic[j] = i
    for k in range(1,len(li)+1):
        answer += dic[k]+' '
    return answer


def order(sentence):
    answer = ''
    li = sentence.split(' ')
    dic = {j:i for i in li for j in range(1,len(li)+1) if str(j) in i}
    for k in range(1,len(li)+1):
        answer += dic[k]+' '
    return answer
'''  
def order(sentence):
    return ' '.join([j for i in range(1,10) for j in sentence.split(' ') if str(i) in j])




if __name__ == '__main__':
    r = order('4of Fo1r pe6ople g3ood th5e the2')
    print(r)

    
# '4of Fo1r pe6ople g3ood th5e the2'
# 'is2 Thi1s T4est 3a'
