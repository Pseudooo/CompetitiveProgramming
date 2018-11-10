#  Solution Descriptions

## Problem B
Initial Problem can be found [here](https://open.kattis.com/problems/mountainbiking)

Now, the wording of this problem was felt to be very misleading at first but can be quickly realised that the bike(s) in the question are travelling up the hill rather than down. The velocities that are given are the required of the speed at the begining of the given segment such that no work is required to move up the hill from the bottom.

This problem can be made much easier by thinking of it backwards. If we reverse the order of the segments that are given then we have an array containing the segments starting from the top of the mountain. Using an equation of motion (v^2=u^2+2as) we can calculate the speed of the bike at the end of the segment whilst taking into account their previous velocity. Now doing this whilst iterating through our reversed array of segments allows us to calculate it much easier. We simply print the elements of the resultant velocities list backwards.


## Problem C
Initial Problem can be found [here](https://open.kattis.com/problems/conversationlog)

With this problem it's a large application of sets. The first input is an integer, n, that tells us the number of messages that have been sent. The following n lines are then each message, the first word of each message is always the sending user. Our first goal is to find a list of words that have been said by every user in the chat at least once. Sets in python can be applied very nicely for this solution.

First we want to convert the data into a different form, the form we used for this solution was two dictionaries, one with a key of the given user's name and the value being a set of words sent by them. The second dictionary tracks the frequency of each word that is sent in a message, so the key is the given word and the value is an integer representing the number of times it has been sent.

Once these new dataforms are built we want to find the messages that are shared, which is accomplished in a single line within python by taking the intersection of all the sets contained in the dictionary of the users words. With this list of shared messages we simply want to sort by their frequency of occurence and sort ones that share a frequency alphabetically.
