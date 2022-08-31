import re


def find_name(arr_names, arr_compare):
    result = []
    for name in arr_names:
        if name.lower().strip() in arr_compare:
            result.append(name.strip())
    return result


def crop_ids(arr):
    result = []
    for i in arr:
        result.append(i.replace("id=\"", "").replace("\"", ""))
    return result


def crop_href(arr):
    result = []
    for href in arr:
        result.append(href.replace("href=\"", "").replace("\"", ""))
    return result


def find_domain(arr):
    result = []
    for i in arr:
        if i.startswith("www."):
            result.append(i.replace("www.", ""))
        elif re.search(r"/.*[a-zA-Z]", i):
            result.append(re.sub(r"/.*[a-zA-Z]", "", i))
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    temp = open("index.html", "r").read()

    find_id = crop_ids(re.findall(r"id=\"[a-z]+\"", temp))
    find_names = find_name(re.findall(r"\.*[a-zA-Z0-9]{2,20}\.*[a-zA-Z0-9]{2,20}\s", temp), find_id)
    find_links = crop_href(re.findall(r"href=\".*\"", temp))
    find_domains = find_domain(re.findall(r"[a-zA-Z0-9]{2,20}\..*[a-zA-Z0-9]{2,20}", temp))

    result_1 = []
    result_2 = []
    for element in range(len(find_id)):
        result_1.append((
            find_id[element],
            find_links[element],
            find_names[element]
        ))
        result_2.append((
            find_id[element],
            find_domains[element],
            find_names[element]
        ))
    print(result_1)
    print(result_2)
