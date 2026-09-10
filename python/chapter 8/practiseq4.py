# open a file named report.txt in write mode

#write mode : replacess sentences
file=open("report.txt","w")
data=file.write("hello")

#append mode : addds sentences instead of replacing them
file=open("report.txt","a")
file.write("\nHI")
