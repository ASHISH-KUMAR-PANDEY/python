def grant_the_hint(txt):
    txt = txt.split(' ')
    ans = []
    m = max(len(i) for i in txt)
    for i in txt:
        l = len(i)
        row = ['_'*l]
        ind = 1
   
