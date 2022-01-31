```
import string
import random
alpha = string.ascii_letters
digits = string.digits
special_cha = string.punctuation
character = list(alpha+digits+special_cha)
def generate_random_password() :
    lenth = int(input("Input the lenth of your password : "))
    #number of characters types ; c = count
    alpha_c = int (input ("Enter the number of alphabates: "))
    digits_c = int (input ("Enter the num of digits: "))
    character_c = int (input("Enter the number of charecters: "))
    character_count = alpha_c + digits_c + character_c
    if character_count > lenth :
        print (" you have entered more than enough characters")
        return
    password  = [ ]
    for i in range (alpha_c):
        password.append(random.choice(alpha))
    for i in range (digits_c):
        password.append(random.choice (digits))
    for i in range (character_c):
        password.append(random.choice(character))
    if character_count < lenth :
        random.shuffle (character)
        for i in range (lenth, character_count):
            password.append (random.choice(character))
    random.shuffle (password)

    print ("Your password is: "+"".join(password))
generate_random_password()
```
