import os
import math

print(os.getcwd())
nida = os.getenv("HOME")
os.chdir(home)                                          #change directory to user's home



os.mkdir('lib64')                                       #create lib64 directory
os.chdir('jail')                                        #change directory to jail
os.mkdir('bin')                                         #create bin directory
os.mkdir('jail')                                        #creating jail directory.
os.mkdir ('lib')                                        #create lib directory
os.mkdir ('etc')                                        #create etc directory



os.system("cp -ru $(which bash) ~/jail/bin/")	        #copying the dependencies of bash
os.system("cp -ru /lib/x86_64-linux-gnu  ~/jail/lib/ ")
os.system("cp -ru /lib64/ ~/jail/")

os.chroot(home + "/jail")
print(os.getcwd())
print(math.sqrt(16))
print(os.getcwd())

