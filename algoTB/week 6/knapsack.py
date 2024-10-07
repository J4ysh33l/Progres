def maximum_gold(capacity, weights):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + weights[i-1])

    return dp[n][capacity]

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    capacity = data[0]
    n = data[1]
    weights = data[2:]
    assert len(weights) == n

    print(maximum_gold(capacity, weights))