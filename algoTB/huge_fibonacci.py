def get_pisano_period_length(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        # Pisano period always starts with 0, 1
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_huge_optimized(n, m):
    if n <= 1:
        return n

    pisano_period_length = get_pisano_period_length(m)
    n = n % pisano_period_length

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_optimized(n, m))