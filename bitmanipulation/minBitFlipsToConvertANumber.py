'''
    10 - 1010
    7  - 0111
    XOR KARNE SE BIT FLIP HOTE HAI
    - DO XOR
    - FIND NUMBER OF ONES
'''

start = 3
goal = 4

print(bin(start ^ goal)[2:].count("1"))