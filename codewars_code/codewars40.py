
def find_missing_letter(chars):
    for i in range(len(chars)-1):
        if ord(chars[i])+1 != ord(chars[i+1]):
            return chr(ord(chars[i]+1)

'''
def find_missing_letter(chars):
    return chr(ord(chars[i]+1) for i in range(len(chars)-1) if ord(chars[i])+1 != ord(chars[i+1]))


if __name__ == '__main__':
                       
    r = find_missing_letter(['a','b','c','e'])
    print(r)
                       
'''
