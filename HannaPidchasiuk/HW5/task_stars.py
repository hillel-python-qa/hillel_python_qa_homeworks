import re

if __name__ == "__main__":
    temp = ''
    find_id = re.findall(r"id=\"[a-z]+\"", temp)
    find_href = re.findall(r"href=\".*\"", temp)
    find_name = re.findall(r"", temp)
    find_domain = re.findall(r"", temp)
#\B\".*.com
#(([A-Za-z0-9]+)\.).*[a-z]
    result_1 = []
    result_2 = []
    for id_i, href, name, domain in find_id, find_href, find_name, find_domain:
        result_1.append((
            id_i.replace("id=\"", "").replace("\"", ""),
            href.replace("href=\"", "").replace("\"", ""),
            name))
        result_2.append((
            id_i.replace("id=\"", "").replace("\"", ""),
            domain,
            name))