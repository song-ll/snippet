# -*- coding: utf-8 -*-
# @Author: Song
# @Date:   2017-07-06 11:21:15
# @Last Modified by:   Song
# @Last Modified time: 2017-07-08 16:43:21

import sqlite3
from employees import employee #, developer, manager
from employees import developer
from employees import manager



emp_1 = employee('ice','lake',90000,'ti')
emp_2 = employee('Nitro','Genet',87000,'intel')

dev_1 = developer('hilda','probe',90000,'ti', 'PERL')
dev_2 = developer('excution','kernel',87000,'intel','RUBY')


dev_3 = developer('Zilda','Shmoo',150000,'ti', 'PERL')
dev_4 = developer('port scan','display', 87000,'intel','Python')



mgr_1 = manager('sue','smith','90000','AndreaSystems',[dev_1,dev_2])


print(emp_1.work)
print(emp_2.email)

print(dev_1.work)
print(dev_2.email)
	
#in memory database RAM only 
#conn = sqlite3.connect(':memory:')

#create file database
conn = sqlite3.connect('employee.db')
conn = sqlite3.connect('developer.db')


#create cursor for SQL execution
c = conn.cursor()

#create a table with SQL syntax  though dotstream for multiple lines inputs
c.execute("""CREATE TABLE employee (
			first text,
			last text,
			pay integer,
			work text
			)""")


c.execute("""CREATE TABLE developer (
			first text,
			last text,
			pay integer,
			work text,
			prog_lang text
			)""")



def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO employee VALUES (:first, :last, :pay, :work)",{'first': emp.first, 'last': emp.last, 'pay': emp.pay, 'work': emp.work})


def insert_dev(dev):
	with conn:
		c.execute("INSERT INTO developer VALUES (:first, :last, :pay, :work, :prog_lang)",{'first': dev.first, 'last': dev.last, 'pay': dev.pay, 'work': dev.work, 'prog_lang': dev.prog_lang})


def get_emps_by_name(last):
    c.execute("SELECT * FROM employee WHERE last = :last", {'last': last})
    return c.fetchall()


def get_devs_by_name(last):
    c.execute("SELECT * FROM developer WHERE last = :last", {'last': last})
    return c.fetchall()


def get_devs_by_proglang(prog_lang):
    c.execute("SELECT * FROM developer WHERE prog_lang = :prog_lang", {'prog_lang': prog_lang})
    return c.fetchall()

#does not update the pay for either emp nor dev in neither connect to database nor :memory:
def update_pay(dev, pay):
	with conn:
		c.execute("UPDATE developer SET pay = :pay  WHERE (first = :first AND last = :last)", {'first': dev.first, 'last': dev.last, 'pay': pay})
		#c.execute("UPDATE developer SET pay = :pay  WHERE (pay = :pay AND first = :first AND last = :last)", {'pay': pay, 'first': dev.first, 'last': dev.last})

#c.execute("SELECT * FROM employee WHERE work = :work", {'work': 'Amazon'})
def remove_emp(emp):
	with conn:
		c.execute("DELETE from employee WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})


def remove_dev(dev):
	with conn:
		c.execute("DELETE from developer WHERE first = :first AND last = :last", {'first': dev.first, 'last': dev.last})


insert_dev(dev_3)
insert_dev(dev_4)

print("program_language :")
devs = get_devs_by_proglang('Python')
print(devs)

print("pay :")
update_pay(dev_4, 99999)
print(dev_4.pay)

print(get_devs_by_name('Shmoo'))

remove_dev(dev_3)

print("name:")
devs = get_devs_by_name('Shmoo')
print(get_devs_by_name('Shmoo'))

print("***********************")


c.execute("INSERT INTO employee VALUES ('John','Robertson',700000,'Houston')")
c.execute("INSERT INTO employee VALUES ('Ken','Walsh',900000,'Boston')")
c.execute("INSERT INTO employee VALUES ('Adam','Khol',300000,'Amazon')")
#dev_1 = developer('hilda','probe',90000,'ti', 'PERL')
#dev_2 = developer('excution','kernel',87000,'intel','RUBY')


#stream formatting
c.execute("INSERT INTO employee VALUES ('{}','{}','{}','{}')".format(dev_1.first, dev_1.last, dev_1.pay, dev_1.work))
c.execute("INSERT INTO employee VALUES ('{}','{}','{}','{}')".format(dev_2.first, dev_2.last, dev_2.pay, dev_2.work))
c.execute("INSERT INTO employee VALUES ('{}','{}','{}','{}')".format(mgr_1.first, mgr_1.last, mgr_1.pay, mgr_1.work))


#place holder tuple
c.execute("INSERT INTO employee VALUES (?, ?, ?, ?)",(dev_1.first, dev_1.last, dev_1.pay, dev_1.work))
c.execute("INSERT INTO employee VALUES (?, ?, ?, ?)",(dev_2.first, dev_2.last, dev_2.pay, dev_2.work))
c.execute("INSERT INTO employee VALUES (?, ?, ?, ?)",(mgr_1.first, mgr_1.last, mgr_1.pay, mgr_1.work))


#dictionry as data structure
c.execute("INSERT INTO employee VALUES (:first, :last, :pay, :work)",{'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay, 'work': emp_1.work})
c.execute("INSERT INTO employee VALUES (:first, :last, :pay, :work)",{'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay, 'work': emp_2.work})
c.execute("INSERT INTO employee VALUES (:first, :last, :pay, :work)",{'first': mgr_1.first, 'last': mgr_1.last, 'pay': mgr_1.pay, 'work': mgr_1.work})


#emp_1 = employee('ice','lake',90000,'ti')
#emp_2 = employee('Nitro','Genet',87000,'intel')


#save the changes
conn.commit()
#close database
#conn.close()

print(emp_1.work)
print(emp_2.pay)

#c.execute("SELECT * FROM employee WHERE last = 'Walsh' ")
c.execute("SELECT * FROM employee WHERE work = 'intel' ")
print(c.fetchall())
#use tuple
c.execute("SELECT * FROM employee WHERE work = ?", ('ti',))
print(c.fetchall())
#dictionary
c.execute("SELECT * FROM employee WHERE work = :work", {'work': 'Amazon'})
print(c.fetchall())



#next row of result
#print(c.fetchone())

#row of list
#print(c.fetchmany(3))

#remining list all
print(c.fetchall())


conn.close()


