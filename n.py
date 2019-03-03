import os
os.chdir('/home')
os.system('mkdir -p  $HOME/os_lab_0')
#Allows us to run system commands or other programs through Python
username=os.getlogin()
ap='/home/'+username+'/os_lab_0/'
os.chdir(ap)
open('nida.txt', 'a').close()
open('elma.txt','a').close()
open('armut.py','a').close()

lastmodified1= os.stat('elma.txt').st_mtime
lastmodified2= os.stat('nida.txt').st_mtime
lastmodified3= os.stat('armut.py').st_mtime
print("elma", lastmodified1,"nida", lastmodified2,"armut", lastmodified3)

for i in os.listdir(os.getcwd()):
     if i.endswith('.txt'):
        print(i)
