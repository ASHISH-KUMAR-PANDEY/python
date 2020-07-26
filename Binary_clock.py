def binary_clock(time):
    time = time.replace(':','')
    temp = list(map(int,time))
    a = [0]
    b = [2,4]
    for i in range(len(temp)):
        if i in a:
            temp[i] = '  '+bin(temp[i])[2:].zfill(2)
        elif i in b:
            temp[i] = ' '+bin(temp[i])[2:].zfill(3)
        else:
            temp[i] = bin(temp[i])[2:].zfill(4)
    temp2 = []
    for i in range(6):
        temp2.append(list(temp[i]))
    temp = list(map(list, zip(*temp2)))

    for i in range(4):
        temp[i] = ''.join(temp[i])

    return temp
