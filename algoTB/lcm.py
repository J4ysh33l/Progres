from math import gcd

def lcm(a, b):
    """Calculate the lowest common multiple of 2 int's: a, b using `gcd()`."""
    return a * b // gcd(a, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))