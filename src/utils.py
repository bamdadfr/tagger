def arrayToString(array):
    string = ''
    if array is None: return string
    
    splitter = '; '
    isFirst = True

    for element in array:
        if isFirst:
            isFirst = False
            string += element
        else:
            string += splitter + element

    return string
