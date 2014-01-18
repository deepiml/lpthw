# Global scope
x = 10

# Scope lookup
def foo():
	print x  # 10 from global scope

foo()  # prints 10

# Variable assignment creates new value
def bar():
	x = 15
	print x

bar() # prints 15
print x # prints 10


def foobar():
	print x # print 10
	def cat():
		x = 12 
		print x # prints 12 -- local
		def dog():
			print x # prints 12 -- enclosed
		dog()
	cat()

foobar()


# DO NOT USE THIS IN REAL LIFE PROGRAMMING!
# MODIFYING GLOBALS IS BAD!!!
def bad():
	global x
	x = 27

print x  # 10
bad()
print x # 27
