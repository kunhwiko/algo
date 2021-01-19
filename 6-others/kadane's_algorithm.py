# Kadane's Algorithm can be utilized in a maximum subarray problem
# It explains a relationship of local_max[i] =  max(arr[i], arr[i] + local_max[i-1])
# time: O(n)   space: O(1)

# Example 1:
# Find the max sum of a contiguous array 

def max_sum(nums):
	# assume a non empty array 
	curr = best = nums[0]
	for i in range(1, len(nums)):
		curr = max(nums[i], nums[i] + curr)
		best = max(curr, best)
	return best 


# Example 2:
# Find the max product of a contiguous array 

def max_product(nums):
	# assume a non empty array 
	curr_min, curr_max, best = nums[0]
	for i in range(1, len(nums)):
		if nums[i] < 0:
			curr_min, curr_max = curr_max, curr_min 
		curr_max = max(nums[i], nums[i] + curr)
		curr_min = min(nums[i], nums[i] + curr)
		best = max(best, curr_max)
	return best  
