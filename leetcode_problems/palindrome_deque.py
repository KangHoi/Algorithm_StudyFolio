from collections import deque
from typing import Deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        d: Deque = deque()
        
        for char in s:
            if char.isalnum():
                d.append(char.lower())
            
        while len(d) > 1:
            if d.pop() != d.popleft():
                return False
            
        return True