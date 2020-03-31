# [-3,-2,-1,2,10,15,16,18,19,20] '-3--1,2,10,15,16,18-20'
# [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20,21,22,24]
# '-6,-3-1,3-5,7-11,14,15,17-22,24
'''
def solution(args):
    i = 0
    li = []
    while i <= len(args)-1:
        try:
            if args[i] + 1 == args[i+1] and args[i+1] +1 == args[i+2]:
                check_count = 2
                while len(args)-1 >= i + check_count:
                    if args[i] + check_count == args[i+check_count]:
                        check_count += 1
                    else:
                        check_count -= 1
                        break
                li.append('%d-%d'%(args[i],args[i+check_count]))
                i += (check_count + 1)
            else:
                li.append(str(args[i]))
                i += 1
        except IndexError:
            print('报错了i=',i)
            li.append(str(args[i]))
            i += 1
    return ','.join(li)

def solution(args):
    li = []
    my_index = 0
    i =0
    if len(args) < 3:return args
    while i < len(args):
        now_index = i
        j = i+1
        while j <= len(args):
            if j != len(args) and args[j] == args[j-1]+1:
                j+=1
            else:
                if j >=(now_index +3):
                    li.append(str(args[now_index])+'-'+str(args[j-1]))
                    my_index += 1
                    i = j - 1
                    break
                else:
                    li[my_index:] = args[i:j]
                    my_index += (j-i)
                    i = j-1
                    break
        i += 1
    return ','.join(map(str,li))
'''
def solution(args):
    out = []
    beg = end = args[0]
    for n in args[1:] + ['']:
        if n != end +1:
            if end == beg:
                out.append(str(beg))
            elif end == beg +1:
                out.extend([str(beg),str(end)])
            else:
                out.append(str(beg)+'-'+str(end))
            beg = n
        end = n

        
    return ','.join(out)




if __name__ == '__main__':
    t = [1,2,3,4,5]
    r = solution(t)
    print(r)
#    assert r == '-6,-3-1,3-5,7-11,14,15,17-22,24'
            
            
        
        
    
