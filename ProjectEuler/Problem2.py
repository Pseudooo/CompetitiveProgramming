import math as m
import time

# Values of phi precalculated for iteration approache's speed
PhiCubed = 2+5**.5
NegPhiNegCube = 2-5**.5
Root5 = 5**.5

Phi = (1+5**.5)/2

# Get the nth term of the fibonacci sequence
def getTerm(n:int): # This function is used for closed form
    return int((Phi**n-(-Phi)**(-n))/Root5)

# Return the nth even term of the fibonacci sequence
def getEvenTerm(n:int):
    return int((PhiCubed**n-NegPhiNegCube**n)/Root5)

# Get the index of a given number
def getIndex(f:int):
    return m.ceil(m.log((f-0.5)*5**.5)/m.log((1+5**.5)/2))

# Collect the limit and calculate the maximum n
maxN = getIndex(int(input())) // 3

now = time.time() # Time the calculation

total = 0

# Iterate through each even term
for i in range(1,maxN+1):
    total+=getEvenTerm(i)

total2 = float((1/Root5)*(((1-PhiCubed**(maxN+1))/(1-PhiCubed))-((1-NegPhiNegCube**(maxN+1))/(1-NegPhiNegCube)))) # Geometric sums

total3 = float((getTerm(maxN*3+2)-1)/2) # Closed form sum

total2,total3 = int(total2),int(total3)

# Timer to compare with brute force solution
delayed = time.time() - now
    
print("Sum 1: {0:>10}".format(total))
print("Sum 2: {0:>10}".format(total2))
print("Sum 3: {0:>10}".format(total3))

print("Took: {0:.10f}s".format(delayed))
