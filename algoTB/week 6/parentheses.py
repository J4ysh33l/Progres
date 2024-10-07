def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def maximum_value(expression):
    digits = []
    operations = []

    for i in range(len(expression)):
        if i % 2 == 0:
            digits.append(int(expression[i]))
        else:
            operations.append(expression[i])

    n = len(digits)
    
    dp_min = [[0] * n for _ in range(n)]
    dp_max = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp_min[i][i] = digits[i]
        dp_max[i][i] = digits[i]
    
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_val = float('inf')
            max_val = float('-inf')
            for k in range(i, j):
                a = evaluate(dp_max[i][k], dp_max[k + 1][j], operations[k])
                b = evaluate(dp_max[i][k], dp_min[k + 1][j], operations[k])
                c = evaluate(dp_min[i][k], dp_max[k + 1][j], operations[k])
                d = evaluate(dp_min[i][k], dp_min[k + 1][j], operations[k])
                
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
            
            dp_min[i][j] = min_val
            dp_max[i][j] = max_val
    
    return dp_max[0][n - 1]

if __name__ == "__main__":
    import sys
    input_expression = sys.stdin.read().strip()
    print(maximum_value(input_expression))