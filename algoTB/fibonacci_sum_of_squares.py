def get_pisano_period_length(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_huge(n, m):
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

def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    fn = fibonacci_huge(n, 10)
    fn_plus_1 = fibonacci_huge(n + 1, 10)

    return (fn * fn_plus_1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))