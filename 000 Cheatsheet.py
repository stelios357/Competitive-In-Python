# 1. Sort Array according to A
array = []
A = []
array.sort(key=lambda i: A[i])

# 2. #Check wether a key in dict:
index = {}  # dict
arr = []  # keys
if arr[1] in index:
    pass

# 3. Decimal to bin:
n = 11
bin(n).replace("0b", "")


#4. All substrings of a string
test_str = "aman"
res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]

#5. Insert inplace:
import bisect
bisect.insort(arr, n)


# 6. Make/check lower / uper
str = "aaa"
str = str.lower()
str.isupper()

#7. Heap:
# Python code to demonstrate working of
# heapify(), heappush() and heappop()

# importing "heapq" to implement heap queue
import heapq

# initializing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))


#8. 2D array:
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]

#9.Sorting acc to another array:
arr.sort(key = lambda i:A[i])

#10. COmbination in Python:
from itertools import combinations
r = 2
list(combinations(arr, r))

#11. NCR:
from math import comb
comb(n,r)

#12. Subtract two lists:
difference = []
list1 = []
list2 = []
zip_object = zip(list1, list2)
for list1_i, list2_i in zip_object:
    difference.append(list1_i-list2_i)