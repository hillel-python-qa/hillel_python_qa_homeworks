my_list_of_items = ["BMW", "Bugatti", "Volkswagen", "Mercedes"]
my_list_of_items2 = ["", "Bugatti", "Volkswagen", "Mercedes"]
my_list_of_items3 = [10, 20, 30, ]

if __name__ == "__main__":
    def my_all(items: str | int) -> str | int:
        output = True
        for item in items:
            if not item:
                output = False
                break
        return output

print(my_all(my_list_of_items))
print(my_all(my_list_of_items2))
print(my_all(my_list_of_items3))
