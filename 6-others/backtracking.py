# Backtracking is a DFS algorithm that "backtracks" when there are no available options 

# It's nice to think of backtracking in the following way:
# For example, to find permutations of [1,2,3]
# f([], [1,2,3]) --> f([1], [2,3]), f([2], [1,3]), f([3], [1,2]) 

# Example 1
# Find all well formed parentheses possible for n pairs  

class Example1:
    def generate_parenthesis(self, n):
        self.res = []
        self.backtrack("", n, n)
        return self.res 
    
    def backtrack(self, curr, l, r):
        if l == 0 and r == 0:
            self.res.append(curr)
        if r < l or l < 0 or r < 0:
            return 
        self.backtrack(curr + "(", l-1, r)
        self.backtrack(curr + ")", l, r-1)

# Example 2
# Find all permutations of an element 

class Example2:
    def permutations(self, nums):
        self.res = []
        self.backtrack([], nums)
        return self.res 
    
    def backtrack(self, curr, nums):
        if not nums:
            self.res.append(curr)
        for i in range(len(nums)):
            self.backtrack(curr + [nums[i]], nums[:i] + nums[i+1:])

# Example 3
# Find all subsets of an element
 
class Example3:
    def subsets(self, nums):
        self.res = []
        self.backtrack([], nums)
        return self.res 
    
    def backtrack(self, curr, nums):
        self.res.append(curr)
        for i in range(len(nums)):
            self.backtrack(curr + [nums[i]], nums[i+1:])
