# Push Dominoes
# Problem: https://leetcode.com/problems/push-dominoes/
# Solution:

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        n = len(dom)
        forces = [0] * n
        
        # Force from left to right
        force = 0
        for i in range(n):
            if dom[i] == 'R':
                force = n
            elif dom[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
            
        # Force from right to left
        force = 0
        for i in range(n - 1, -1, -1):
            if dom[i] == 'L':
                force = n
            elif dom[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
            
        res = []
        for f in forces:
            if f > 0:
                res.append('R')
            elif f < 0:
                res.append('L')
            else:
                res.append('.')
                
        return "".join(res)

if __name__ == "__main__":
    solution = Solution()
    
    d1 = ".L.R...LR..L.."
    print(f"Pushed dominoes '{d1}': {solution.pushDominoes(d1)}")
