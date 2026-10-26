def prep_matrix(key):
    key=key.upper().replace("J","I")
    rem="ABCDEFGHIKLMNOPQRSTUVWXYZ"


    char=""

    for ch in key+rem:
        if ch.isalpha() and ch not in char:
            char+=ch

    return [list(char[i:i+5])for i in range (0,25,5)]

def prep_text(text):

    result=""

    text=text.upper().replace("J","I").replace(" ","")
    i=0

    while(i<len(text)):
        result+=text[i]

        if i+1 < len(text):
            if text[i] == text[i+1]:
                result+="X"
                i+=1
            else:
                result+=text[i+1]
                i+=2
        else:
            i+=1
    if len(result)%2 != 0:
        result+="X"

    return result
def playfair(text,matrix,val):
    result=""

    for i in range(0,len(text),2):
        a=text[i]
        b=text[i+1]
        r1=-1
        r2=-1
        c1=-1
        c2=-1
        for r in range(5):
            for c in range (5):
                if matrix[r][c] == a :
                    r1=r
                    c1=c
                if matrix[r][c] == b:
                    r2=r
                    c2=c

        if r1 == r2:
            result+=matrix[r1][(c1+val)%5]
            result+=matrix[r2][(c2+val)%5]
        elif c1 == c2 :
            result+=matrix[(r1+val)%5][c1]
            result+=matrix[(r2+val)%5][c2]
        else:
            result+=matrix[r1][c2]
            result+=matrix[r2][c1]
    return result

key=input("Enter the key:")
text=input("Enter the text:")

matrix=prep_matrix(key)
text=prep_text(text)

cipher=playfair(text,matrix,1)
recover=playfair(cipher,matrix,-1)
print("text:",text)
print("Cipher:",cipher)
print("Recover:",recover)