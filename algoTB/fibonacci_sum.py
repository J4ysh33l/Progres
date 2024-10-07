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

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fibonacci_sum(n):
    if n <= 1:
        return n

    # Sum of first n Fibonacci numbers is F(n+2) - 1
    n_plus_2_fib = fibonacci_huge(n + 2, 10)
    sum_fib = n_plus_2_fib - 1

    # Since we are interested in the last digit
    return sum_fib % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))