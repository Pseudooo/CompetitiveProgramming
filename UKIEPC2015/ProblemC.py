# ====== COLLECT INPUTS

# n quantity represents the amount of messages
n = int(input())

# MsgFreq dict contains frequency of occurence of each message
MsgFreq = {}

# Dictionary to contain message sets for each user
UserMessages = {}

for i in range(n):
    msg = input().split()
    
    # Increase the given word's frequency
    for word in msg[1:]:
        if word in MsgFreq.keys():
            MsgFreq[word]+=1
        else:
            # Init key
            MsgFreq[word] = 1
            
    user = msg[0] 
    MsgSet = set(msg[1:])
    
    if user in UserMessages.keys():
        # Extend current set to include any new messages
        UserMessages[user] = set.union(UserMessages[user], MsgSet)
    else:
        # init key
        UserMessages[user] = MsgSet
    
# Now we look at the intersection of messages between sets
SharedMessages = list(set.intersection(*[UserMessages[a] for a in UserMessages.keys()]))

# Check if the shared messages list is empty, if so edge case ALL CLEAR
if SharedMessages == []:
    print("ALL CLEAR") # No shared messages between users
else:
    # Not empty
    
    # Sort based on frequency
    SharedMessages.sort(key=lambda a : MsgFreq[a], reverse=True)
    
    # Now sort the sections that share the same frequency
    x=0
    for i,word in enumerate(SharedMessages):
        if MsgFreq[word] != MsgFreq[SharedMessages[x]]:
            
            left = SharedMessages[:x] # Break the list to allow the part that requires sorted to be sorted
            toSort = SharedMessages[x:i]
            right = SharedMessages[i:]
            
            # Sort
            toSort.sort()
            
            # Reconstruct list to contain sorted section
            SharedMessages = left+toSort+right
            
            x = i
    
    [print(msg) for msg in SharedMessages]
    
    
    
    