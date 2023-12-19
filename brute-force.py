# Caesar Cipher
import pyperclip


message = input("Enter your message: ").strip()

# mode = int(input("Enter 1 to encrypt, 2 to decrypt: "))


symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(symbols)):
    translated = ""

    for symbol in message:
        if symbol in symbols:
            symbolIndex = symbols.find(symbol)
            translatedIndex = symbolIndex - key
            
            if translatedIndex < 0:
                translatedIndex += len(symbols)

            translated += symbols[translatedIndex]
        else: 
            #if there's no symbol like that, it will append without encrypting or decrypting
            translated += symbol

    #output translated string
    print('Key #%s: %s' % (key, translated))
pyperclip.copy(translated)