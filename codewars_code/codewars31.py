def next_version(version):
    l = version.count('.')
    print(l)
    
    a = int(''.join(version.split('.'))) + 1
    print(a)
    return '.'.join(str(a))





if __name__ == '__main__':
#    r = next_version('1.2.3.4.5.6.7.8.9')
    r = next_version('99.9')
    print(r)


