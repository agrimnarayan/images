plainText = input("ENTER THE PLAIN TEXT").upper().replace(' ','')
key = int(input("ENTER THE KEY"))
encr = ''.join([chr(((ord(i)%65)+key)%26 + 65) for i in plainText])
print(encr)
decr = ''.join([chr(((ord(i)%65)-key)%26 + 65) for i in encr])
print(decr)