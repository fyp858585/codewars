#a = 'the_a-cat_is-savege'
'''
long = len(a)
li = []

for i in range(long):
    if i == 0 and a[i]!='t':
        li.append(a[0].title())
    elif a[i] == '-' or a[i] == '_':
        big = a[i+1].title()
        li.append(big)
    elif a[i-1] != '-' and a[i-1] != '_':
        li.append(a[i])
        print(a[i-1])

b = ''
for i in li:
    b +=i

print(b)
'''
 
def to_camel_case(s):
    return s[0] + s.title().translate(None,"-_")[1:] if s else s


r = to_camel_case('the_a-cat_is-savege')
print(r)
