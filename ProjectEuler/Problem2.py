import math as m
import time

now = time.time()

# Get the nth term of the fibonacci sequence
def getTerm(n:int):
    return int((1 / 5**.5)*(((1+5**.5)/2)**n-((1-5**.5)/2)**n))

# Get the index of a given number
def getIndex(f:int):
    return m.ceil(m.log((f-0.5)*5**.5)/m.log((1+5**.5)/2))

# Collect the limit and calculate the maximum n
limit = int(input())
maxN = getIndex(limit)

total = 0

# Iterate in steps of 3 to only get even numbers
for i in range(3,maxN,3):
    total+=getTerm(i)

# Timer to compare with brute force solution
delayed = time.time() - now
    
print("Sum:",total)
print("Took: "+str(delayed)+"s")
