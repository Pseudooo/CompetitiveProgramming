'''
Conversation Log:

This problem features an integer input of n which includes the number of
messages that have been sent in total, each message is sent by a user and
the goal of this problem is to identify all of the messages that are shared
between all of the n messages.

All of these shared messages should then be outputted in alphabetical order,
in the instance of a tie however they should be ordered in terms of which
was the most frequent.

'''

# ====== COLLECT INPUTS

# n quantity represents the amount of messages
n = int(input())

# A list of n messages that have been sent
Messages = []

for i in range(n):
    Messages.append(input().split())

# ====== PROCESS

# MsgFreq dict contains frequency of occurence of each message
MsgFreq = {}

UserMessages = {}

for msg in Messages:
    
    # First build the frequency dictionary
    for wrd in msg[1:]:
        if wrd in MsgFreq.keys():
            # Increase index
            MsgFreq[wrd]+=1
        else:
            # If doesn't exist initialize
            MsgFreq[wrd] = 1
    
    user = msg[0] # First word will always be user
    MsgSet = set(msg[1:])
    
    if user in UserMessages.keys():
        # Union is a method of appending to curret set
        UserMessages[user] = set.union(UserMessages[user], MsgSet)
    else:
        
        UserMessages[user] = MsgSet
    
# Now we look at the intersection of messages between sets
SharedMessages = list(set.intersection(*[UserMessages[a] for a in UserMessages.keys()]))

# Check if the shared messages list is empty, if so edge case ALL CLEAR
if SharedMessages == []:
    print("ALL CLEAR") # No shared messages between users
else:
    # Not empty
    
    # Now sort shared messages by message frequency
    SharedMessages.sort() # Sort alphabetically first
    
    # Sort based on frequency
    SharedMessages.sort(key=lambda a : MsgFreq[a], reverse=True)
    
    [print(msg) for msg in SharedMessages]
    
    
    
    