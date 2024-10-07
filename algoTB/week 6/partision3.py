from sys import stdin

def partition3(values):
    total_sum = sum(values)
    
    if total_sum % 3 != 0:
        return 0
    
    target_sum = total_sum // 3
    n = len(values)
    
    dp = [[[False] * (target_sum + 1) for _ in range(target_sum + 1)] for _ in range(n + 1)]
    dp[0][0][0] = True

    for i in range(1, n + 1):
        num = values[i - 1]
        for j in range(target_sum + 1):
            for k in range(target_sum + 1):
                dp[i][j][k] = dp[i-1][j][k]
                if j >= num:
                    dp[i][j][k] = dp[i][j][k] or dp[i-1][j-num][k]
                if k >= num:
                    dp[i][j][k] = dp[i][j][k] or dp[i-1][j][k-num]

    return 1 if dp[n][target_sum][target_sum] else 0

if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))