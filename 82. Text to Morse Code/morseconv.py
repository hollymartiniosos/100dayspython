
def morse_converter(text: str) -> str: 
    #dictionary
    morse = {'A':'.-',
         'B':'-...',
         'C':'-.-.',
         'D':'-..',
         'E':'.',
         'F':'..-.',
         'G':'--.',
         'H':'....',
         'I':'..',
         'J':'.---',
         'K':'-.-',
         'L':'.-..',
         'M':'--',
         'N':'-.',
         'O':'---',
         'P':'.--.',
         'Q':'--.-',
         'R':'.-.',
         'S':'...',
         'T':'-',
         'U':'..-',
         'V':'...-',
         'W':'.--',
         'X':'-..-',
         'Y':'-.--',
         'Z':'--..',
         '0':'-----',
         '1':'.----',
         '2':'..---',
         '3':'...--',
         '4':'....-',
         '5':'.....',
         '6':'-....',
         '7':'--...',
         '8':'---..',
         '9':'----.',
         '.':'.-.-.-',
         ',':'--..--',
         '?':'..--..',
         '=':'-...-',
         ' ':' '}
    # message=''
    # # long version - not sure how to add each letter after iteration to the message instead of printing it one by one
    # for character in text:
    #     message += morse[character] + ' '

   
    message2 = " ".join([morse[character] for character in text])
    print(f'Encrypted message is: {message2}')
    return message2  

    
