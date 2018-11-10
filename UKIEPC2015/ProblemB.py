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