# pip install numpy
import numpy as np
import time
import sys
# print(np.__version__)
# print(dir(np))

new_list = [1,2,3,4,5]
new_arr = np.array(new_list)

print(new_list)  # [1,2,3,4,5]
print(new_arr)  #[ 1 2 3 4 5 ]

print(type(new_list))   # <list>
print(type(new_arr))    # <numpy.ndarray>

a = np.array([10]) # zero-dimensional array
b = np.array([10,15]) # one-dimensional array
c = np.array([[14,24],[34,35]]) # two-dimensional array
d = np.array([[[3,5],[7,9]],[[2,4],[6,8]]]) #three-dimensional array

# to access number 4 in 3d array:
print(d[1][0][1])  # 4
print(d[1,0,1])  # 4

# to know number of dimensions of the array :

print(c.ndim)  # 2
print(d.ndim) # 3

# create custom array

custom_arr = np.array([11,22,33], ndmin=3)
print(custom_arr)  # [[[11 22 33]]]
print(custom_arr.ndim) # 3-dimensional array
print(custom_arr[0][0][0]) # 11
print(custom_arr[0,0,2]) # 33

# numpy or array will convert any heterogeneous list into list of either integer or string
# according to data inside:

myArr1 = np.array([1,2,"3","6",9,12]) # this will be converted to array of strings
print(myArr1)  #['1' '2' '3' '6' '9' '12']

myArr2 = np.array([1,2,3.14,4.25,6,7])
print(myArr2)   # [1.   2.   3.14 4.25 6.   7.  ]
# the arry will be converted to float because you have floats inside

print("#" * 50)

# let's compare time and performance between list and array in python:
elements = 100000

list_one = range(elements)
list_two = range(elements)

arr_one = np.arange(elements)
arr_two = np.arange(elements)

list_start = time.time()
list_result = [(n1*n2) for n1, n2 in zip(list_one,list_two)]
print(list_result)
print("#" * 50)
arr_start = time.time()
arr_result = arr_one * arr_two
print(arr_result)
print("#" * 50)
print(f"list time is : {time.time() - list_start}")
print(f"array time is : {time.time() - arr_start}")

##################################################
#  list time is : 0.11365032196044922
#  array time is : 0.0005776882171630859

print(arr_one.itemsize)  # 8
print(arr_one.size) # 100,000
print(f"bytes for all array: {(arr_one.itemsize)*(arr_one.size)}")  # 800,000

print(sys.getsizeof(list_one[10]))  # 28 , any number except 0 should return the same
print(len(list_one))
print(f"bytes for all list: {sys.getsizeof(list_one[10])*(len(list_one))}") # 280,000,0

# so array size = 800,000 vs list size = 280,000,0
# then, list size = array size * 3.5

# let's explore slicing in arrays :
print(arr_one[3:8])  # [3 4 5 6 7]
print(arr_one[:15])  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

arr_three = np.array([[[3,5],[7,9]],[[2,4],[6,8]],[[31,51],[71,19]],[[21,41],[61,81]]])
print(arr_three[:2])  # [[[3 5] [7 9]] [[2 4] [6 8]]]
print("#" * 50)
print(arr_three[:3, :2]) #  [[[ 3  5][ 7  9]][[ 2  4][ 6  8]][[31 51][71 19]]]
print("#" * 50)
print(arr_three[2:, :2, :1]) # [[[31][71]][[21][61]]]
print("#" * 50)
print(arr_three[2:, :2:2])  # [[[31 51]][[21 41]]]

# show array data type ;
print("#" * 50)
print(arr_three.dtype)  # int64
arr_four = np.array(["ahmed", "hassan", "ali", "abdelhameed"])
print(arr_four.dtype)  # <U11
# U11 because U = unicode and 11 is the longest character of a string which is "abdelhameed"
print("#" * 50)
arr_five = np.array([1,2,3], dtype=float) 
print(arr_five.dtype) # float64
print(arr_five) #[1. 2. 3.]
# you can change type by ("i" or "int" or int)
# you can change type by ("f" or "float" or float)
# to change type of array to another one, use this case :
arr_five = arr_five.astype("str")
print(arr_five)  # ['1.0' '2.0' '3.0']
print("#" * 50)
# ravel : flattened the multi-dimensional array to 1-dimensional array :
print(arr_three.ravel())  # [ 3  5  7  9  2  4  6  8 31 51 71 19 21 41 61 81]
print("#" * 50)
# shapes of array :
arr_three = np.array([[[3,5],[7,9]],[[2,4],[6,8]],[[31,51],[71,19]],[[21,41],[61,81]]])
print(arr_three.ndim) # 3-dimensional array
print(arr_three.shape)  # (4, 2, 2)
# this means you have 4 main lists includes 2 sub-arrays includes 2 elements in every list
print("#" * 50)
arr_six = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr_six.ndim) # 1 dimensional array
print(arr_six.shape) # (12,) 12 elements
print("#" * 50)
# reshape arr_six :
reshaped_arr_six = arr_six.reshape(3,4)
print(reshaped_arr_six.ndim)  # 2-dimensional
print(reshaped_arr_six.shape) # (3,2,2)
print(reshaped_arr_six)  # [[ 1  2  3  4][ 5  6  7  8][ 9 10 11 12]]
print("#" * 50)
three_dim_of_arr_six = arr_six.reshape(2,3,2)
print(three_dim_of_arr_six.ndim)  # 3-dimensional
print(three_dim_of_arr_six.shape) # (2,3,2)
print(three_dim_of_arr_six)  # [[[ 1  2][ 3  4][ 5  6]][[ 7  8][ 9 10][11 12]]]






