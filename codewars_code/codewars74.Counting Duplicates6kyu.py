# 检查重复项不分大小写 如果多次重复也只算一次
# 例子 iiiiia 返回1 iiiiiiiiaa 返回2 aAbB 返回2
# abcd 返回 0
'''
def duplicate_count(text):
##    set1 = set(list(text.lower()))
##    if len(set1) == len(text):
##        return 0
    count = 0
    li = []
    lower = text.lower()
    for i in lower:
        if i not in li:
            if lower.count(i)>1:
                count += 1
                li.append(i)
    return count

'''
def duplicate_count(text):
    return len([i for i in set(text.lower()) if text.lower().count(i)>1])

                


if __name__ == '__main__':
    r = duplicate_count('iiiiiiiiaaa')
    print(r)
