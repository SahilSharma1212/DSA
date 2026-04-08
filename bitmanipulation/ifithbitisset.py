a = 13
i = 2

# leftshift 1
leftshiftedOne = 1<<i

print("it is not set") if a & leftshiftedOne == 0 else print("It is Set")