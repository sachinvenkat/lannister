import shutil, os
os.chdir('F:\\')
shutil.copy('F:\capp.txt', 'F:\\bixbzy')


import shutil
shutil.move('F:\\networks.txt', 'F:\\ping')
#Moving and Renaming Files and Folders


#Permanently Deleting Files and Folders

import os
for filename in os.listdir():
if filename.endswith('.rxt'):
os.unlink(filename)

If you had any important files ending with .rxt, they would have been
accidentally, permanently deleted. Instead, you should have first run the
program like this:

import os
for filename in os.listdir():
if filename.endswith('.rxt'):
#os.unlink(filename)
print(filename)


#Walking a Directory Tree

import os
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
print('The current folder is ' + folderName)
for subfolder in subfolders:
print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
for filename in filenames:
print('FILE INSIDE ' + folderName + ': '+ filename)
print('')


#Compressing Files with the zipfile Module

import zipfile, os
os.chdir('C:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()


#Extracting from ZIP Files

import zipfile, os
os.chdir('C:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()


#Creating and Adding to ZIP Files

import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
