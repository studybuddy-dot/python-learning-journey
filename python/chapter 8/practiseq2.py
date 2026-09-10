#write a program to read certificate.txt and check whether the word lives comes in it or not

file=open("certificate.txt","r")
data=file.read()

data=data.lower()

if "live" in data:
    print("Found live in certificate.txt")