def swap_case(s):
    newstring=""
    for ch in s:
        if ch.isupper():
            newstring+=ch.lower()
        elif ch.islower():
            newstring+=ch.upper()
        else:
            newstring+=ch
    return newstring
    

if __name__ == '__main__':