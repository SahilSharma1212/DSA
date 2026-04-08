def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):

        if prices[i] < min_price:
            min_price = prices[i]

        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)

    return max_profit

print(int(maxProfit([7,1,5,3,6,4])))