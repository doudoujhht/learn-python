
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits = ['0','1','2','3','4','5','6','7','8','9']
while True:

    choice = input("type encode to encode a message, type decode to decode a message ")
    if choice == "encode":
        message = input("enter your message: ")
        shift = int(input("enter the shift: "))
        for i in message:
            if i in letter:
                print(letter[(letter.index(i) + shift) % 26], end="")
            elif i in uppercase: 
                print(uppercase[(uppercase.index(i) + shift) % 26], end="")
            elif i in digits:
                print(digits[(digits.index(i) + shift) % 10], end="")
            else:
                print(i, end="")
        print("\n")
    
    elif choice == "decode":
        message = input("enter your message: ")
        shift = int(input("enter the shift: "))
        for i in message:
            if i in letter:
                print(letter[(letter.index(i) - shift) % 26], end="")
            elif i in uppercase:
                print(uppercase[(uppercase.index(i) - shift) % 26], end="")
            elif i in digits:
                print(digits[(digits.index(i) - shift) % 10], end="")
            else:
                print(i, end="")
        print("\n")
    
    else:
        print("please enter encode or decode")
        continue
    decode_again = input("do you want to decode another message? (y/n)")
    if decode_again.lower() != 'y':
        print("Bye!")
        break


