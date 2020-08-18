def new_alph(ch):
    ch = ch.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alph = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alph
def encrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alph(char)
        for t in text:
            if alph.count(t) == 1 :
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += new[alph.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1
    return res
text1 = 'SHRADDHA'
text_dec = 'MNOPQRRT'
key = 'KEY'
if len(key) <= len(text1):
    big_key = key * (len(text1) // len(key)) + key[:len(text1) % len(key)]
    text_encrypt = encrypt(text1, big_key)
print('PLAIN-TEXT: "' + text1 + '"')
print('KEYWORD : "' + key + '"')
print('CIPHERTEXT : ' + text_encrypt)
