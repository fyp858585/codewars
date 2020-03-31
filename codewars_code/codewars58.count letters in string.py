# count letters in string
#'arithmetics'
# {'s': 1, 'e': 1, 'c': 1, 'i': 2, 'm': 1, 'a': 1, 't': 2, 'h': 1, 'r': 1}
'''
def letter_count(s):
    dic = {}
    for i in sorted(s):
        if i not in dic:
            dic[i] = s.count(i)
    return dic




def letter_count(s):
    li = []
    li = [s.count(i) for i in sorted(s) if i not in li]
    print(li)
    print(sorted(s))
    return dict(zip(sorted(s),li))
'''
def letter_count(s):
    return {i:s.count(i) for i in sorted(s)}


if __name__ == '__main__':
    r = letter_count('arithmetics')
    print(r)

