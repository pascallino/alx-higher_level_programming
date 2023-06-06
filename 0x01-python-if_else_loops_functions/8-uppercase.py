def uppercase(str):
    uppercase = ""
    for ch in str :
        if ch >= 'a' and ch <= 'z' :
            uppercase += chr(ord(ch) - 32)
        else :
            uppercase += ch
    print(f"{uppercase:s}")

    
