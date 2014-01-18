from sys import argv
script,my_name=argv
prompt='>'
print "hi %r ,am the %r script"%(my_name,script)
print "i did like 2 ask few questions"
print "do u like me %s"%my_name
likes=raw_input(prompt)
print "where do u live %s?"%my_name
lives=raw_input(prompt)
print "what kind of a computer do u have?"
computer=raw_input(prompt)
print '''Alright, so you said %r about liking me.
 You live in %r. Not sure where that is.
 And you have a %r computer. Nice'''%(likes,lives,computer)