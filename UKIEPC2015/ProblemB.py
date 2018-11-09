'''

Mountain Biking:

This problem features finding the speed of a cyclist as he reaches the
end of the ith segment (there are n line segments). The bike will initially
start from a stationary position. The outputs are then the speed of the bike
at the end of each of the n segments.

'''

n,g = [int(a) for a in input().split()]

Segments = []

for i in range(n):
    s,theta = [int(b) for b in input().split()]
    Segments.append((s,theta))
    

