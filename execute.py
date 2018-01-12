import os

path_in = os.environ['HOME'] + "/Documents/uni/Introprog/introprog-wise1718/Aufgaben/"
path_out = os.environ['HOME'] + "/Documents/uni/Introprog/introprog-wise1718/Tutorien/t29/Gruppen/g01/Arbeitsverzeichnis/"

for filename in os.listdir(path_in):
	if filename not in os.listdir(path_out) and "Blatt" in filename:
		print(filename)
		command = "python3 rename.py "+filename
		os.system(command)

#os.system("python3 rename.py 04")