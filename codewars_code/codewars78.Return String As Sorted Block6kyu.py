def blocks(s):
    #str.isalpha
    s = sorted(s)
    li = []
    up = []
    num = []
    repetition_li = []
    repetition_up = []
    repetition_num = []
    for i in s:
        if i.isalpha() == True:
            if i.islower() ==True:
                if i not in li:
                    li.append(i)
                else:
                    repetition_li.append(i)
            else:
                if i not in up:
                    up.append(i)
                else:
                    repetition_up.append(i)
        else:
            if i not in num:
                num.append(i)
            else:
                repetition_num.append(i)
    answer = ''.join(li+up+num)
    if repetition_li and repetition_up and repetition_li:
        answer += '-'+'-'.join(repetition_li+repetition_up+repetition_num)
    return answer

if __name__ == '__main__':
    r = blocks('21AxBzxxxBBBB')
    print(r)
