import magic
import os
import threading
import time
import shutil

dir="/home/nida/Desktop/files"
#os.listdir(dir)




for f in os.listdir(dir):
    print(f)
    try:
        print(magic.from_file(os.path.join(dir,f), mime=True))
    except:
        continue




def create_folders():
	#take folders
	folders = []
	for i in os.listdir(dir):
		try:
			folders.append(magic.from_file(i, mime=True).split('||')[1])
		except:
			pass

	# create folders
	for f in folders:
		try:
			os.makedirs(f+'Folder')
		except:
			pass

def cpy(file):
	#print(file)
	try:
		tp = magic.from_file(file, mime=True).split('/')[1]
		#os.rename(file, os.path.join(tp+"Folder",file)) 	 # move file
		shutil.copy(file, os.path.join(tp+"Folder",file))
	except Exception as e:
		#print(e)
		pass




	

'''shutil.copy(,'')
shutil.copy('', '')
shutil.copy('', '')
shutil.copy('', '')


t1= threading.Thread(target=create_folders , args=(i,))
t2= threading.Thread(target=cpy, args=(,)) #tamamlama şeklini anlayamadım bir türlü
t3= threading.Thread(target= , args=(,))
t4= threading.Thread(target= , args=(,))
BU ÖDEVİ YAPAMADIM AMA BANA ÇOK ŞEY KATTI      (⌐■_■)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()'''
