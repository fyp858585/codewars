# 接收一个数组，偶数放前边，从小到大 奇数放后边 从大到小 且去重
# 例子 [12,14,7,3,14,17]  返回 [12,14,17,7,3]




def men_from_boys(arr):
    ji = [i for i in arr if i%2 !=0]
    ou = [i for i in arr if i%2 ==0]
    answer = sorted(set(ou)) + sorted(set(ji))[::-1]
    return answer


if __name__ == '__main__':
    r = men_from_boys([12,14,7,3,14,17])
    print(r)

