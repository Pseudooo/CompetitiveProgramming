import math as m
import bisect as b

# Hard consonants, a word must start with these
hardConsonants = [ord(l) for l in "bcdgknpt"]
# Hard Endings, any word ending in a hard consonant will be replaced
# Hard endings are always an "a", "o" or "u" followed by a "h"
hardEndings = [ord(l) for l in "aou"]

# Makes a list of words from the input
words = input().split()
words = [list(w) for w in words]

# Stores a list of nimionese words
final = []

# Helper function to return the closest value to a number in a list
def getClosest(list, val):
    pos = b.bisect_left(list, val)
    # Check which is closest
    if pos == 0:
        return list[pos]
    if pos == len(list):
        return list[pos-1]
    if val-list[pos-1] <= list[pos]-val:
        return list[pos-1]
    return list[pos]

# Loop through every word
for w in words:
    # Convert the first letter of the word to a hard consonant
    startLetter = chr(getClosest(hardConsonants, ord(w[0].lower())))

    w[0] = w[0].isupper() and startLetter.upper() or startLetter

    # Create a list of cyllables
    cyllables = "".join(w).split("-")
    cyllables = [list(c) for c in cyllables]

    # Loop through every cyllable aside from the first
    for i in range(len(cyllables[1:])):
        c = cyllables[i+1]
        # Check every letter for being a hard consonant
        for l in range(len(c)):
            if ord(c[l].lower()) in hardConsonants:
                c[l] = c[l].isupper() and startLetter.upper() or startLetter

    # Add ending to the last cyllable
    if ord(cyllables[-1][-1].lower()) in hardConsonants:
        endLetter = chr(getClosest(hardEndings, ord(cyllables[-1][-1].lower())))

        cyllables[-1].append(endLetter)
        cyllables[-1].append("h")

    # Combine cyllables back into a word
    final.append( str().join([str().join(i) for i in cyllables]) )


# Print out the final words
print(" ".join(final))
