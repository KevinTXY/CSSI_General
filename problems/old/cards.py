def everyone_sign(names):
    namedict = {}
    for i in names:
        namedict[i] = "Thank You! Your friends"
        for j in names:
            if j != i:
                namedict[i] += ", " + j
    return namedict
