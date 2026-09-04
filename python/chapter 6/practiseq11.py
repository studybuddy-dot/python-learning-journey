#multiplication table that user wants using for loop
n=int(input("Enter a number:"))
m=1
for m in range(1,11,1):
    print(f"{n}x{m}={n*m}")
    m=m+1