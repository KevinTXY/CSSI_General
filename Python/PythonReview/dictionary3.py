# snacks = {
#     'fruit snacks' : 10,
#     'apples' : 7,
#
# }
# my_list = ["ravenswood", "bucktown"]
# # for item in my_list:
# #     print item
#
# snacks["raisins"] = 2
#
# for item in snacks:
#     if item == "raisins":
#         snacks["raisins"] = 8
#     print ("%s get a %i out of 10") % (item, snacks[item]
snacks = {}
while True:
    snack = raw_input("Enter your snack here. Enter 'stop' to stop adding entries: ")
    if snack != ('stop' or 'Stop' or 'STOP'):
        rating = raw_input("What is your rating? ")
        snacks[snack] = int(rating)
    else:
        break
print snacks
