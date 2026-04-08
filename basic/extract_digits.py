n = 5873
nnum = 0
while n > 0:
    rem = n % 10
    nnum = nnum* 10 + rem
    n = n // 10
print(nnum)