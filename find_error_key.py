import os

for dirpath, _, filenames in os.walk(os.getcwd()):
	for _file in filenames:
		f = open(str(_file),"r")
		lines = f.readlines()
		linecount = 1
		for i in lines:
		    thisline = i.split(" ")
		    for j in thisline:
			    if j == "ERROR":
				    print "File : " + str(_file) + " lineNo : " + str(linecount)
		    linecount +=1
