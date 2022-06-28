def longest(words):
    mynewlist = []
    for i in words:
        mynewlist.append(len(i))

    return (max(mynewlist))