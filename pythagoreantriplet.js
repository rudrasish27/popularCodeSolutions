// # Returns true if there is Pythagorean 
// # triplet in ar[0..n-1] 
function isTriplet(ar){ 
// 	# Square all the elemennts 
	for(var i=0; i<ar.length; i++){
		ar[i] = ar[i] * ar[i] 
	}
// 	# sort array elements 
	ar.sort((a,b)=>a-b); 

// 	# fix one element 
// 	# and find other two 
// 	# i goes from n - 1 to 2 
	for(i=ar.length-1; i>1; i--){ 
// 		# start two index variables from 
// 		# two corners of the array and 
// 		# move them toward each other 
		let j = 0
		let k = i - 1
		while (j < k){ 
// 			# A triplet found 
			if (ar[j] + ar[k] == ar[i]) 
				return true
			else{
				if(ar[j] + ar[k] < ar[i]) 
					j = j + 1
				else
					k = k - 1
			}
		}
	}
// 	# If we reach here, then no triplet found 
	return false
}
// # Driver program to test above function */ 
ar = [3, 1, 4, 6] 
if(isTriplet(ar))
	console.log("Yes") 
else
	console.log("No") 

/*(Use Sorting)
We can solve this in O(n2) time by sorting the array first.

1) Do square of every element in input array. This step takes O(n) time.

2) Sort the squared array in increasing order. This step takes O(nLogn) time.

3) To find a triplet (a, b, c) such that a2 = b2 + c2, do following.




Fix ‘a’ as last element of sorted array.
Now search for pair (b, c) in subarray between first element and ‘a’. A pair (b, c) with given sum can be found in O(n) time using meet in middle algorithm discussed in method 1 of this post.
If no pair found for current ‘a’, then move ‘a’ one position back and repeat step 3.2.
*/
