def cover_segments(segments):
    # Sort segments by their right endpoint
    segments.sort(key=lambda x: x[1])
    
    points = []
    current_point = None
    
    for segment in segments:
        if current_point is None or segment[0] > current_point:
            current_point = segment[1]
            points.append(current_point)
    
    return points

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    segments = []
    index = 1
    for i in range(n):
        l = int(data[index])
        r = int(data[index + 1])
        segments.append((l, r))
        index += 2
    
    points = cover_segments(segments)
    print(len(points))
    print(' '.join(map(str, points)))