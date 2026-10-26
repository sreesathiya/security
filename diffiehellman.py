p=int(input("Enter the value for p:"))
g=int(input("Enter the value for g:"))

a=int(input("Enter the private key of A's:"))
b=int(input("Enter the private key of B's:"))


A=pow(g,a,p)
B=pow(g,b,p)

AS=pow(B,a,p)
BS=pow(A,b,p)

print("p:",p)
print("g:",g)
print("private key of A:",a)
print("public key of A:",A)
print("Private key of B",b)
print("public key of B:",B)
print("shared key:",AS,":",BS)