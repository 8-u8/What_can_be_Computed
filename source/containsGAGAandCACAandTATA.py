
#%%
from containsGAGA import *

#%%
def containsGAGAandCACAandTATA(inString):
    if containsGAGA(inString) == 'yes' and\
        containsCACA(inString) and\
            containsTATA(inString):
        return 'yes'
    else:
        return 'no'


#%%
def containsCACA(searchString):
    return containsSubstring(searchString, 'CACA')


def containsTATA(searchString):
    return containsSubstring(searchString, 'TATA')

#%%
def containsSubstring(searchString, subString):
    if subString in searchString:
        return True
    else:
        return False

#%%
