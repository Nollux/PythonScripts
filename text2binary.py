#!/usr/bin/python3
text_input = list(input("Enter text: "))

unicode = []
binary = []

try:
    
    for i in text_input:
        unicode.append(ord(i))
        
    for k in unicode:
        num = bin(k)[2:]
        binary.append(num)

    for j in range(len(binary)):
        while len(str(binary[j])) % 8 != 0:
            binary[j] = "0" + binary[j]

    result = ''.join(binary)
       
    print(result)

except:
    
    print("Error: could not convert")

