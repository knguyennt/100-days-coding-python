print('''
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                   
''')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text, shift_amount, cipher_direction):
    shift_amount = len(alphabet) if shift_amount > len(alphabet) else shift_amount
    re = ''
    for w in plain_text:
        if w in alphabet:
            if cipher_direction == "encode":
                if alphabet.index(w) + shift_amount > len(alphabet) - 1:
                    re += alphabet[(alphabet.index(w) + shift_amount) - len(alphabet) - 1]
                else:
                    re += alphabet[alphabet.index(w) + shift_amount]
            elif cipher_direction == "decode":
                if alphabet.index(w) - shift_amount < 0:
                    re += alphabet[len(alphabet) - (alphabet.index(w) + 1) + shift_amount]
                else:
                    re += alphabet[alphabet.index(w) - shift_amount]
        else:
            re += w
    print(re)

caesar(text, shift, direction)