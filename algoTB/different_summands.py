def find_maximum_k(n):
    summands = []
    current_sum = 0
    current_number = 1
    
    while current_sum + current_number <= n:
        summands.append(current_number)
        current_sum += current_number
        current_number += 1
    
    # Adjust the last number if the sum is not exactly n
    if current_sum < n:
        summands[-1] += (n - current_sum)
    
    return summands

if __name__ == '__main__':
    n = int(input())
    result = find_maximum_k(n)
    print(len(result))
    print(' '.join(map(str, result)))