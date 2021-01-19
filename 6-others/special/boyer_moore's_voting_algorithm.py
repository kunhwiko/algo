# Boyer Moore's Voting Algorithm is an efficient algorithm that finds a majority element
# a majority element means an element occurs more than n/2 times 
# we assume a majority element does exist 
# time: O(n)   space: O(1)

def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num 
        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate 