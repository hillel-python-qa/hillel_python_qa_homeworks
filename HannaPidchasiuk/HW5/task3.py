# there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: euro}

if __name__ == "__main__":
    a = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
    a_pairs = a.strip().replace("=sssss", "").split("&")
    a_dict = {}
    for pair in a_pairs:
        if pair.find("=") > 0:
            temp = pair.split("=")
            a_dict.update({temp[0]: temp[1]})
    print(a_dict)
