def max_dot_product(prices, clicks):
    # Sort both sequences
    prices.sort()
    clicks.sort()
    
    # Calculate the dot product
    max_product = sum(p * c for p, c in zip(prices, clicks))
    
    return max_product

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    prices = list(map(int, data[1:n+1]))
    clicks = list(map(int, data[n+1:2*n+1]))
    
    result = max_dot_product(prices, clicks)
    print(result)
