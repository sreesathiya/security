text=input("Enter the Text:")
col=int(input("Enter the no of cols:"))
text=text.upper().replace(" ","")
row=(len(text)+col-1)//col


text=text.ljust(row*col,"X")

matrix=[list(text[i:i+col])for i in range (0,len(text),col)]

print("Matrix:-")
for r in matrix:
    print(r)

cipher=""
for j in range(col):
    for i in range (row):
        cipher+=matrix[i][j]

print("Cipher text:",cipher)

temp=[['']* col for _ in range (row)]
k=0
for j in range (col):
    for i in range (row):
        temp[i][j]=cipher[k]
        k+=1

plain=""

for i in range (row):
    for j in range (col):
        plain+=temp[i][j]

print("Recovered:",plain)