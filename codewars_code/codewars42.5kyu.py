#recipe = {'flour':500,'sugar':200,'eggs':1}
#available = {'flour':1200,'sugar':1200,'eggs':5,'milk':200}
'''
def cake(recipe,available):
    li = []
    for k in recipe:
        if k not in available:
            return 0
        else:
            time = available[k]/recipe[k]
            li.append(int(time))
    return min(li)
'''

def cake(recipe,available):
    return min(available.get(k,0)//recipe[k] for k in recipe)




if __name__ == '__main__':
    r = cake({'flour':500,'sugar':200,'eggs':1},{'sugar':1200,'eggs':5,'milk':200})
    print(r)
