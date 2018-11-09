'''

Mountain Biking:

This problem features finding the speed of a cyclist as he reaches the
end of the ith segment (there are n line segments). The bike will initially
start from a stationary position. The outputs are then the speed of the bike
at the end of each of the n segments.

'''

import math as m

n,g = [int(a) for a in input().split()]

Segments = []

for i in range(n):
    s,theta = [int(b) for b in input().split()]
    Segments.append((s,theta))

Segments = Segments[::-1]
vels = []
lastVel = 0
for s,theta in Segments:
    vel = 0.0
    vel = (lastVel**2+(2*g*m.cos(m.radians(theta))*s))**.5
    vel = vel.__round__(6)
    lastVel = vel
    vels.append(vel)
    
vels = vels[::-1]
    
[print(vel) for vel in vels]