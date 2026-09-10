# ask user for a file name and copy it to a backup folder

import shutil
file=input("Enter filename:")
shutil.copy(file,"backup_"+file)