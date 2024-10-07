def get_max_value(capacity, weights, values):
    # Calculate value to weight ratio
    items = []
    for i in range(len(weights)):
        if weights[i] != 0:
            items.append((values[i] / weights[i], weights[i], values[i]))

    # Sort items by value to weight ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    for value_per_weight, weight, value in items:
        if capacity == 0:
            break
        amount = min(weight, capacity)
        total_value += amount * value_per_weight
        capacity -= amount
    
    return total_value

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    capacity = int(data[1])
    
    weights = []
    values = []
    for i in range(n):
        values.append(int(data[2 + 2*i]))
        weights.append(int(data[2 + 2*i + 1]))
    
    max_value = get_max_value(capacity, weights, values)
    print(f"{max_value:.4f}")