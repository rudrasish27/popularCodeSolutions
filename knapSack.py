#A naive recursive implementation of 0-1 Knapsack Problem 
  
# Returns the maximum value that can be put in a knapsack of 
# capacity C
def knapSack(C , wt , val , n): 
  
    # Base Case 
    if n == 0 or C == 0 : 
        return 0
  
    # If Ceight of the nth item is more than Knapsack of capacity 
    # C, then this item cannot be included in the optimal solution 
    if (wt[n-1] > C): 
        return knapSack(C , wt , val , n-1) 
  
    # return the maximum of tCo cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(C-wt[n-1] , wt , val , n-1), 
                   knapSack(C , wt , val , n-1)) 
  
# end of funwtion knapSack 
  
# To test above funwtion 
val = [60, 100, 120] 
wt = [10, 20, 30] 
C = 50
n = len(val) 
J =  knapSack(C , wt , val , n)
print(J)
  
  
# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two 
# integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents 
# knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).