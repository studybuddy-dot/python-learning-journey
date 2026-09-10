#word counter 
#count how many words are there in file notes.txt

with open("notes.txt","r") as f:
    data=f.read()
    print(len(data))