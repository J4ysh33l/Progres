def binary_search(keys, query):
    left = 0
    right = len(keys) - 1
    while right >= left:
        middle = (left + right) // 2
        if keys[middle] == query:
            return middle
        elif keys[middle] < query:
            left = middle + 1
        else:
            right = middle - 1
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    results = []
    for q in input_queries:
        results.append(binary_search(input_keys, q))
    
    print(' '.join(map(str, results)))