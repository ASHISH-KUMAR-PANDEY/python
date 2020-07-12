def tap_code(text):
    ans=''
    alf='abcdefghijlmnopqrstuvwxyz'
    if text.isalpha():
        for i in text:
            if i=='k':i='c'
            p=alf.find(i)
            r=p//5+1
            c=p%5+1
            ans+='.'*r+' '+'.'*c+' '
        return ans[:len(ans)-1]
    else:
        text=text.split()
        for i in range(0,len(text),2):
            r=len(text[i])
            c=len(text[i+1])
            p=5*(r-1)+c-1
            ans+=alf[p]
        return ans
