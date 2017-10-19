# -*- coding: utf-8 -*-
# @Author: Song
# @Date:   2017-07-01 16:21:15
# @Last Modified by:   Song
# @Last Modified time: 2017-09-05 13:07:48

import logging
import employees
#logger.debug detailed information for diagnose and logger.debugging

#INFO confirmation of things are working as expected

#debug something unexpected happened software is still work as expected

#ERROR software has not been able to perform some function

#CRITICAL program may be unable to continue running 

#print('The imported module is: {}'.format(__name__))

logging.basicConfig(filename='console.log', level=logging.DEBUG)

def deco_logger(func):
	def log_func(*args):
		logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
		print(func(*args))
	return log_func



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f_formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('console.log')
file_handler.setFormatter(f_formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(f_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


#logging.basicConfig(filename='console.log', level=logging.INFO, format = '%(asctime)s:%(name)s:%(message)s')

logger.debug('The current module is: {}'.format(__name__))

def add(num1,num2):
    """addition"""
    #logger.debug("the sum is :")
    return num1+num2

def substract(num1,num2):
	"""substraction"""
	return num1-num2

def multiply (num1, num2):
	"""multiply"""
	return num1*num2

def divide(num1,num2):
	"""division"""
	try:
		result = num1/num2
	except ZeroDivisionError:
		#logger.error('Attempt divide by Zero')
		logger.exception('Attempt divide by Zero')
	else:
		return num1/num2
		 

num1 = 1024
num2 = 512 #0


print (' *** closure outer logger passing function in as argument *args *** ')
add_logger = deco_logger(add)
sub_logger = deco_logger(substract)
mul_logger = deco_logger(multiply)
div_logger = deco_logger(divide)
	
add_logger(num1, num2)
sub_logger(num1, num2)
mul_logger(num1, num2)
div_logger(num1, num2)



logger.info("The results are:")
    #return
#logger.debug("the sum is :")
#logger.debug('{} + {} = {}'.format(num1, num2, add(num1, num2)))
logger.debug("The answers are :")
logger.debug('addition:')
logger.debug('{} + {} = {}'.format(num1, num2, add(num1, num2)))
logger.debug("substraction:")
logger.debug('{} - {} = {}'.format(num1, num2, substract(num1, num2)))
logger.debug("multiply:")
logger.debug('{} * {} = {}'.format(num1, num2, multiply(num1, num2)))
logger.debug("division:")
logger.debug('{} / {} = {}'.format(num1, num2, divide(num1, num2)))



def main():
	print ('The imported module is: {}'.format(__name__))

if __name__ == '__main__':
	print ('Excuted the current modle')
else:
	print('Run from imported module...')
	main()


employees.main()