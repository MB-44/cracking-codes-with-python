# Caesar Cipher

import pyperclip


message = "This is my hidden message"
key = 13

mode = "decrypt"

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?"

translated = ""

for symbol in message:
    if symbol in symbols:
        symbolIndex = symbols.find(symbol)

        #this will perform encryption or decryption
        if mode == "encrypt":
            translatedIndex = symbolIndex + key
        elif mode == "decrypt":
            translatedIndex = symbolIndex + key

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