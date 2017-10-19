import random
import time
import copy

size1 = 100
size2 = 10000
size3 = 1000000

span = 1000000
threshold = 20



#---------------------------------------
#---------------------------------------
# Bubble Sort is slowest in all format except identifying already sorted and passing with exit the loop
#
# quick sort is faster than sort
# 
# Insertion Sort is faster than Selection Sort except reverse sorted order
#
# Quick Sort is faster than Merge Sort
#
#---------------------------------------
#---------------------------------------
#
# two layers of nested loops
# slow sort O(n^2)
# '-1' index step for element compare and shifted to the left
# skip the element which is already in its correct position
# 
#   temp = a
#   a = b
#   b = temp
#---------------------------------------

# not optimized, equiv to while version below, but uses for loop

def insertion_sort1(A):
    #the first element at index 0 is considered sorted and starts from index 1
	for i in range(1, len(A)):
        # '-1' index step for element compare and shifted to the left
		for j in range(i-1, -1, -1):

			if A[j] > A[j+1]:

				A[j], A[j+1] = A[j+1], A[j]
            # skip the element which is already in its correct position
			else:

				break



# not optimized, equiv to break version, but uses while loop		

def insertion_sort2(A):

	for i in range(1, len(A)):
		#where nested loop starts
		j = i-1
		#loop index
		while A[j] > A[j+1] and j >= 0:

			A[j], A[j+1] = A[j+1], A[j]
            # '-1' index step for element compare and shifted to the left
			j -= 1



# optimized - shifts instead of swapping		
#   temp = a
#   a = b
#   b = temp
def insertion_sort3(A):

	for i in range(1, len(A)):

		curNum = A[i]

		k = 0

		for j in range(i-1, -2, -1):

			k = j

			if A[j] > curNum:

				A[j+1] = A[j]

			else:

				break

		A[k+1] = curNum

				

#---------------------------------------
#
# Selection Sort
#
# two layers of nested loops
# slow sort O(n^2)
# inner (i = 0 to len(A)) ¦ outer loop (j = i+1 to len(A))
# average case: O(nlog(n))
# iterate though the entire list to identify the smallest element
# swap into the left most first position of unsorted list
# tracking the sorted list via index 'i'
# increment compare index of 'j'
# 
#---------------------------------------			

def selection_sort(A):

	for i in range (0, len(A) - 1):

		minIndex = i

		for j in range (i+1, len(A)):

			if A[j] < A[minIndex]:

				minIndex = j

		if minIndex != i:

			A[i], A[minIndex] = A[minIndex], A[i]



#---------------------------------------

# Bubble Sort
#
# slowest in all format except identifying already sorted and passing with exit the loop
#
# initialize two indexes for comparison
# two layers of nested loops
# inner (i = 0 to n-1) ¦ outer loop (j = 0 to n-1-i)
# swap elements into increasing order
# start from beginning of the list again
# slow sort O(n^2)
#---------------------------------------

# not optimized			

def bubble_sort1(A):

	for i in range (0, len(A) - 1):

		for j in range (0, len(A) - i - 1):

			if A[j] > A[j+1]:

				A[j], A[j+1] = A[j+1], A[j]

				

# optimized to exit if no swaps occur		

def bubble_sort2(A):

	for i in range (0, len(A) - 1):

		done = True

		for j in range (0, len(A) - i - 1):

			if A[j] > A[j+1]:

				A[j], A[j+1] = A[j+1], A[j]

				done = False

		if done:

			return



#---------------------------------------

# Merge Sort
# big O analysis of run time
# recursive on list
# divide and conquer algorhim
# very efficient for large number of data set
# log(n) merge step each step doube the list size
# must look at each element
# average case: O(nlog(n)) => log2(8) = 3
# select middle length of the list
# bring down into L and R lists
# iterate through two sorted list to pick the smaller one push into merge list
# incrementing index of list which pushed element to merge
#
#---------------------------------------				

def merge_sort(A):
    #recursive on list
	merge_sort2(A, 0, len(A)-1)

	

def merge_sort2(A, first, last):

	if last-first < threshold and first < last:

		quick_selection(A, first, last)

	elif first < last:
        #index
		middle = (first + last)//2
        #break into half at middle
		merge_sort2(A, first, middle)

		merge_sort2(A, middle+1, last)
        # merge elements from two sorted lists
		merge(A, first, middle, last)

		

def merge(A, first, middle, last):
    #index of left half of list
	L = A[first:middle]
    #index of right half of list
	R = A[middle:last+1]
    #signal EndOfValue
	L.append(999999999)
	#signal EndOfValue
	R.append(999999999)
    # initialize indexes
	i = j = 0

	

	for k in range (first, last+1):
        #compare elements of the two lists 
		if L[i] <= R[j]:
            #assign smaller element into sorted merge list
			A[k] = L[i]
            #incrementing L list index
			i += 1

		else:
            #assign smaller element into sorted merge list
			A[k] = R[j]
            #incrementing R list index
			j += 1

#---------------------------------------

# Quick Sort
#
# big O analysis of run time
# compare every number to PIVOT 
# left partition:  x < pivot
# right partition: y > pivot
# select PIVÔT is key to split the list in half and perfermance
# median of three(First¦Last¦Middle)
# random chose pivot O(nlog(n))
# swap pivot into first position
# assign a border 
# start pivot comparison¦swap from element after border
# advance both border and compare pointers
# kept comparison & swap till end of list
# swap pivot (at the first) into current border position
# recursive on both left partition and right partition respectively till two elements left
# divide and conquer algorhim
# very efficient for large number of data set
# average case: O(nlog(n))
# worst case:   O(n^2)
#---------------------------------------
    #user interface list A
def quick_sort(A):
    #recursive on list
	quick_sort2(A, 0, len(A)-1)

	

def quick_sort2(A, low, hi):
    
	if hi-low < threshold and low < hi:
        #median of three(First¦Last¦Middle) 
        #small data set use selection sort for performance
		quick_selection(A, low, hi)

	elif low < hi:
        #partition function return pivot median of three(First¦Last¦Middle)
		p = partition(A, low, hi)
        #recursive on left partition of pivot 
		quick_sort2(A, low, p - 1)
        #recursive on right partition of pivot
		quick_sort2(A, p + 1, hi)

	

def get_pivot(A, low, hi):
    #index
	mid = (hi + low) // 2
    #value selection as border
	s = sorted([A[low], A[mid], A[hi]])
    
	if s[1] == A[low]:

		return low

	elif s[1] == A[mid]:

		return mid

	return hi

	

def partition(A, low, hi):

	pivotIndex = get_pivot(A, low, hi)
    #for each comparison
	pivotValue = A[pivotIndex]
    #swap pivot to left most
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
    #initialize border
	border = low



	for i in range(low, hi+1):
        #pivot as reference in list iteration
		if A[i] < pivotValue:
            #advance both border and compare pointers
			border += 1
            #swap with border till end of list
			A[i], A[border] = A[border], A[i]
    #swap pivot with border position
	A[low], A[border] = A[border], A[low]


    #for pivot
	return (border)

	

def quick_selection(x, first, last):

	for i in range (first, last):
        #partition
		minIndex = i

		for j in range (i+1, last+1):

			if x[j] < x[minIndex]:

				minIndex = j

		if minIndex != i:
            #swap
			x[i], x[minIndex] = x[minIndex], x[i]

	

#--------------RANDOM ORDER----------------------

#------------------------------------------------

# size = 100

#------------------------------------------------

print("\nRandom Order Input\n---------------------------------")
print("\nTime in milliSeconds\n---------------------------------")


w = [random.randint(0, span) for a in range(0, size1)]

t1 = time.clock()

insertion_sort3(w)

print("Insertion Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size1)]

t1 = time.clock()

selection_sort(w)

print("Selection Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size1)]

t1 = time.clock()

bubble_sort2(w)

print("Bubble Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size1)]

t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size1)]

t1 = time.clock()

quick_sort(w)

print("Quick Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size1)]

t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size1),"): ", (time.clock()-t1) * 1000)
print("Tim Sort is Python build-in sorting algorithm combine Merge sort and Inserting sort.")
#------------------------------------------------

# size = 10,000

#------------------------------------------------

w = [random.randint(0, span) for a in range(0, size2)]

t1 = time.clock()

insertion_sort3(w)

print("Insertion Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size2)]

t1 = time.clock()

selection_sort(w)

print("Selection Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size2)]

t1 = time.clock()

bubble_sort2(w)

print("Bubble Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size2)]

t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size2)]

t1 = time.clock()

quick_sort(w)

print("Quick Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size2)]

t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

#------------------------------------------------

# size = 1,000,000

#------------------------------------------------

w = [random.randint(0, span) for a in range(0, size3)]

t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size3)]

t1 = time.clock()

quick_sort(w)

print("Quick Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, span) for a in range(0, size3)]

t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



# ----------------ALREADY SORTED-----------------

#------------------------------------------------

# size = 10,000

#------------------------------------------------

print("\nAlready Sorted Input\n---------------------------------")
print("Check and pass through the already¦partial sorted elements to exit loop\n---------------------------------")


w = [a for a in range(0, size2)]

t1 = time.clock()

insertion_sort3(w)

print("Insertion Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



t1 = time.clock()

selection_sort(w)

print("Selection Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



t1 = time.clock()

bubble_sort2(w)

print("Bubble Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



t1 = time.clock()

quick_sort(w)

print("Quick Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

#------------------------------------------------

# size = 1,000,000

#------------------------------------------------

w = [a for a in range(0, size3)]

t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



t1 = time.clock()

quick_sort(w)

print("Quick Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



# ----------------REVERSE SORTED-----------------

#------------------------------------------------

# size = 10,000

#------------------------------------------------

print("\nReverse Sorted order\n---------------------------------")
print("\nReverse Already Sorted order\n---------------------------------")


w = [a for a in range(0, size2)]

w.reverse()

t1 = time.clock()

insertion_sort3(w)

print("Insertion Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [a for a in range(0, size2)]

w.reverse()

t1 = time.clock()

selection_sort(w)

print("Selection Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [a for a in range(0, size2)]

w.reverse()

t1 = time.clock()

bubble_sort2(w)

print("Bubble Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [a for a in range(0, size2)]

w.reverse()

t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [a for a in range(0, size2)]

w.reverse()

t1 = time.clock()

#quick_sort(w)

print("Quick Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)
print("Quick Sort(size=", str(size2),": maximum recursion depth exceeded in comparison")


w = [a for a in range(0, size2)]

w.reverse()

t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

#------------------------------------------------

# size = 1,000,000

#------------------------------------------------

w = [a for a in range(0, size3)]

w.reverse()

t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



w = [a for a in range(0, size3)]

w.reverse()

t1 = time.clock()

#quick_sort(w)

print("Quick Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)
print("Quick Sort(size=", str(size3),": maximum recursion depth exceeded in comparison")


w = [a for a in range(0, size3)]

w.reverse()

t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



#--------------RANDOM ORDER, MANY DUPLICATES------------------

#------------------------------------------------

# size = 10,000

#------------------------------------------------

print("\nRandom Order Input with Many Duplicate Values\n---------------------------------")



w = [random.randint(0, size2//10) for a in range(0, size2)]

t1 = time.clock()

insertion_sort3(w)

print("Insertion Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, size2//10) for a in range(0, size2)]

t1 = time.clock()

selection_sort(w)

print("Selection Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0,size2//10) for a in range(0, size2)]

t1 = time.clock()

bubble_sort2(w)

print("Bubble Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, size2//10) for a in range(0, size2)]

t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, size2//10) for a in range(0, size2)]

t1 = time.clock()

quick_sort(w)

print("Quick Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, size2//10) for a in range(0, size2)]

t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size2),"): ", (time.clock()-t1) * 1000)

#------------------------------------------------

# size = 1,000,000

#------------------------------------------------

w = [random.randint(0, size2//10) for a in range(0, size3)]

t1 = time.clock()

merge_sort(w)

print("Merge Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, size2//10) for a in range(0, size3)]

t1 = time.clock()

#quick_sort(w)

#print("Quick Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)



w = [random.randint(0, size2//10) for a in range(0, size3)]

t1 = time.clock()

w.sort()

print("Tim Sort(size=", str(size3),"): ", (time.clock()-t1) * 1000)