class Solution(object):
    def calPoints(self, operations):
        stack = []
        
        for i in operations:
            if i not in ["C", "D", "+"]:
                stack.append(int(i))
            else:
                s = len(stack)
                if i == "+":
                    if s >= 2: 
                        stack.append(stack[-1] + stack[-2])
                
                elif i == "C":
                    if s > 0: 
                        stack.pop()
                
                elif i == "D":
                    if s > 0: 
                        stack.append(2 * stack[-1])
        
        return sum(stack)
