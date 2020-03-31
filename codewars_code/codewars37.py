'''
def fake_bin(x):
    li = []
    for i in x:
        if int(i)<5:
            li.append('0')
        else:
            li.append('1')

'''
def fake_bin(x):
    return ''.join('0' if int(i)<5else '1' for i in x )


r = fake_bin('2131524415')
print(r)

