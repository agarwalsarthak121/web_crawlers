#! /usr/bin/python3

import shutil
import os
import re

source = os.listdir()

for files in source:
    if files.lower().endswith('.mp4') or files.lower().endswith('.mkv') or files.lower().endswith('.avi'):
        if os.path.getsize('./'+files) > 200000000:
            os.makedirs('Movies',exist_ok=True)
            dest = './Movies'
            shutil.move('./'+files,dest)
        else:           
            os.makedirs('Videos',exist_ok=True)
            dest = './Videos'
            shutil.move('./'+files,dest)
    if files.lower().endswith('.jpg') or files.lower().endswith('.png'):
        os.makedirs('Pictures',exist_ok=True)        
        dest = './Pictures'
        shutil.move('./'+files,dest)
    if files.lower().endswith('.pdf') or files.lower().endswith('.docx'): 
        os.makedirs('Docs',exist_ok=True)      
        dest = './Docs'
        shutil.move('./'+files,dest)
    if files.lower().endswith('.zip'):
        os.makedirs('Compressed',exist_ok=True)
        dest = './Compressed'
        shutil.move('./'+files,dest)

