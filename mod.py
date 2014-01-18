from sys import argv
program,my_name=argv
new='>'
print "hi %r ,am the %r "%(my_name,program)
print "i did like 2 ask few questions"
print "do u like me %s"%my_name
likes=raw_input(new)
print "where do u live %s?"%my_name
lives=raw_input(new)
print "what kind of a computer do u have?"
computer=raw_input(new)
print '''Alright, so you said %r about liking me.
 You live in %r. Not sure where that is.
 And you have a %r computer. Nice'''%(likes,lives,computer)