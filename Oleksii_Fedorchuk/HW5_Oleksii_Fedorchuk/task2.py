friends = ["John", "Marta", "James", "Amanda", "Marianna"]
title_string = ' Names '
print(f"{title_string}".center(50, "*"))
for friend in friends:
    print(friend.rjust(27))

# Option 1
# print(f"{friends[0].rjust(27)}")
# print(f"{friends[1].rjust(27)}")
# print(f"{friends[2].rjust(27)}")
# print(f"{friends[3].rjust(27)}")
# print(f"{friends[4].rjust(27)}")

# Option 2
# for names in friends:
#     print(f"{friends[0]}".rjust(27))
#     print(f"{friends[1]}".rjust(27))
#     print(f"{friends[2]}".rjust(27))
#     print(f"{friends[3]}".rjust(27))
#     print(f"{friends[4]}".rjust(27))
#     break
