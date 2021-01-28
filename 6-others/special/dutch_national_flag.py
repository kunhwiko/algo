# Dutch National Flag originates from arranging balls of 3 different colors together into same colored clusters.
# Where counting sort takes time O(n) space O(n), this algorithm reduces the space to O(1) 

def dutch_national_flag(nums):
    ptr, ptr0, ptr2 = 0, 0, len(nums)-1 
    
    while ptr <= ptr2:
        if nums[ptr] == 0:
            nums[ptr], nums[ptr0] = nums[ptr0], nums[ptr]
            ptr += 1
            ptr0 += 1
        elif nums[ptr] == 2:
            nums[ptr], nums[ptr2] = nums[ptr2], nums[ptr]
            ptr2 -= 1
        else:
            ptr += 1
    