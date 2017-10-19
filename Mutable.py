



print ("string is immutable")

a = "my girls"
print (a)
print ('address of current a is: {}'.format(id(a)))
#a[3] = "G"
print (a)

a = "my scholars"
print (a)
print ('address of current a is: {}'.format(id(a)))
#a[3] = "S"
#print (a)



print ("\n\nstring buffer is immutable")
print ("\n\nlist is mutable")
a = [1,2,3,4,5]
print (a)
print ('address of current a is: {}'.format(id(a)))

a[3] = 'S'
print (a)
print ('address of current a is: {}'.format(id(a)))



list = ['sky lake', 'tiger lake', 'cannon lake', 'ice lake', 'salt lake' ]

output = '<ul>\n'

for cpu in list:
	output += '\t<li>{}</li>\n'.format(cpu)
	print ('address of current cpu is: {}'.format(id(cpu)))

#adds closing of list
output += '</ul>'

print (output)

print ('\n')

