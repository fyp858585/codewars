def list_squared(m,n):
    answer = []
    for i in range(m,n+1):
        li = []
        for j in range(1,i+1):
            if i % j ==0:
                li.append(i**2)
        a = sum(li) **0.5
        if int(a) == a:
            answer.append([int(a),sum(li)])
    return answer


if __name__ == '__main__':
    r= list_squared(1,250)
    print(r)

    
        
            
