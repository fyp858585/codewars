'''
def name_in_str(str,name):
    n = 0
    for i in str:
        if i == name[n]:
            n += 1
    if n == len(name):
        return True
    else:
        return False



def name_in_str(str,name):
    n = 0
    for i in str:
        if i == name[n]:
            n += 1
    return True if n ==len(name) else False
'''

def name_in_str(str,name):
    it = iter(str.lower())
    return all(c in it for c in name.lower())



if __name__ == '__main__':
    r = name_in_str('Across the rivers','chris')
    print(r)

