from sys import argv
script,filename=argv
txt=open(filename,'w')
txt.truncate()
new="old text is deleted"
txt.write(new)
txt.close()