n = 13  # 1101
i = 2
'''
so i will left shift 1 by n places, and XOr the whole thing, so on the particular ith bit if:

ith bit scenario:
    - if bit = 0, 0^1 = 1
    - if bit = 1, 1^1 = 0
non ith bits:
    - if bit = 0, 0^0 = 0
    - if bit = 1, 0^1 = 1
'''

leftshiftedone = 1 << i

print(f"bit is toggled now and {n} is now : {n ^ leftshiftedone}")