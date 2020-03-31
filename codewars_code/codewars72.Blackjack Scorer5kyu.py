def score_hand(cards):
    compare = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    score = sum([compare[i] for i in cards])
    count = cards.count('A')
    while score > 21:
        if 'A' in cards:
            if count >0:
                score -= 10
                count -= 1
            else:
                break
        else:
            break
    return score


def A(lis):
    lis1= []
    for i in lis:
        if i == 'J' or i =='Q' or i =='K':
            i=10
        elif i =='A':
            i=1
        else:
            i =int(i)
        lis1.append(i)
    count = sum(lis1)
    count_A=lis.count('A')
    for i in range(count_A):
            if count>=21:
                return count

            else:
                A=10
                count+=A
                break

    return count







if __name__ == '__main__':
    a = score_hand(['A','A','A','A','A','A','A','A','A','A','A','A'])
    r = A(['5','6','A','A'])
    print('a:',a,'r:',r)
