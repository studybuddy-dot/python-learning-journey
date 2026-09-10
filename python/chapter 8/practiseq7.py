#read only first line of a file

with open("report.txt","r") as f:
    line1=f.readline()
    print("Line 1 is:",line1)
    