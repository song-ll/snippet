# -*- coding: utf-8 -*-
# @Author: Song
# @Date:   2017-06-24 16:21:15
# @Last Modified by:   Song
# @Last Modified time: 2017-07-09 02:59:59
import os
from datetime import datetime

#print (dir(os))
print("current working directory:")
print (os.getcwd())


print("changed working directory:")
os.chdir ('C:/Intel/cc_android_2016.0.036/bin/intel64')
print (os.getcwd())
print (os.listdir('C:/Intel/cc_android_2016.0.036/bin'))

os.chdir('C:/Python36/')
os.mkdir ('osModule/file')
os.rmdir ('osModule/file')
os.removedirs ('osModule/file')
os.makedirs ('osModule/file')
os.listdir ('C:/Python34/osModule')
os.chdir('C:/Python34/osModule')
print (os.getcwd())
print(os.listdir())

#os.rename('C:\Python34\intel.PNG','C:\Python34\intel.JPG')
print ('Logo file : intel.JPG has properties as:')
print (os.stat('C:\Python36\intel.JPG'))
modify_time = os.stat('C:\Python36\intel.JPG').st_mtime
create_time = os.stat('C:\Python36\intel.JPG').st_ctime
print (datetime.fromtimestamp(modify_time))
print (datetime.fromtimestamp(create_time))
print (modify_time)
print (create_time)

for dirpath, dirname, filenames in os.walk('C:/Users/Song/Desktop'):
	print ('Current path:', dirpath)
	print ('list directories: ', dirname)
	print ('list files under the directories:', filenames)

	os.chdir ('C:/Users/Song/Desktop')
	print (os.environ.get('Desktop'))

    #print (os.environ.get('HOME'))
	#file_path = os.path.join(os.environ.get(os.getcwd()), 'Meastro.sln')
	#file_path = os.path.join(os.environ.get(os.getcwd()), 'Meastro.sln')
	
	#print (file_path)

	print (os.path.splitext('C:/Ruby23/bin/comics.txt'))

	print (dir(os.path))

