#append "completed" to an existing file named status.txt

with open("status.txt","w") as f:
    f.write("4th sept = Incomplete")

with open("status.txt","a") as f:
    f.write("\n5th sept = Completed")