'''
A string of sorts

sort_strings('foo','of') return 'oofs'
sort_strings('string','gnirts') return 'gnits
sort_strings('banana','abn') return 'aaabnn'
'''

def sort_strings(s,ordering):
    a = list(s)
    li = []
    for i in ordering:
        for j in a:
            if i in a:
                li.append(i)
                a.remove(i)
    return ''.join(li+a)

if __name__ == '__main__':
    r = sort_strings('banana','abn')
    print(r)

    
