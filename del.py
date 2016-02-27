import os

src = os.listdir(os.getcwd())

for files in src:
    if files.endswith('~'):
        os.unlink('./'+files)
