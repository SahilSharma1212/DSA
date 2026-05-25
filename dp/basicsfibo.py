n = int(input("Enter a number:"))

dp = [-1]*(n+1)

def fiboDP(n):
    if n == 1 or n == 0:
        return n
    
    if dp[n] == -1:
        curr = fiboDP(n-1) + fiboDP(n-2)
        dp[n] = curr
        return curr
    else:
        return dp[n]

print(f"Answer is : {fiboDP(n)}")