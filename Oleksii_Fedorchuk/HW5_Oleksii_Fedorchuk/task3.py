if __name__ == "__main__":
    tsk = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
    change = tsk.strip().replace("=sssss", "").split("&")
    dct = {}
    for items in change:
        if items.find("=") > 0:
            spt = items.split("=")
            dct.update({spt[0]: spt[1]})
    print(dct)
