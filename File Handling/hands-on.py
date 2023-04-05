paradin = open("C:\\Users\\chiag\\OneDrive\\Desktop\\Cloud DevOps\\Ag-devops\\Python\\python-introduction\\File Handling\\ikpe.txt", "r")

#print(dir(paradin))

#paradin.write("the way i am feeling now \nI am not happy ooo \nI am more than happy")

print(paradin.read())

file_data = open('C:\\Users\\chiag\\OneDrive\\Desktop\\Cloud DevOps\\Ag-devops\\Python\\python-introduction\\File Handling\\sample.txt', 'r') # an open bug from the vs code side https://stackoverflow.com/questions/51006989/visual-studio-code-filenotfounderror-errno-2-no-such-file-or-directory
print(file_data.read())
file_data.close()

# imports
from os.path import dirname, join
import os

print("\n# Lets try to fix the folder path issue, read the file using automated path")
current_dir = dirname(__file__)
file_path = join(current_dir, ".\ikpe.txt")
file_data= open(file_path, 'r')
print(file_data.read())
file_data.close()

print("\n# Lets try to fix the folder path issue and still read line 3")
current_dir = dirname(__file__)
file_path = join(current_dir, ".\ikpe.txt")
file_data= open(file_path, 'r')
print(file_data.readlines()[2])
file_data.close()

print("\n#verifying if the file exists before deletion")
current_dir = dirname(__file__)
file_path = join(current_dir, "./new_file.txt")
if os.path.exists(file_path):
	os.remove(file_path)
else:
	print("file with path: {} not found".format(file_path))