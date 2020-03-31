# codewars is nice输出#CodewarsIsNice
# 对字符串去空格 首写字母大写最开头+#号 长度不能超过140



'''
def generate_hashtag(s):
    if not s:
        return False
    answer = '#'
    li = s.strip(' ').split(' ')
    result = ''.join([i.capitalize() for i in li if i])
    if not result:
        return False
    answer += result
    if len(answer)>=140:
        return False
    return answer
'''

def generate_hashtag(s):
    return '#'+s.strip().title().replace(' ','') if 0<len(s)<=140 else False
    

if __name__ == '__main__':
    r = generate_hashtag('codewars is nice')
    print(r)
