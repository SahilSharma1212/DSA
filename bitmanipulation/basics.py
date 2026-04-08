num = 31

binform = bin(num)[2:]
print(binform)

num2 = 22
# 10110
# 11111

# AND - 10110
print(f"AND - {num & num2}")
# XOR - 01001
print(f"XOR - {num ^ num2}")
# RIght SHIFT - 
print(f"RSHIFT - {num >> 1}")
# Left SHIFT - 
print(f"LSHIFT - {num << 1}")