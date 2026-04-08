# left shift 1 by n places, calc its 1's compliment, do the or with the main number

n = 13
i = 2
# 9 is 1001
# so - 
leftShiftedOne = 1<<i
# 1's compliment
leftShiftedOne = ~leftShiftedOne
print(f"bit is cleared now and {n} is now : {n & leftShiftedOne}")