# Sliding Window "slides a window" of size k through an array from left to right

# Example 1:
# Find the max sum of a size k subarray 

def max_subarray(nums, k):
	curr = best = sum(nums[:k])
	for i in range(1, len(nums)-k+1):
		curr -= nums[i-1]
		curr += nums[i+k-1]
		best = max(best, curr)
	return best 


# Example 2:
# Find the longest substring without repeating characters 

def longest_nonrepeat_substring(s):
	indices = {}
	start = longest = 0
	for i in range(len(s)):
		if s[i] in indices and start <= indices[s[i]]:
			start = indices[s[i]] + 1
		indices[s[i]] = i
		longest = max(longest, i-start+1)
	return longest 

