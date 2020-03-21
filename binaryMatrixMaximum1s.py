# python program to find row with 
# maximum 1 in row sorted binary 
# matrix 
 
# function for finding row with 
# maximum 1 
def findMax (arr, N): 
    row = 0
    j = len(arr[0]) - 1
    for i in range(N): 
        # find left most position 
        # of 1 in a row find 1st 
        # zero in a row 
        print(i)
        while (arr[i][j] == 1 and j >= 0): 
            row = i 
            j -= 1
          
    print("Row number = " , row + 1, 
         ", MaxCount = ", len(arr[0]) - j-1) 
  
# driver program 
arr = [ [0, 1, 1, 1],
        [0, 0, 0, 1], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0], 
        [0, 0, 0, 1] ] ;

print(range(len(arr)));
findMax(arr, len(arr)); 
  
# This code is contributed by Sam007 
