import string
import random
def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size=8 
    return ''.join(random.choice(chars) for x in range(size,12))
print(randompassword())

