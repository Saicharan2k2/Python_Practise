# f=open(r"text_file.txt")
# # here \ is included in file path because python treats single slash as escape character
# # by placing second slash it eliminates 
# print(f.read())

# f=open(r"text_file.txt","a")
# f.write("this file is added with some content")
# f.close()

# f=open(r"text_file.txt","r")
# print(f.read())
# f.close()
# PS C:\Users\saich\Python Practise> & C:/Users/saich/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/saich/Python Practise/file_operations.py"
# This is text file created for testing purpose this file is opened with the help of python open functionthis file is added with some content

import os
os.remove(r"text_file.txt")