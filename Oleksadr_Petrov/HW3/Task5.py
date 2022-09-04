vip_guests = ["Minodora Áurea", "Itoro Alban", "Gabriella Emil", "Sigmund Govinda"]
common_guests = ["Ivan Ivanov", "Oleg Petrov", "Sergey Smirnov", "Egor Letov", "Vitaliy Sidorov"]
vip_places = {
                1: vip_guests.pop(),
                2: vip_guests.pop(),
                3: vip_guests.pop(),
                4: vip_guests.pop()
             }
common_places = {
                   1: common_guests.pop(),
                   2: common_guests.pop(),
                   3: common_guests.pop(),
                   4: common_guests.pop(),
                   5: common_guests.pop(),
                   6: None,
                   7: None,
                   8: None
             }

print(vip_places)
print(common_places)
