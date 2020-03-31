'''
def monkey_count(n):
    li = []
    for i in range(1,n+1):
        li.append(i)
    return li
'''
def monkey_count(n):
    return list(range(1,n+1))

if __name__ == '__main__':
    r = monkey_count(5)
    print(r)
