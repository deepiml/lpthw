def prime(x):
	for i in range(2, x):
		y = x % i
		if y!=0:
			

print 'Is 2 Prime? %s' % prime(2)
print 'Is 3 Prime? %s' % prime(3)
print 'Is 6 Prime? %s' % prime(6)
print 'Is 11 Prime? %s' % prime(11)