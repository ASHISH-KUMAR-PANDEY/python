def convert_to_roman(number):
    number = str(number)
	#Convert number into a list of units ex: 3999 to [3000, 900, 90, 9]
    lst = [ n.ljust(len(number)-i, '0') for i, n in enumerate(number) ]

    # Conversion rules:
    # 1 - I,
    # 4 - IV, 5 - V,
    # 9 - IX, 10 -X,
    # 40 - XL, 50 - L,
    # 90 - XC, 100 - C,
    # 400 - CD, 500 -D
    # 900 - CM, 1000 - M
    roman_string = ''
    for num in lst:
        if int(num) >= 1000:
            roman_string += 'M'*int(num[0])
        elif int(num) == 900:
            roman_string += 'CM'
        elif int(num) >= 500:
            roman_string += 'D'+'C'*int(str(int(num)-500)[0])
        elif int(num) == 400:
            roman_string += 'CD'
        elif int(num) >= 100:
            roman_string += 'C'+'X'*int(str(int(num)-100)[0])
        elif int(num) == 90:
            roman_string += 'XC'
        elif int(num) >=50:
            roman_string += 'L'+'X'*int(str(int(num)-50)[0])
        elif int(num) == 40:
            roman_string += 'XL'
        elif int(num) >= 10:
            roman_string += 'X'+'I'*int(str(int(num)-10)[0])
        elif int(num) == 9:
            roman_string += 'IX'
        elif int(num) >= 5:
            roman_string += 'V'+'I'*int(str(int(num)-5)[0])
        elif int(num) == 4 :
            roman_string += 'IV'
        else:
            roman_string += 'I'*int(num[0])

    return roman_string
