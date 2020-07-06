def arrayToString(array):
    string = ''
    
    splitter = '; '
    isFirst = True

    for element in array:
        if isFirst:
            isFirst = False
            string += element
        else:
            string += splitter + element

    return string
