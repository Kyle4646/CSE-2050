'''
Task: Write a function longest_prefix that takes in a list of words and returns the longest prefix they all share
Specifics:
- The list will be called words and will be a list of strings
- Prefixes are the beginning part of words
- Essentially, I'm asking you to find how many characters from the start of a string in the list do they all share
- Eg. ["greed", "great", "green"] => "gre"
'''

def longest_prefix(words):
    if not words:
        return ""

    prefix = ""

    for i in range(len(words[0])): # i is index of each character of one word
        for j in range(1, len(words)): # j is index of every other word in list
            # check if false
            if i >= len(words[j]):
                return prefix

            if words[j][i] != words[0][i]:
                return prefix
        
        prefix += words[0][i]

    return prefix