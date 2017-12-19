# Kevin Taha
# 10/24/ 2017

# Checks count of left parentheses and makes sure that each one is closed properly.
def is_string_balanced(message):
    parenthcount = 0
    for i in message:
        if i == "(":
            parenthcount += 1
        elif i == ")":
            if parenthcount == 0:
                return False
            else:
                parenthcount -= 1
    if (parenthcount != 0):
        return False
    return True

message = raw_input()
print is_string_balanced(message)
