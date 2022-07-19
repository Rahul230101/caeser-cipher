# Caeser Cipher

def caser_cipher(text,shift,direction):
    if direction == "encode":
        cipher = ""
        for i in text:
            if i in alphabets:
                position = alphabets.index(i)
                new_position = position + shift
                new_i = alphabets[new_position]
                cipher += new_i
            else:
                cipher += i
        print(cipher)
    elif direction == "decode":
        cipher = ""
        for i in text:
            if i in alphabets:
                position = alphabets.index(i)
                new_position = position - shift
                new_i = alphabets[new_position]
                cipher += new_i
            else:
                cipher += i
        print(cipher)

print("Lets Encode and Decode some messages !!!!")
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
,'o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n'
,'o','p','q','r','s','t','u','v','w','x','y','z']
# should_continue = True 
while True:  # while should_continue:
    direction = input("Enter 'encode' or 'decode' to encrypt and decrypt the message : \n")
    text = input("Type your message: \n").lower()
    shift = int(input('Enter a shift: \n'))
    shift = shift % 25
    caser_cipher(text,shift,direction)
    
    user = input("Do you want to continue: press y or n: \n").lower()
    if user == 'y':
        print("Welcome Back to Caser Cipher")
        continue
    else:  # should_continue = False
        print("Goodbye! have nice day") 
        break