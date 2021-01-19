# Backtracking is a DFS algorithm that "backtracks" when there are no available options 

# Example 1:
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