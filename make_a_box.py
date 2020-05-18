def makeBox(n):
    a=""
    b=list()
    for i in range(n):
        if(i==0):
            a+="#"*n
            b.append(a)
            a=""
        elif(i == n-1):
            a+='#'*n
            b.append(a)
            a=""
        else:
            a+='#'+" "*(n-2)+'#'
            b.append(a)
            a=""
