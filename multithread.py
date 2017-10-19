# -*- coding: utf-8 -*-
# @Author: Song
# @Date:   2017-07-29 00:09:39
# @Last Modified by:   Song
# @Last Modified time: 2017-07-29 12:48:18



import os
from os import getpid
from random import random
from math import sqrt, pi
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Pipe





def start_function_for_processes(n):
	result_sent_back_to_parent = n * n
	return result_sent_back_to_parent


def prove_existence():
	print (getpid())


print ('***multi thread in python***')


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


def ponger(pp, ss):
	count_1 = 0
	while count_1 < 200:
		msg = pp.recv()
		print('Process {0} got message: {1}'.format(os.getpid(), msg))
		pp.send(ss)
		count_1 += 1



if __name__ == '__main__':
	parent, child = Pipe()
	proc = Process(target = ponger, args = (child, 'ping'))
	proc.start()
	parent.send('pong')
	ponger(parent, 'pong')
	proc.join()



if __name__ == '__main__':
	p = Process(target = prove_existence, args = ())
	p.start()
	p.join()
	p2 = Process(target = prove_existence, args = ())
	p2.start()
	p2.join()




if __name__ == '__main__':
	mypi = compute_pi(10000000)
	print ('my pi: {0}, Error: {1}'.format(mypi, mypi - pi))




if __name__ == '__main__':
	with Pool(processes = 5) as p:
		results = p.map(start_function_for_processes, range(200), chunksize = 10)
	print(results)


	with Pool(4) as p:
		pis = p.map(compute_pi, [10000000] * 4 )
		print (pis)
		mypi = sum (pis)/4
		print ('my pi: {0}, Error: {1}'.format(mypi, mypi - pi))
	






















