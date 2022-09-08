import re

if __name__ == '__main__':
    original = ["FirstItem", "FriendsList", "MyTuple"]
    redone = []
    for vari in original:
        search = re.findall('\B[A-Z]', vari)
        for to_transform in search:
            redone.append(vari.replace(to_transform, f'_{to_transform.lower()}').lower())
    print(redone)
