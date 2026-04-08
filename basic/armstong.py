num = 153

isArmstrong = True
num2 = num
sum = 0
while num > 0:
    sum = sum + ((num%10)*(num%10)*(num%10))
    num = num // 10

print(num2 == sum)