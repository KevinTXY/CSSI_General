# Kevin Taha
# 10/30/2018
# Comments: Still trying to teach myself O notation so my statements might not be correct here.
# Would love to be corrected if they aren't.


# One line pythonic solution. Both methods used are O(n) so this won't be great
# for huge data sets.
def find_max_idx_v0(input):
    return input.index(max(input))


# Faster method. Essentially a binary search so runtime should be about O(logn), which would massively
# improve runtime for very large data sets. Assumed that array is always increasing or decreasing
# so that the same number is never successively displayed.
def find_max_idx(arrin):
    arrlen = len(arrin) #len is constant time
    # Quickly handle our two major corner cases that stand in this prompt.
    if(arrlen == 1):
        return 0
    if(arrlen == 2):
        if(arrin[0] > arrin[1]):
            return 0
        else:
            return 1
    # Search algorithm that takes advantage of the array's sorting.
    i = arrlen / 2
    while(True):
        if((i == 0) or (i == arrlen - 1) or (arrin[i + 1] < arrin[i]) and (arrin[i - 1] < arrin[i])):
            return i
        else:
            if(arrin[i + 1] > arrin[i]):
                i = (arrlen + i) / 2
            elif(arrin[i + 1] < arrin[i]):
                i /= 2
            else:
                return - 1


print(find_max_idx([1,2,3,2,1,0]))
