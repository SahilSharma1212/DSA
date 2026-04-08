factors = set()

num = 36

i = 2

while i*i <= 36:
    if 36%i == 0:
        factors.add(i)
        factors.add(36//i)
    i = i + 1

factlist = list(factors)
print(factlist)