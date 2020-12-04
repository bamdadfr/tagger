# components
from env import *
from utils_replace_commas import UtilsReplaceCommas

def UtilsArrayToString(array):
    if array is None: return ENV_TAGGING_TODO
    
    string = ''
    splitter = '; '
    isFirst = True

    for element in array:
        if isFirst:
            isFirst = False
            string += element
        else:
            string += splitter + element
    
    string = UtilsReplaceCommas(string)

    return string
