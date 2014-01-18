from sys import argv
from os.path import exists
script,file1,file2=argv
input=open(file1)
input1=input.read()
print "%d bytes"%len(input1)
print "file2 exists %r"%exists(file2)
raw_input()
output=open(file2,'w')
output.write(input1)

output.close()
input.close()