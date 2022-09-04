casino_blacklist = ["Minodora Áurea", "Itoro Alban", "Gabriella Emil", "Sigmund Govinda"]
poker_blacklist = ["Minodora Áurea", "Itoro Alban", "Shaquille Rahma", "Oleksander Cenric"]
alcohol_blacklist = ["Minodora Áurea", "Itoro Alban", "Shaquille Rahma", "Colm Eutychos"]

result = set(casino_blacklist) & set(poker_blacklist) & set(alcohol_blacklist)
print(result)
