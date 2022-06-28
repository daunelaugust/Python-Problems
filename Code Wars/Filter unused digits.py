def unused_digits(*numbers):
    place = []

    for i in str(numbers):
        place.append(i)

    mynewlist = [s for s in place if s.isdigit()]
    lastlist = []
    for k in range(0, 10):
        if str(k) in mynewlist:
            continue
        else:
            lastlist.append(k)
    laststring = ""
    for j in lastlist:
        laststring += str(j)

    return laststring