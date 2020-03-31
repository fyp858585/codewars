# *可以代替任何数字 返回其中能被6整除的数字
# 例如 输入'*2' return ['12','42','72']
# 输入'*2*' return ['024','120','126','222','228','324','420',426','522','528','624','720','726','822','828','924']

def is_divisible_by_6(string):
    li = []
    l = len(string)
    dic = {string[i]:i for i in range(l)}
    for i in range(10**(l-1),10**l-1):
        str1 = str(i)
        num = ''
        for j in dic:
            try:
                num = int(j)
            except ValueError:
                pass
            if type(num) == int:
                if j == str1[dic[j]]:
                    if i%6 ==0:
                        li.append(i)
    return li

if __name__ == '__main__':
    r = is_divisible_by_6('*2*')
    print(r)
        
        
        
