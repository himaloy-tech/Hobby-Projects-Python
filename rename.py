import os
# Source file path 
source = input("Source: ")
  
# destination file path 
dest = input("Destination with the new file name: ")
  
  
# try renaming the source path 
# to destination path 
# using os.rename() method 
  
try : 
    os.rename(source, dest) 
    print("Source path renamed to destination path successfully.") 
  
# If Source is a file  
# but destination is a directory 
except IsADirectoryError: 
    print("Source is a file but destination is a directory.") 
  
# If source is a directory 
# but destination is a file 
except NotADirectoryError: 
    print("Source is a directory but destination is a file.") 
  
# For permission related errors 
except PermissionError: 
    print("Operation not permitted.") 
  
# For other errors 
except OSError as error: 
    print(error)