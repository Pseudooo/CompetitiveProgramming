#  Solution Descriptions

## Problem C
Problem C was largely solved using sets, in attempting to solve it the idea of efficiency was kept in mind.

First we collected the inputs that were to be provided these were:
- n _The amount of messages that are to be entered_
- n * Message Lines _The message that was sent, each message will lead with the sender's name_

From an array containing the messages a dictionary was built containing all of the frequencies of each message that has been sent across all users and also a dictionary that contains the set of message(s) sent by each user. This allowed us to use the intersection functionality of sets to find all messages that are shared between all users. The set of messages shared between all users is simply the intersection of all sets from each user that we defined in our dictionary.

The list was then sorted alphabetically.

Lambda was then used to sort the list based on the frequency of each message being sent.
