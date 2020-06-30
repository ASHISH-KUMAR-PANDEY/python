def farey(n):
    Ltuple = []
    for denominator in range(1,n+1):
        for numerator in range(0, denominator+1):
            Ltuple.append( (numerator/denominator, str(numerator)+"/"+str(denominator)) )

    Ltuple.sort(key = lambda x : x[0])

    #delete the same element, rank is based on how low the denominator is#
    def restart():
        obl = []

        for pair in Ltuple.copy():
            if [x[0] for x in Ltuple.copy()].count(pair[0]) > 1:
                for pairS in Ltuple.copy():
                    if pairS[0] == pair[0]:
                        obl.append(pairS)

                delete = sorted(obl, key=lambda x : int(x[1].split("/")[1]))[1:]
                for pair in delete:
                    Ltuple.remove(pair)
                return False
        return True

    while True:
        if restart():
            break

    Ltuple.sort(key = lambda x : x[0])
    return [x[1] for x in Ltuple]
