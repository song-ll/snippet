# -*- coding: utf-8 -*-
# @Author: Song
# @Date:   2017-06-30 16:21:15
# @Last Modified by:   Song
# @Last Modified time: 2017-08-01 14:31:55

import os
# File descriptor

# context manager

os.chdir('C:/Ruby23/bin')
print (os.getcwd())
print (dir(os))

for ff in os.listdir():
	#if ff == '.DS_Store':
	#	continue

	file_name, file_ext = os.path.splitext(ff)
	print(file_name)

#f_title, f_course, f_number = file_name.split('-')
#print('{}-{}-{}{}}'.format(f_number, f_course, f_title, file_ext))

#remove white space
#f_title = f_title.strip()
#f_course = f_course.strip()
#f_number = f_number.strip()

#remove number sign
#f_number = f_number.strip()[1:]

#pad the number for sort
#f_number = f_number.strip()[1:].zfill(2)


#print('{}-{}-{}{}}'.format(f_number, f_course, f_title, file_ext))
#print('{}-{}{}}'.format(f_number, f_title.strip(), file_ext.strip()))

#new_name = '{}-{}{}'.format(f_num, f_title, file_ext)

#os.rename(fn, new_name)



with open('C:/Python36/test.txt', "r+") as f:


    f = open('C:/Python36/test.txt', "r+")
   


print(f.read(100))
print("****************")
f_content = f.read()
print(f_content)
print("****************")
f_contentLine = f.readline()
print(f_contentLine, end=' ')

print("****************")
f_contentLines = f.readlines()
print(f_contentLines, end=' ')
print(f_contentLines)

print("****************")
# for line in f:
#   size_to_read = 9
#   f_contentLine = f.readline(size_to_read)
#    print(f_contentLine, end=' ')

print("****************")
f_contentLine = f.readline(100)

while len(f_contentLine) > 8:

    print(f_contentLine, end='')
    f_contentLine = f.readline(8)
    print(f.tell())

    print(f.seek(9))

    f_contentLine = f.readline(8)
    print(f_contentLine)

# print(f.readline(), end=' ')
print(f.name)
print(f.mode)
f.close()
print(f.closed)




#with open('C:/Python34/LICENSE.txt', "r+") as rf:
with open('C:/Users/Song/Pictures/2014-10-11/logo.PNG', "rb") as rf:
	with open('C:/Python36/Intel.PNG',"wb") as wf:
	#with open('C:/Python34/start.txt',"wb") as wf:
		for line in rf:
			wf.write(line)

			chunk_size = 4096
			rf_chunk = rf.read(chunk_size)
			while len(rf_chunk) > 0:
				wf.write(rf_chunk)
				rf_chunk = rf.read(chunk_size)
	


############################################################################

infile = "inputFile.txt"

outfile = "outputFile.txt"



# print each line, as read in

with open(infile) as f1:

	for line in f1:

		print (line)



print ("\n*******************")



# print each line, stripping last newline character

with open(infile) as f1:

	for line in f1:

		print (line[:-1])



print ("\n*******************")

		

# print makes only (first word of each line)

with open(infile) as f1:

	for line in f1:

		row = line.split(",")

		print(row[0])



print ("\n*******************")

		

# print each line as a formatted list

with open(infile) as f1:

	for line in f1:

		row = line.split(",")

		print(row[0] + "\n-----------------")

		for i in range(1, len(row)):

			print(row[i])



print ("\n*******************")

			

# add each line to a list

cars = list()

with open(infile) as f1:

	for line in f1:

		row = line.split(",")

		cars.append(row)

	print(cars[0][0])

	

# write Makes only to outputFile

with open(outfile, 'a') as f2:

	for car in cars:

		f2.write(car[0] + "\n")



# write list of row-lists to outputFile

with open(outfile, 'a') as f2:

	for car in cars:

		f2.write(str(car) + "\n")

		