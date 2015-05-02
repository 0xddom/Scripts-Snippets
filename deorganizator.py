##########################################
# This script takes all the files of
# the input directory and its child
# directories and copies them to
# the output directory
#
# (c) Daniel Domínguez, 2015
##########################################

import os
import shutil

IN_DIRECTORY = u"Your input directory"
OUT_DIRECTORY = u"Your output directory"

def short_str(s,n):
    sep = "..."
    if n < len(s):
        _s = s[0:n-len(sep)-7]
        return _s + sep + s[-7:]
    return s

def build_path(f,d):
    return os.path.join(d,f)

def copy_file(f,din,dout):
    if os.path.isdir(build_path(f,din)):
        print("[+] Entering directory " + short_str(build_path(f,din),50))
        copy_files(build_path(f,din),dout)
        print("[+] Exited directory")
    else:
        print("[+] Starting to copy file " + short_str(build_path(f,din),50))
        print("[+] Output dir: " + dout)
        shutil.copy2(build_path(f,din), dout)
        print("[+] Copying finished to file " + short_str(build_path(f,dout),50))

def copy_files(din,dout):
    files = os.listdir(din)
    for file in files:
        copy_file(file,din,dout)

copy_file(IN_DIRECTORY,IN_DIRECTORY,OUT_DIRECTORY)
