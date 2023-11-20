#program to solve the Fractional Knapsack problem using a greedy method:
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    knapsack = []

    for item in items:
        if capacity >= item.weight:
            knapsack.append((item.weight, item.value))
            total_value += item.value
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            knapsack.append((capacity, item.value * fraction))
            total_value += item.value * fraction
            break

    return knapsack, total_value

if __name__ == "__main__":
    # Example usage
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    knapsack_capacity = 50

    result, total_value = fractional_knapsack(items, knapsack_capacity)

    print("Selected items in the knapsack:")
    for weight, value in result:
        print(f"Weight: {weight}, Value: {value}")

    print("Total value in the knapsack:", total_value)
