def maxProfit(stocks):
    max_profit = 0

    for i in range(1, len(stocks)):
        if stocks[i] > stocks[i - 1]:
            max_profit += stocks[i] - stocks[i - 1]

    return max_profit


# Test the function
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 7
