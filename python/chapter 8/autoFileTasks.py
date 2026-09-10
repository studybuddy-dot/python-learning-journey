# copy rename delete can be done using some python modules

#copy 
import shutil
shutil.copy("Notes.txt","backup_notes.txt")

#rename
import os
os.rename("saumya_info.txt","sany_info.txt")

#delete
import os
os.remove("emp.txt")