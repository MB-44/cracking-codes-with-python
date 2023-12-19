# Caesar Cipher
import pyperclip


message = input("Enter your message: ").strip()
key = int(input("Enter your key: "))
mode = int(input("Enter 1 to encrypt, 2 to decrypt: "))


symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?"

translated = ""

for symbol in message:
    if symbol in symbols:
        symbolIndex = symbols.find(symbol)

        #this will perform encryption or decryption
        if mode == 1:
            translatedIndex = symbolIndex + key
        elif mode == 2:
            translatedIndex = symbolIndex - key

        #this will handle if it's wraparound
        if translatedIndex >= len(symbols):
            translatedIndex -= len(symbols)
        elif translatedIndex < 0:
            translatedIndex += len(symbols)
        
        translated += symbols[translatedIndex]
    else: 
        #if there's no symbol like that, it will append without encrypting or decrypting
        translated += symbol

#output translated string
print(translated)
pyperclip.copy(translated)