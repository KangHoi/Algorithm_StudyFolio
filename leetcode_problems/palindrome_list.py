class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:  # ��Ʈ�� ���� ��� ĳ���Ͱ� �ϳ��� ��ȸ����
            if char.isalnum():
                strs.append(char.lower())
        # check palindrome
        while len(strs) > 1:  # ��� �� ö�� �̻� ������ �� pop�� ������
            if strs.pop(0) != strs.pop():  # pop(0)�� �����ϸ� �� ���� ���� ������ �� �ְ�, pop()�� �� ���� ���� ������
                return False
            
        return True