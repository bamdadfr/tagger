def replaceCommas(string):
    return string.replace(',', ';')


def arrayToString(array):
    if array is None: return 'TO_FILL'
    
    string = ''
    splitter = '; '
    isFirst = True

    for element in array:
        if isFirst:
            isFirst = False
            string += element
        else:
            string += splitter + element
    
    string = replaceCommas(string)

    return string
