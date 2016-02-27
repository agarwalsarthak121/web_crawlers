import os,shutil

source = os.listdir()
ch = input('Enter chapter: ')
for files in source:
    if 'C'+ch+'P' in files:
        os.rename('./'+files,'./'+files[:-4]+'.png')
