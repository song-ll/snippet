# -*- coding: utf-8 -*-
# @Author: Song
# @Date:   2017-07-16 03:39:36
# @Last Modified by:   Song
# @Last Modified time: 2017-07-28 23:32:28


#

#import logging

print ('****first class function****')
def square(x):
	return x * x

def cube(y):
	return y * y * y
#f = square() will execute the function
#g = square assign function 
f = square(9)
g = square

print(square)
print(f)
print(g)
print(g(9))


def arr_map(func, arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result


square_1 = arr_map(square, [1,2,3,4,5,6])
print(square_1)

cube_1 = arr_map(cube, [1,2,3,4,5,6]) 
print(cube_1)


def logger(msg):
	def log_message():
		print ('Log:', msg)

	return log_message
	
#closure only pass assignment
log_hi = logger('Hi, there!')
#execute function
log_hi ()


def html_tag(tag):
	def wrap_text(msg):
		print ('<{0}>{1}</{0}>'.format(tag, msg))

	return wrap_text

dart_1 = html_tag('h1')
dart_2 = html_tag('Test Headline!')
dart_3 = html_tag('Another Headline!')
#wait to be excuted
print(dart_1)
print(dart_2)
print(dart_3)

dart_1 ('It\'s the Headline!')
dart_2('hey no mountain high enough')
dart_3('mountain high 500 meters short to îts peak')


print ('*****variable scope*****')
print ('*****local variable scope*****')
#function
print ('*****enclapsing variable scope*****')
#
print ('*****global variable scope*****')
#top level of module
print ('*****built-in variable scope*****')
#preassigned

x = 'global x'

def demo():
	y = 'local y'
	#doesn't overwrite global x only valid inside the function
	x = 'local x'
	print (y)

demo()


print ('didn\'t find in local | enclosing, found in global')
def demo_1():
	y = 'local y'
	#didn't find in local | enclosing, found in global
	print (x)

demo_1()


print ('doesn\'t overwrite global x only valid inside the function')
def demo_2():
	y = 'local y'
	#doesn't overwrite global x only valid inside the function
	x = 'local x'
	print (x)
#can't access local y via gelb
#print (y)
#access global via gelb
print (x)

demo_2()


print ('overwrite global x from inside the function')
def demo_3():
	global x
	#overwrite global x from inside the function
	x = 'local x'
	y = 'local y'
	print (x)

demo_3()
 

print ('passing parameter as argument inside the function as local')
def demo_4(z):
	global x
	#overwrite global x from inside the function
	x = 'local x'
	print (z)

demo_4('local z')


#import buildins

#print(dir(buildins))
#buildins are easily overwritten in python

print ('Enclosed variable within nested functions')

def outter():
	xx = 'outter xx'

	def inner():
		xx = 'inner xx'
		print (xx)

	inner ()
	print(xx)


outter()

print ('retrieve variable from Enclosed nested functions')
def outter_1():
	xx = 'outter xx'

	def inner_1():
		#xx = 'inner xx'
		print (xx)

	inner_1()
	print(xx)


outter_1()



print ('nonlocal variable alter Enclosed nested functions')
def outter_2():
	xx = 'outter xx'

	def inner_2():
		nonlocal xx
		xx = 'inner xx'
		print (xx)

	inner_2()
	print(xx)


outter_2()


xx = 'global xx'
print ('globalal variable alter Enclosed nested functions')
def outter_3():
	xx = 'outter xx'

	def inner_3():
		#nonlocal xx
		xx = 'inner xx'
		print (xx)

	inner_3()
	print(xx)


outter_3()
print (xx)


#global interpreter lock
print ('***multi thread in python***')
from random import random
from math import sqrt, pi

def compute_pi(n):
	ii, inside = 0, 0
	while ii < n:
		x = random()
		y = random()
		if sqrt(x*x + y*y) <= 1:
			inside += 1
		ii += 1
	ratio = 4.0 * inside / n
	return ratio

if __name__ == '__main__':
	mypi = compute_pi(10000000)
	print ('my pi: {0}, Error: {1}'.format(mypi, mypi - pi))





















