def who_is_next(n,r):
#   return n[r-len(n)+1] if r > len(n) else n[r-1]
    while r > len(n):
        r = (r-len(n)+1)//2
    return n[r-1]
    

if __name__ == '__main__':
    result = who_is_next(['peter1','bob2','luci3','xiuer4','sb5'],52)
#   result = who_is_next(['peter1','bob2','luci3'],52)
#    result = who_is_next(['peter1','bob2','luci3'],4)
    print(result)


