# V A P O R C O D E
'''
def vaporcode(s):
    return ' '.join([i.upper() for i in s.replace(' ','')])
'''

def vaporcode(s):
    return '  '.join(s.replace(' ','').upper())


if __name__ == '__main__':
    r = vaporcode('Lets go to the movies')
    print(r)

