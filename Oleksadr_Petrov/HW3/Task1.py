def company_takeover(takin, taken):
    takin.extend(taken)
    taken.clear()


eleks = ["Ivan Ivanov", "Oleg Petrov", "Sergey Smirnov", "Egor Letov", "Vitaliy Sidorov"]
toshiba = ["Minodora Áurea", "Itoro Alban", "Shaquille Rahma", "Oleksander Cenric", "Ivan Ivanov"]
company_takeover(toshiba, eleks)
print("New Toshiba: ", toshiba)
print("New Eleks: ", eleks)
