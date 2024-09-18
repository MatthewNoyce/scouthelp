import os

#Change for the folder where the images are stored
filepath = r""

#Change to edit the name of the first file in the directory
#e.g. if wanting to start at 10 instead of 0 change counter variable
 
counter = 0

#takes every file in the directory and renames it so that it is all in numerical order.
for file in os.listdir(filepath):
    name = file.split(".")
    name[0] = counter
    counter +=1

    os.rename(f"{filepath}/{file}", f"{filepath}/{name[0]}.{name[1]}")
    
