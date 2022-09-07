# actual result - ["FirstItem", "FriendsList", "MyTuple"]
# expected result -["first_item", "friends_list", "my_tuple" ]
camel_format = ["FirstItem", "FriendsList", "MyTuple"]
snake_format = []
for word in camel_format:
     new_word = word
     for i in range(len(word)):
          if word[i].isupper():
             if i==0:
                 new_word = new_word.replace(word[i], word[i].lower())
             else:
                  new_word = new_word.replace(word[i],"_" +  word[i].lower())
    snake_format.append(new_word)
print(snake_format)