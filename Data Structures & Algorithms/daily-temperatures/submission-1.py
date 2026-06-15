class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        1. Brute Force
        
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break
        return res
        '''
        """
        2. Using Stack
        """
        n = len(temperatures)
        res = [0] * n
        stack = [] # pairs (temperature, index)

        for i, t in enumerate(temperatures): # i: index; t: temparature
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
            

        
        

                

