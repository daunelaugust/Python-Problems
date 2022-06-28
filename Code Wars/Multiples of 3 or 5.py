def solution(number):
    list = []
    if number <= 0:
        return 0
    for i in range(1,number):
        if (i % 3 == 0) and (i % 5 == 0):
            list.append(i)
        elif(i%3==0) or (i%5==0):
            list.append(i)

    return sum(list)