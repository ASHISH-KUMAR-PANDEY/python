import string
all_letters= string.ascii_letters
charachter = {}
key = 1

for i in range(len(all_letters)):
    charachter[all_letters[i]] = all_letters[(i+key)%len(all_letters)]
    
plain_text= "substitution method"
substituted_text=[]

for char in plain_text:
    if char in all_letters:
        temp = charachter[char]
        substituted_text.append(temp)
    else:
        temp =char
        substituted_text.append(temp)

substituted_text= "".join(substituted_text)
print("The shift key is: ",key)
print("Substituted Text is: ",substituted_text)
