def likes(names):
    long = len(names)
    answer = ''
    if long == 0:
        return 'no one likes this'
    elif long == 1:
        return names[0] + ' ' + 'likes this'
    elif long == 2:
        return names[0] + ' and ' + names[1] +  ' ' + 'likes this'
    elif long == 3:
        return names[0] + ',' + names[1] + ' and ' + names[2] + ' ' +'likes this'
    elif long > 3:
        return names[0] + ',' + names[1] + ' and ' + str(long-2) + ' others likes this'

if __name__ == '__main__':
    r = likes(['peter','bob','lilith','eason','666','diao'])
    print(r)
    
