def reversible_prime(n):
    li = []
    for i in range(2,10000):
        for j in range(2,9999):
            if i%j==0:
                break
            else:
                li.append(i)
    return sorted(set(li))

if __name__ == '__main__':
    r = reversible_prime(100)
    print(r)

    
