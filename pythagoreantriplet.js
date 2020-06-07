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

// # This code is contributed by Aditi Sharma 
