import os
import shutil
import sys

#call with argv[1] = Ordnername mit Vorlagen/ und .pdf-Datei im Ordner

def makedir_out(path_in,path_out,directory):
	os.chdir(path_out)
	os.mkdir(directory)
	return path_out+directory




Blatt = sys.argv[1]+"/"
Vorgaben = "Vorgaben/"
path_in  = os.environ['HOME'] + "/Documents/uni/Introprog/introprog-wise1718/Aufgaben/"+Blatt
path_out = os.environ['HOME'] + "/Documents/uni/Introprog/introprog-wise1718/Tutorien/t29/Gruppen/g01/Arbeitsverzeichnis/"

path_out = makedir_out(path_in,path_out,Blatt)

for filename in os.listdir(path_in):
	if filename != "Vorgaben"	:
		#print(filename)
		#print(path_out+filename)
		shutil.copyfile(path_in+filename,path_out+filename)

path_in = path_in + Vorgaben
path_out = makedir_out(path_in,path_out,Vorgaben)

for filename in os.listdir(path_in):
	tmpfilename = filename
	if "_vorgabe" in str(filename):
		tmpfilename = tmpfilename.replace("_vorgabe","")
		#print(tmpfilename)
		
	shutil.copyfile(path_in+filename,path_out+tmpfilename)






