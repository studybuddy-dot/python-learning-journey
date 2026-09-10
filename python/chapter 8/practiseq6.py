#read a file and print full content

with open("report.txt","r") as f:
    data=f.read()
    print(data)