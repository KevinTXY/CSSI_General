# Finds median values in x and y components of all coordinates respectively.
# Only two directions to worry about, which allows this to work.
# Other solutions I tried involved iterating over a boxed range and using the
# mean values, but this should be far more efficient.
def find_meeting_point(coords):
    xarr, yarr = [], []
    for i in coords:
        xarr.append(i[0])
        yarr.append(i[1])
    return(median(xarr), median(yarr))
# Returns median of an array since Python2.7 doesn't have a non-numpy way to do this
def median(arr):
    arr.sort()
    if len(arr) % 2: #Evaluates to true if not 0
        return arr[(len(arr)) / 2]
    return (arr[(len(arr)) / 2] + arr[(len(arr)) / 2 - 1]) / 2
