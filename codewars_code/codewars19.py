# t = 最大里程
# k = 去的城市数量
# ls = 每个城市间的距离
# 230 4  430 5

# xs = [100,70,56,44,89,73,68,56,64,123,233,144,50,132,123,34,89]

from itertools import combinations

'''
def choose_best_sum(t,k,ls):
    return max((s for s in (sum(i) for i in combinations(ls,k)) if s<=t), default=None)
'''

def choose_best_sum(t,k,ls):
    sum2 = 0
    for i in combinations(ls,k):
        sum1 = sum(i)
        if sum1 >t:
            continue
        sum2 = max(sum2,sum1)
    if sum2 ==0:
        return None
    return sum2



if __name__ == '__main__':
    r = choose_best_sum(430,5,[100,70,56,44,89,73,68,56,64,123,233,144,50,132,123,34,89])
    print(r)
    

# combinations 函数返回所有排列组合
