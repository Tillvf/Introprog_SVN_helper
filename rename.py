import os
import shutil


#call with argv[1] = Ordnername mit Vorlagen/ und .pdf-Datei im Ordner

def makedir_out(path_out,directory):
	os.chdir(path_out)
	os.mkdir(directory)
	return path_out+directory



def create_dir_file(file,path_in,path_out):
	
	Blatt = file+"/"
	Vorgaben = "Vorgaben/"

	if Blatt not in os.listdir(path_out) :
		path_out = makedir_out(path_out,Blatt)
	else:
		os.chdir(Blatt)

	if path_out.endswith("Arbeitsverzeichnis/"+Blatt) :	
		for filename in os.listdir(path_in):
			if filename != "Vorgaben" and filename != "vorgaben"	:
				shutil.copyfile(path_in+filename,path_out+filename)
	
	path_in = path_in + Vorgaben
	if path_out.endswith("Arbeitsverzeichnis/"+Blatt) :
		print ("Arbeitsverzeichnis")
		path_out = makedir_out(path_out,Vorgaben)
	
	for filename in os.listdir(path_in):
		tmpfilename = filename
		if "_vorgabe" in str(filename):
			tmpfilename = tmpfilename.replace("_vorgabe","")
			
		shutil.copyfile(path_in+filename,path_out+tmpfilename)





#Hier muss der Pfad des Introprog SVN verzeichnisses angegeben werden
#(ausgehend vom Home verzeichnis)
#funktioniert nur auf UNIX Systemen 
#Beispielpfad: /Documents/uni/Introprog/


path_SVN = "/Documents/uni/Introprog/"

path_in    = os.environ['HOME'] + path_SVN + "introprog-wise1718/Aufgaben/"
path_out   = os.environ['HOME'] + path_SVN + "introprog-wise1718/Tutorien/t29/Gruppen/g01/Arbeitsverzeichnis/"
path_out_2 = os.environ['HOME'] + path_SVN + "introprog-wise1718/Tutorien/t29/Gruppen/g01/Abgaben/"

for filename in os.listdir(path_in):
	path_tmp   = path_in+filename+"/"
	if filename not in os.listdir(path_out) and "Blatt" in filename:
		create_dir_file(filename,path_tmp,path_out)
	if filename not in os.listdir(path_out_2) and "Blatt" in filename:
		create_dir_file(filename,path_tmp,path_out_2)


		





