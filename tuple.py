# -*- coding: utf-8 -*-
# @Author: Song
# @Date:   2017-07-09 16:21:15
# @Last Modified by:   Song
# @Last Modified time: 2017-10-17 14:37:04

list = ['sky lake', 'tiger lake', 'cannon lake', 'ice lake', 'salt lake' ]
print (list)
print (len(list))
print (list[0])
print (list[4])
#last item use index: -1
print (list[-1])
#range of value 0 index
print (list[0:2])
#begin and end index can be omit with only one index specified
print (list[:3])
print (list[3:])
#append one element on list
list.append('tree lake')
print (list)
#add into specific location
list.insert(2, 'prairie lake')
print (list)
#merge list - list within list
list_1 = ['moon lake','star lake']
list_2 = ['bird lake', 'volcano lake']
list.append(list_1)
print (list)
list.insert(2, list_2)
print (list)
#add element into list
list.extend(list_2)
print (list)
#remove list
list.remove(list_2)
print (list)
list.remove(list_1)
print (list)
#pop only retrieve the last element
gpu = list.pop()
print (gpu)
#keep pop up last element in the list till it's empty
#reverse element order
list.reverse()
print (list)
#sort list
list.sort()
print (list)
#sort in decent order
list.sort(reverse=True)
print (list)
#sort the list without altering original order
s = sorted(list)
print (s)

num = [1.1, 1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9]
print (min(num))
print (max(num))
print (sum(num))

#find index
print (list.index('tree lake'))
#check element is in the list
print ('ice lake' in list)

#make a loop though the list item is advanced to next element at each loop
for item in list:
		print (item)


#index the element while iterating
for gpu in enumerate (list):
	print (gpu)


for index, gpu in enumerate (list):
	print (index, gpu)


#turn list elements into one string
s_list = ', '.join(list)
print (s_list)

h_list = ' - '.join(list)
print (h_list)

list = h_list.split(' - ')
print (list)

list = s_list.split(', ')
print (list)



#mutable non-mutable reference to the same mutable object which is static
#tuple can't be modified
list_3 = list

list[4] = 'art lake'
#verify 
print (list_3)
print (list)

#Immutable
tuple = ('tree lake', 'tiger lake', 'sky lake', 'salt lake', 'prairie lake', 'ice lake', 'cannon lake', 'bird lake')
tuple_1 = tuple

#tuple[4] = 'art lake'
print (tuple)
print (tuple_1)


#set not ordered threw away duplicates element
set = {'tree lake', 'tiger lake', 'sky lake', 'salt lake', 'prairie lake', 'ice lake', 'cannon lake', 'bird lake'}
print (set)

#empty list
empty_list = []
#empty_list = list()

#empty tuple
empty_tuple = ()
#empty_tuple = tuple ()

#empty set not work since its for dictionary
empty_set = {}
empty_set = ()


#duplicate element
set_1 = {'tree lake', 'tiger lake', 'sky lake', 'salt lake', 'prairie lake', 'ice lake', 'cannon lake', 'bird lake', 'tree lake', 'art lake', 'tone lake'}
print (set_1)

print(set_1.intersection(set))

print(set_1.difference(set))

print(set_1.union(set))


#dictionary hash table
#string, integer, list
manager = {'first':'sue', 'last':'smith', 'work':'AndreasSystems', 'pay': 90000, 'supervise':['dev_1', 'dev_2', 'dev_new']}
print (manager)
print (manager['pay'])
print (manager['supervise'])
#access key
print (manager.get('work'))

#add element use list prentace
manager['phone'] = '555-1212'
#access none existing key give return string
print (manager.get('phone', 'not in record'))
#update individual value
manager['last'] = 'dickinson'
print (manager)
#update entire dictionary
manager.update({'first':'sue', 'last':'johnson', 'work':'AndreasSystems', 'pay': 150000, 'supervise':['dev_1', 'dev_2', 'dev_new']})
print (manager)
#remove key
del manager['last']
print (manager)

#remove key
emp = manager.pop('supervise')
print (emp)

#loop keys only
#dict_keys
print(manager.keys())
#dict_keys
print(manager.values())
#item both key and valu
print(manager.items())

#abstract key
for keys in manager:
		print (keys)

#abstract key value pair
for key, value in manager.items():
	print (key, value)


list_5 = [8,5,2,6,7,1,9,4,3,0,7,1,0]
tuple = (8,5,2,6,7,1,9,3,0,7,1,0)
set = {8,5,2,6,7,1,9,3,0,7,1,0}
dic = {'first':'sue', 'last':'smith', 'work':'AndreasSystems', 'pay': 90000, 'supervise':['dev_1', 'dev_2', 'dev_new']}

print ('Sorted list variable: {}'.format(sorted(list_5)))
print ('reverse Sorted list : {}'.format(sorted(list_5, reverse = True)))
print ('Sorted list variable: {}'.format(list_5.sort()))
s_li = list_5.sort(reverse = True)
print ('Sorted variable: ', s_li)
print ('Original list variable: ', list_5)


#tuple can not be: tuple.sort()
print ('tuple Original variable: ', tuple)
print ('Sorted tuple: {}'.format(sorted(tuple)))
print ('reverse Sorted tuple : {}'.format(sorted(tuple, reverse = True)))


print ('dictionary Original variable: ', dic)
print ('Sorted hash key only: {}'.format(sorted(dic)))
print ('reverse Sorted tuple keys: {}'.format(sorted(dic, reverse = True)))


list_4 = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 3, 2, 1, 0]
print (list_4)
#sort with absolute value given as: key
print (sorted(list_4, key = abs))
print ('*****Slicing*****')
print (list_4[3:6])
print ('mixing negative index for slicing :')
print (list_4[1:-2])
print ('index default to the end :')
print (list_4[5:])
print ('index default to the beginning 0:')
print (list_4[:-3])
print ('index default to the entire list:')
print (list_4[:])
print ('specify the steps [start:ens:step]')
print (list_4[2:-2:2])
print ('negative step run reverse order :')
print (list_4[-2:3:-2])
print ('reverse the entire list with default indexes :')
print (list_4[::-1])


str_url = 'https://software.intel.com'
print (str_url)
print ('reverse the entire string with default indexes :')
print (str_url[::-1])
print ('get top level of url domain drop: .com ')
print (str_url[-4:])
print ('get url only without protocol :')
print (str_url[8:])
print ('get url body only :')
print (str_url[8:-4])



class employee:

	def __init__(self, first, last, pay, work):
		self.first = first
		self.last = last
		self.pay = pay
		self.work = work
		#self.email = first + '.' + last + '@' + work + '.com'

		#employee.num_of_emp += 1
		#logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))


	#format of the employee object at the print
	def __repr__(self):
		return "employee('{}','{}','{}','{}')".format(self.first, self.last, self.pay, self.work)


	
emp_1 = employee('John', 'Doe', 70000, 'TI')
emp_2 = employee('Steve', 'Smith', 30000, 'MGH')
emp_3 = employee('Jane', 'Doe', 90000, 'INTEL')

Employees = [emp_1, emp_2, emp_3]

#*********************************************
def last_sort(emp):
	return emp.last

def first_sort(emp):
	return emp.first

def pay_sort(emp):
	return emp.pay

def work_sort(emp):
	return emp.work



print ('last name Sorted dictionary :')
s_Emp = sorted(Employees, key = last_sort)
print (s_Emp)


print ('first name Sorted dictionary :')
s_Emp = sorted(Employees, key = first_sort)
print (s_Emp)


print ('pay rate Sorted dictionary :')
s_Emp = sorted(Employees, key = pay_sort)
print (s_Emp)


print ('pay rate Sorted dictionary :')
s_Emp = sorted(Employees, key = pay_sort, reverse = True)
print (s_Emp)


print ('work place Sorted dictionary :')
s_Emp = sorted(Employees, key = work_sort)
print (s_Emp)


#*********************************************
#yale lambda function
print ('lambda Sorted last dictionary :')
s_Emp = sorted(Employees, key = lambda e: e.last)
print (s_Emp)


print ('lambda first Sorted dictionary :')
s_Emp = sorted(Employees, key = lambda e: e.first)
print (s_Emp)


print ('lambda pay Sorted dictionary :')
s_Emp = sorted(Employees, key = lambda e: e.pay)
print (s_Emp)


print ('lambda work Sorted dictionary :')
s_Emp = sorted(Employees, key = lambda e: e.work)
print (s_Emp)



#*********************************************
#attributes as key for sorting
from operator import attrgetter

print ('attribute Sorted last dictionary :')
s_Emp = sorted(Employees, key = attrgetter('last'))
print (s_Emp)


print ('attribute Sorted first dictionary :')
s_Emp = sorted(Employees, key = attrgetter('first'))
print (s_Emp)


print ('attribute Sorted pay dictionary :')
s_Emp = sorted(Employees, key = attrgetter('pay'))
print (s_Emp)


print ('attribute Sorted work dictionary :')
s_Emp = sorted(Employees, key = attrgetter('work'))
print (s_Emp)




from collections import namedtuple


#RGB     R    G    B
color = (55, 155, 255)
#tuple
print ('RED :', color[0])
print ('GREEN :', color[1])
print ('BLUE :', color[0])


#dictionary
dic_color = {'red':55, 'green':155, 'blue':255}
print ('RED :', dic_color['red'])
print ('GREEN :', dic_color['green'])
print ('BLUE :', dic_color['blue'])


#namedtuple
Color = namedtuple('Color',['red', 'green', 'blue'])
color = Color(red = 55, green = 155, blue = 255)
#regular tuple
color = (55, 155, 255)
#     ->named<-
color = Color(55, 155, 255)

#regular tuple via index
print (color[0])
#access via name
print (color.red)

#define new color
white = Color(255, 255, 255)
#access blue of Color white
print (white.blue)
#no dot syntax in dictionary
#dictionary
print ('dictionary blue :')
print (dic_color['blue'])
#named tuple
print ('namedtuple blue with dot syntax:')
print (color.blue)



import itertools
print ("\n\n***********************************")
print ("Permutation vs. Combination")

combinations = itertools.combinations(list_4, 14)
for b in combinations:
	print (b)

count = 0
permutations = itertools.permutations(list_4, 2)
for p in permutations:
	print (p)
	count += 1
	print ([result for result in permutations if sum(result) < 0])	

print ('Total combination of permutations is: {}'.format(count))


count_1 = 0
combinations = itertools.combinations(list_5, 13)
for c in combinations:
	print (c)

permutations = itertools.permutations(list_5, 3)
for q in permutations:
	print (q)
	count_1 += 1
	print ([result11 for result11 in permutations if sum(result11) == 11])

print ('Total permutations number is: {}'.format(count_1))


#target = 'sample'
letter = 'abcdefghijklmnopqrstuvwxyz'
#letter = 'plmeas'

permutations = itertools.permutations(letter, 3)
combinations = itertools.combinations(letter, 3)
#ar = ''.join(itertools.permutations(letter, 1))

for ar in permutations :
	for br in combinations :	
		arr = ''.join(ar)
		brr = ''.join(br)
		#print (''.join(ar))
		print (arr)
		print (brr)
		#print (''.join(br))
		if arr == brr:
		#if ar == br:
			print ('Match Found!{}'.format(ar))
			break
		else:
			print ('No Match!')


