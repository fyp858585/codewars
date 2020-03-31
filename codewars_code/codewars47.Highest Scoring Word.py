# a = 1 , b = 2 , c = 3 , 以此类推，返回字符串中加起来最大的单词
# 例：man i need a taxi up to ubud 返回 'taxi'
'''
def high(x):
    letter = [chr(i) for i in range(ord('a'),ord('z')+1)]
    nums = list(range(1,27))
    dic = {}
    for i in nums:
        dic[letter[i-1]] = i
    x_split = x.split(' ')
    answer = {}
    for word in x_split:
        and1 = 0
        for j in word:
            and1 += dic[j]
        answer[and1] = word
    max1 = max(answer.keys())
    return answer[max1]



def high(x):
    words = x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]
'''

def high(x):
    return max(x.split(),key=lambda k: sum(ord(c) -96 for c in k))




if __name__ == '__main__':
    r = high('take me to semynak')
    print(r)
    
# man i need a taxi up to ubud
# what time are we climbing up the volcano
