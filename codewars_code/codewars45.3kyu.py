def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x**(n if n < 4 else n % 4 + 4)
    return n % 10



def last_digit(lst):
    if not lst:
        return 1
    else:
        out = 1
        for n in lst[len(lst):0:-1]:
            out = n**out
            if out > 2:
                out -=2
                out %= 4
                out += 2
    return lst[0]**out%10






if __name__ == '__main__':
    r = last_digit([3,4,5])
    print(r)
