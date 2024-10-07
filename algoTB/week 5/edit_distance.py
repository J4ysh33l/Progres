def edit_distance(first_string, second_string):
    m, n = len(first_string), len(second_string)
    
    # Create a (m+1)x(n+1) matrix to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 1)  # Substitution
    
    return dp[m][n]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    first_string = data[0]
    second_string = data[1]
    print(edit_distance(first_string, second_string))