import os
import math

print(os.getcwd())
nida = os.getenv("HOME")
os.chdir(nida)                                          #change directory to user's home



os.mkdir('sec')                                         #create sec directory
os.chdir('sec')                                        #change directory to sec
os.mkdir('bin')                                         #create bin directory
os.mkdir('lib64')                                        #creating lib64 directory.
os.mkdir ('lib')                                        #create lib directory
os.mkdir ('etc')                                        #create etc directory



os.system("cp -ru $(which bash) ~/sec/bin/")	        #copying the dependencies of bash
os.system("cp -ru /lib/x86_64-linux-gnu  ~/sec/lib/ ")
os.system("cp -ru /lib64/ ~/sec/")

os.chroot(nida + "/sec")
print(os.getcwd())
print("nidanınjaili")
print(os.getcwd())

