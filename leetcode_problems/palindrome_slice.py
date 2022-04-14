from collections import deque
from typing import Deque, Reversible

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = Reversible.sub('[^a-z0-9', '', s)
        return s == s[::-1]