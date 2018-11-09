'''

Mountain Biking:

This problem features finding the speed required of a cyclist to reach the
top of the mountain without walking. Therefore the speed required of the 
cyclist at the start of each segment must be calculated in a way that allows
for them to reach the top.

Solution:

In order to make things a bit easier to calculate we're going to reverse things
and imagine that they start at the top of the hill with speed 0 and calculate
the velocity of the cyclist as they reach the end of each segment. This can be
done much easier using v^2=u^2+2as (SUVAT) equation. So we start by collecting
all of the required inputs, we then reverse the order of the list of segments
inputted and iterate through the new list. At each iteration we can calculate
the final velocity of the cyclist given a=g*cos(theta) and s is given for the
segment. u is just our previous velocity which is initially 0. At the end we 
simply reverse the order of v again and print it.

'''

import math as m

# Collect the n number of segments and gravitational constant g.
n,g = input().split()
n,g = int(n),float(g)

# List of tuples containing the segment length and angle
Segments = []

for i in range(n): # Build list
    s,theta = [int(b) for b in input().split()]
    Segments.append((s,theta))

# Reverse order of segments to make problem easier
Segments = Segments[::-1]

# Vel list and the previos velocity list
vels = []
lastVel = 0 # We start from rest so 0

# Iterate through each segment to calculate velocity
for s,theta in Segments:
    vel = 0.0
    # v=sqrt(u^2+2as)
    vel = (lastVel**2 + 2*g*m.cos(m.radians(theta))*s)**.5
    
    vel = vel.__round__(6)
    lastVel = vel # Update the previos vel for next iteration
    vels.append(vel) # Append vel

# Print velocity list backwards     
[print(vel) for vel in vels[::-1]]