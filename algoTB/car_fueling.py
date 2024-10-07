def min_refills(distance, tank, stops):
    # Add start (0) and end (distance) to the list of stops
    stops = [0] + stops + [distance]
    
    num_refills = 0
    current_position = 0
    
    while current_position < len(stops) - 1:
        last_refill_position = current_position
        
        # Move to the furthest reachable stop
        while (current_position < len(stops) - 1 and
               stops[current_position + 1] - stops[last_refill_position] <= tank):
            current_position += 1
        
        # If no progress is made, it means the next stop is unreachable
        if current_position == last_refill_position:
            return -1
        
        # If we haven't reached the last stop, we need a refill
        if current_position < len(stops) - 1:
            num_refills += 1
    
    return num_refills

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    d = int(data[0])
    m = int(data[1])
    n = int(data[2])
    stops = list(map(int, data[3:3 + n]))
    
    result = min_refills(d, m, stops)
    print(result)