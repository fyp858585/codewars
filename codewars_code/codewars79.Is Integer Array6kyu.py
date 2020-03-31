def is_int_array(arr):
    if arr == '':
        return False
    if None in arr:
        return False
    for i in arr:
        try:
            if i == int(i):
                pass
            else:
                return False
        except:
            False
    return True

if __name__ == '__main__':
    r = is_int_array([1,2,None])
    print(r)
