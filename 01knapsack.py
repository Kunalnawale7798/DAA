#Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and 
#bound strategy.
def knapsack_0_1(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstructing the solution
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    knapsack_capacity = 50

    max_value, selected_items = knapsack_0_1(values, weights, knapsack_capacity)

    print("Maximum value:", max_value)
    print("Selected items:", selected_items)
