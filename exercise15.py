from sys import argv
script,filename=argv
txt=open(filename)
print "the filename is %r"%filename
txt.read()
print "am typing it again"
file_again=raw_input('>')
txt_again=open(file_again)
print 'txt_again.read()'
