def grant_the_hint(txt):
    txt = txt.split(' ')
    ans = []
    m = max(len(i) for i in txt)
    for i in txt:
        l = len(i)
        row = ['_'*l]
        ind = 1
        for j in range(len(i)):
            el = i[:ind] + ('_'*(l-ind))
            row.append(el)
            ind+=1
        for j in range(m-l):
            row.append(i)
        ans.append(row)    
    a = []
    for i in range(len(ans[0])):
        bl = []
        for j in range(len(ans)):
            bl.append(ans[j][i])
        a.append(" ".join(bl))  
    return a
