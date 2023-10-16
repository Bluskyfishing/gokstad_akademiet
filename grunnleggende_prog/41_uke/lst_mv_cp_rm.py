import os 
import shutil

dirContent = os.listdir()
for content in dirContent:
    print(f"Is folder: {os.path.isdir(content)}\nIs file: {os.path.isfile(content)}")

oldName = "Cool.txt"
newName = "NotCool.log"
os.rename(oldName,newName)


#shutil.move(oldName, newName)

copyName = f"copy_{oldName}"

if os.path.exists(oldName) and os.path.isfile(oldName) and not os.path.exists(copyName):
    shutil.copy(oldName,newName)
    print(f"Copied {oldName} --> {newName}")
else:
    print("Couldn't find the file you wanted to copy or the file you copied already exists!")



if os.path.exists(newName) and os.path.isfile(newName):
    os.remove(newName)
    print(f"Removed file: {newName}")
else:
    print("Couldnt find the file.")