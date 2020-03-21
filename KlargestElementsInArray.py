''' Python3 code for k largest elements in an array'''
  
def kLargest(arr, k): 
    # Sort the given array arr in reverse  
    # order. 
    print(range(k))
    arr.sort(reverse = True) 
    # Print the first kth largest elements 
    for i in range(k): 
        print (arr[i])  
  
# Driver program 
arr = [1, 23, 12, 9, 30, 2, 50] 
# n = len(arr) 
k = 3
kLargest(arr, k) 
  
# k largest(or smallest) elements in an array | added Min Heap method