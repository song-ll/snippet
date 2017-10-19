# -*- coding: utf-8 -*-
# @Author: Song
# @Date:   2017-06-25 16:21:15
# @Last Modified by:   Song
# @Last Modified time: 2017-09-05 13:07:31


import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.console')
file_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)


logging.basicConfig(filename ='employee.console', level = logging.INFO, format = '%(asctime)s:%(name)s:%(message)s')


print('The imported module is: {}'.format(__name__))



class employee:

	raise_amount = 1.04
	num_of_emp = 0

	def __init__(self, first, last, pay, work):
		self.first = first
		self.last = last
		self.pay = pay
		self.work = work
		#self.email = first + '.' + last + '@' + work + '.com'

		employee.num_of_emp += 1
		logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))


	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	@property
	def email(self):
		return '{}.{}@{}.com'.format(self.first, self.last, self.work)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		logging.info('decommisioned')
		self.first = None
		self.last = None



	def pay_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	def __repr__(self):
		return "employee('{}','{}','{}','{}')".format(self.first, self.last, self.pay, self.work)
		#return "%s.%s(%d, %d, %d)" % (self.__class__.__module__,
		#							  self.__class__.__qualname__,
		#							  self._year,
		#							  self._month,
		#							  self._day)

	def __str__(self):
		return '{} - {} - {}'.format(self.fullname, self.email, self.work)
		#__str__ = isoformat

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		#return len(self.fullname())
		return len(self.fullname)


	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls,emp_str):
		first, last, pay, work = emp_str.split('-')
		return cls(first, last, pay, work)

	@classmethod
	def fromtimestamp(cls,t):
	#construct fron POSIX (time.time())
		y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
		return cls(y,m,d)

	@classmethod
	def today(cls):
		#construct from time.time()
		t = _time.time()
		return cls.fromtimestamp(t)


	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


import datetime
my_date = datetime.date(2016, 7, 14)

print(employee.is_workday(my_date))


import sys
print(sys.executable)
print(sys.version)


#@implements_to_string
#class HTTPException(Exception):
#	"""baseclass for all HTTP exception WSGI render default error page"""
#	code = None
#	description = None

#	def __init__(self, description = None, response = None):
#		Exception.__init__(self)
#		if description is not None:
#			self.description = description
#		self.response = response


class developer(employee):
	"""inheritent from employee class"""
	raise_amount = 1.10

	def __init__(self, first, last, pay, work, prog_lang):
		super().__init__(first, last, pay, work)
		#employee.__init__(self, first, last, pay, work)
		self.prog_lang = prog_lang

	#def __init__(self, arg):
	#	super(developer, self).__init__()
	#
	#	self.arg = arg

class manager(employee):
	"""docstring for manager"""
	raise_amount = 1.10

	def __init__(self, first, last, pay, work, employees = None):
		super().__init__(first, last, pay, work)

		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			#print ("--->", emp.fullname())
			print ("--->", emp.fullname)

	#def __init__(self, arg):
	#	super(manager, self).__init__()
	#	self.arg = arg



dev_1 = developer('hilda','probe',90000,'ti', 'PERL')
dev_2 = developer('excution','kernel',87000,'intel','RUBY')

emp_1 = employee('ice','lake',90000,'ti')
emp_2 = employee('Nitro','Genet',87000,'intel')

mgr_1 = manager('sue','smith','90000','AndreaSystems',[dev_1,dev_2])

employee.set_raise_amt(1.07)

emp_str_1 = 'John-Doe-70000-TI'
emp_str_2 = 'Steve-Smith-30000-MGH'
emp_str_3 = 'Jane-Doe-90000-INTEL'

#first, last, pay, work = emp_str_3.split('-')

new_emp_3 = employee.from_string(emp_str_3)


print(emp_1)
print(emp_2)


repr(emp_1)
str(emp_2)


logging.info(emp_1)
logging.info(emp_2)


logging.info(dev_1.email)
logging.info(dev_1.prog_lang)

logging.info('****************')
logging.info(dev_2.email)
logging.info(dev_2.prog_lang)

logging.info('****************')
logging.info(mgr_1.email)

mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_2)
mgr_1.print_emp()

mgr_1.remove_emp(dev_1)
mgr_1.print_emp()
#print(help(developer))
"""method resolution order"""
print(employee.raise_amount)

#emp_1.first = "ice"
#emp_1.last = "lake"
#emp_1.email = "song.li@ti.com"
#emp_1.pay = "90,000"

#emp_2.first = "Nitro"
#emp_2.last = "Genet"
#emp_2.email = "songx1.li@intel.com"
#emp_2.pay = "87,000"

print(emp_1.email)
print(emp_2.email)
print(new_emp_3.email)

print('****************')
emp_1.first = 'kepler'
print(emp_1.email)
#print(emp_1.fullname())
#print ('{} {}'.format(emp_1.first, emp_1.last))
#print ('{} {}'.format(emp_2.first, emp_2.last))

#print (emp_1.fullname())
#print (emp_2.fullname())

#print(employee.fullname(emp_1))
#print(employee.fullname(emp_2))

print ("employee pay:")
print(emp_1.pay)
emp_1.pay_raise()
print(emp_1.pay)

logging.info ("develpor pay:")
logging.info(dev_1.pay)
dev_1.pay_raise()
logging.info(dev_1.pay)

logging.info(emp_1.__repr__())
logging.info(emp_2.__str__())

logging.info(emp_1.__dict__)
logging.info(emp_2.__dict__)
#print(employee.__dict__)
print(employee.num_of_emp)


emp_1.set_raise_amt(1.07)


print(employee.pay_raise)
#print(emp_1.set_raise_amt)
logger.info(emp_1.pay)
logger.info(emp_2.email)
logger.info(new_emp_3.pay)

print("Is Sue a manager?")
print(isinstance(mgr_1, manager))
print("Is Sue an employee?")
print(isinstance(mgr_1, employee))
print("Is Sue a developer?")
print(isinstance(mgr_1, developer))

print("Is sue a manager?")
print(issubclass(developer, employee))
print("Is Sue an employee?")
print(issubclass(manager, employee))
print("Is Sue a developer?")
print(issubclass(manager, developer))


print(1+2)
print("dunder")
print(int.__add__(1,2))

print('a'+'b')
print("dunder")
print(str.__add__('a','b'))
#__repr__
#__str__
logger.info("sum of salary:")
logger.info(dev_1 + dev_2)

logger.info("name length is:")
logger.info(len(mgr_1))

emp_4 = employee('John','Smith', 52000,'MGH')
emp_4.fullname = 'Corey Schafer'
logger.info(emp_4)
logging.info(emp_4.email)
logging.info(emp_4.fullname)

logger.info('****************')
emp_4.first = 'Joan'
logger.info(emp_4)
logging.info(emp_4.email)
#print(emp_4.email())
logging.info(emp_4.fullname)

dev_2.fullname = 'Corey Schafer'
logger.info(dev_2)
logger.info(dev_2.email)
logger.info(dev_2.fullname)

logging.info(mgr_1.fullname)
del mgr_1.fullname
logging.info(mgr_1.fullname)


#checking module excution location
def main():
	print ('The imported module is: {}'.format(__name__))

if __name__ == '__main__':
	print ('Excuted the current modle')
else:
	print('Run from imported module...')
	main()