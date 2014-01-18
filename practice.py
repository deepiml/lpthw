print "enter x"
x=raw_input("value")

from sys import argv
script,number_1,number_2 = argv

print " %r %r"%(number_1,number_2)

files=open(number_1)

def rewind(f):
    f.seek(10)

rewind(files)

y = files.read()

print y

print 'i\'d like to use\''

def evaluation():
    y=10+23-76
    return y


c=evaluation()
print c

def practice():
    print"am practising"

practice()

