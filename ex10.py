from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA


private_key=None
public_key=None

def generate_key():
    global private_key,public_key
    key=RSA.generate(2048)
    private_key=key
    public_key=key.publickey()


    with open("private.pem","wb") as f:
        f.write(private_key.export_key())

    with open("public.pem","wb") as f:
        f.write(public_key.export_key())

    print("Generated Success")
    print("private:",private_key.export_key().decode())
    print("public:",public_key.export_key().decode())


def sign():
    if private_key is None:
        print("generate first")
        return 

    msg=input("Enter the message:")
    digest=SHA256.new(msg.encode())
    sign=pkcs1_15.new(private_key).sign(digest)

    print("signed")
    print("Digest:",digest.hexdigest())
    print("Signature:",sign.hex())


def verify_sign():

    if public_key is None:
        print("generate first")
        return 

    msg=input("Enter the message:")
    sign=input("Enter the sign(hex):")


    try:
        sign=bytes.fromhex(sign)
        digest=SHA256.new(msg.encode())
        pkcs1_15.new(public_key).verify(digest,sign)
        print("Valid")
    except (ValueError,TypeError):
        print("Invalid")


def tampering():
    if private_key is None or public_key is None:
        print("Generate keys first!")
        return
    msg=input("Enter the message:")
    digest=SHA256.new(msg.encode())

    sign=pkcs1_15.new(private_key).sign(digest)

    modified=msg+"X"

    try:
        digest=SHA256.new(modified.encode())
        pkcs1_15.new(public_key).verify(digest,sign)
        print("Valid")
    except (TypeError,ValueError):
        print ("Invalid - Message has been modified!")




while True:
    print("1.Generate key")
    print("2.sign")
    print("3.verify")
    print("4.tampering")
    print("5.To exit")


    c=int(input("Enter the choice:"))

    if c == 1:
        generate_key()
    elif c==2:
        sign()
    elif c==3:
        verify_sign()
    elif c==4:
        tampering()
    else:
        break