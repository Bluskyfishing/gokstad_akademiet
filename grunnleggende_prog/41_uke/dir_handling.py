import os
import shutil

currentDir = os.getcwd()
print(currentDir)

newFolder = os.path.join(currentDir, "Test")
if not os.path.exists("Test"):
    print("Made new folder:",newFolder)
    os.mkdir("Test")
else:
    print("Folder",newFolder,"already exists!")

if os.path.exists(newFolder) and os.path.isdir(newFolder):
    print("Removed folder:",newFolder)
    os.rmdir(newFolder)
else:
    print("Couldn't find folder:",newFolder)


multiple_dirs = os.path.join(currentDir, "m1", "m2", "m3")

if not os.path.exists(multiple_dirs):
    print("Making new folder:",multiple_dirs)
    os.mkdir(multiple_dirs)
else:
    print("Folder",multiple_dirs,"already exists!")

#Deletes everything in folder.  B
removeDir = os.path.join(currentDir,"m1")
if os.path.exists(removeDir) and os.path.isdir(removeDir):
    shutil.rmtree(removeDir)
    print("Deleted folder",removeDir)
else:
    print("Couldn't find folder(s):",removeDir)