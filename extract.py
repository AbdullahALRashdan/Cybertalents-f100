#!/usr/bin/python

import os
import subprocess
from termcolor import colored # pip install termcolor

""" Important:

This script only works with single files that have been compressed multiple
times through different compression programs, each time compressed by itself
without any other files.
The script ends once multiple files were extracted.

1. Create a new directory (e.g.: mkdir extracted/) (child of the current one),
and copy your archive file there with no other files. 

Supported compressions:
KGB, ARJ, PPMD, ZIP, RZIP, GZIP, BZIP2, TAR, CAB, ARC, XZ, 7z, ZOO, RAR

2. Install these data compression programs:
`sudo apt-get install ppmd kgb arj rzip bzip2 cabextract nomarch zoo`

Note: You may need to install ppmd and zoo packages manually 

3. Set the variable `path` to your new directory name. """

path = "extracted" # Your new directory name

# Context manager for changing the current working directory
class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

# Return file type
def file_type(a):
    r = ''
    for i in range(0, len(a)):
        if a[i] == ',' or a[i] == '-':
            break 	
        else:
            r += a[i]
    return r

# Enter then exit directory
with cd(path):

    i = 0

    while True:

        file_name = os.popen("find . -maxdepth 1 -not -type d").read()

        # if more than one file, exit
        if (file_name.count('\n') > 1):
            print colored("=> end of decompression:\nmultiple files were extracted.", "magenta")
            break
        else:
            file_name = file_name.rstrip('\n')

        i += 1
        print colored("\n" + str(i) + " => " + "Detecting type of file: " + file_name + "\n", "cyan")
        c = os.popen("file " + file_name).read()
        print("`file` command output:\n" + c)
        s = file_type(c)
    
        if s == file_name + ": KGB Archiver file with compression level 3\n" :
            print colored("Extracting from KGB file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.kgb && kgb ' + file_name + '.kgb && rm ' + file_name + '.kgb')
        
        elif s == file_name + ": ARJ archive data":
            print colored("Extracting from ARJ file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.arj && arj e ' + file_name + '.arj && rm ' + file_name + '.arj')
        
        elif s == file_name + ": PPMD archive data\n":
            print colored("Extracting from PPMD file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.ppmd && ppmd d ' + file_name + '.ppmd && rm ' + file_name + '.ppmd')
        
        elif s == file_name + ": rzip compressed data ":
            print colored("Extracting from rzip file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.rz && rzip -d ' + file_name + '.rz')	
        
        elif s == file_name + ": gzip compressed data":
            print colored("Extracting from gzip file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.gz && gzip -d ' + file_name + '.gz')
        
        elif s == file_name + ": POSIX tar archive (GNU)\n":
            print colored("Extracting from POSIX file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.tar && tar -xvf ' + file_name + '.tar && rm ' + file_name + '.tar')
        
        elif s == file_name + ": Zip archive data":
            print colored("Extracting from Zip file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.zip && unzip ' + file_name + '.zip && rm ' + file_name + '.zip ')
        
        elif s == file_name + ": Microsoft Cabinet archive data":
            print colored("Extracting from CAB file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.cab && cabextract ' + file_name + '.cab && rm ' + file_name + '.cab')	
        
        elif s == file_name + ": bzip2 compressed data":
            print colored("Extracting from bzip2 file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.bz2 && bzip2 -d ' + file_name + '.bz2 ')
        
        elif s == file_name + ": ARC archive data":
            print colored("Extracting from ARC file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.arc && nomarch ' + file_name + '.arc && rm ' + file_name + '.arc ')
        
        elif s == file_name + ": XZ compressed data\n":
            print colored("Extracting from XZ file...\n", "grey")
            os.system(' mv ' + file_name + ' ' + file_name + '.xz && xz -d ' + file_name + '.xz  ')
        
        elif s == file_name + ": 7":
            print colored("Extracting from 7z file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.7z && p7zip -d ' + file_name + '.7z')
        
        elif s == file_name + ": Zoo archive data":
            print colored("Extracting from Zoo file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.zoo && zoo -e ' + file_name + '.zoo && rm ' + file_name + '.zoo')
        
        elif s == file_name + ": RAR archive data":
            print colored("Extracting from RAR file...\n", "grey")
            os.system('mv ' + file_name + ' ' + file_name + '.rar && unrar e ' + file_name + '.rar && rm ' + file_name + '.rar')
    
        else:
            print colored("=> End of decompression:\nEither not an archive file or a non-handled format.\n\n=> Output of `file` command:\n" + c, "magenta")
            print colored("If this format isn't handled by this script please add a new elif statement.", "red")
            break
