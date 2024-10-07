import sys

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

def fibonacci_partial_sum(from_, to):
    if to < from_:
        return 0

    sum_to = (fibonacci_huge(to + 2, 10) - 1) % 10
    sum_from = (fibonacci_huge(from_ + 1, 10) - 1) % 10

    result = sum_to - sum_from
    if result < 0:
        result += 10

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))