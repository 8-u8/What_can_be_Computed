#%%
import utils
# from utils import rf

def countLines(inString):
    lines = inString.split('\n')
    return str(len(lines))

#%%
def longestWord(inString):
    words = inString.split()
    longest = ''
    lengthOfLongest = 0
    for word in words:
        if len(word) > lengthOfLongest:
            longest = word
            lengthOfLongest = len(word)
    return longest