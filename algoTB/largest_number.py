from functools import cmp_to_key

def largest_number(numbers):
    # Custom comparison function
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    # Convert numbers to strings for concatenation
    numbers = list(map(str, numbers))
    
    # Sort numbers using the custom comparison function
    numbers.sort(key=cmp_to_key(compare))
    
    # Concatenate the sorted numbers
    largest_num = ''.join(numbers)
    
    # To handle the case where there are leading zeros (e.g., [0, 0])
    return '0' if largest_num[0] == '0' else largest_num

if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(largest_number(numbers))