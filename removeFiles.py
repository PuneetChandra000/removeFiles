import os 
import shutil

print(os.getcwd())

#os.mkdir("/WhiteHatJr/Python/c99/c99 project/newFolder")

path = "/WhiteHatJr/Python/c99/c99 project/newFolder"

print( os.path.exists(path) )

if os.path.exists(path) :
   input(os.listdir(path))

else :
    print("This path is wrong")

listOfFiles = os.listdir(path)

for i in listOfFiles :
    name ,  ext = os.path.splitext(i)

    if ext == '':
        continue

    else :
        shutil.rmtree(path)
