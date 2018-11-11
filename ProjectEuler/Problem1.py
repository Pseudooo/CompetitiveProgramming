'''

I have modified this problem a little bit for my own entertainment
instead of having it calculate the sum for the first set to 1000
I instead would like to make an efficient way to calculate the sum
for some arbitrary interger that is defined by the user

'''

# n-1 because we don't want to include our bound
n = int(input())-1

# Going to use 3 arithmetic series' to calculate the sum
biggest3n,biggest5n,biggest15n = -1,-1,-1

for i in range(15):
    
    # We can't have negative terms (Not natural)
    if n-i < 0:
        break
    
    # Work backwards from upper bound to find largest of each multiple
    # calculate n of term in sequence
    if (n-i) % 3 == 0 and biggest3n == -1:
        biggest3n = (n-i) // 3
    
    if (n-i) % 5 == 0 and biggest5n == -1:
        biggest5n = (n-i) // 5
        
    if (n-i) % 15 == 0:
        biggest15n = (n-i) // 15
        break

sum1 = (biggest3n/2) * (6+(biggest3n-1)*3) # sum of all threes in bound
sum2 = (biggest5n/2) * (10+(biggest5n-1)*5) # sum of all fives in bound
sumOfConflicts = (biggest15n/2) * (30+(biggest15n-1)*15) # sum of all 15s (Conflicts)
total = int(sum1+sum2-sumOfConflicts) # Calculate total

print("Sum: {0}".format(total))