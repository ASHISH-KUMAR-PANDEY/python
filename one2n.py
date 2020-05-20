def digits(number):
    if number == 1:
        return 0

    a = 0
    myans = 0
    while number > 1:
        if number <= 9*10**a:
            myans += (a+1)*(number-1)
            number -= number*10**a
        else:
            myans += (a+1)*9*10**a
            number -= 9*10**a

        a += 1
    return myans
