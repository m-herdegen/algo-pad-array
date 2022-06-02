#REMEMBER TO PSEUDOCODE
def pad(array, min_size, value = None):
    # find the difference between the current size and the minimum size
    padding = len(array) - min_size
    # if the current size is less than the minimum size
    if padding < 0:
        while padding:
            # add padding to the answer array
            array.append(value)
            padding+=1
    
    return array
