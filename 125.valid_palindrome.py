# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s: str) -> bool:
    l,r = 0, len(s) - 1
    while 1:
        while l <= r and not s[l].isalnum():
            l += 1
        while l <= r and not s[r].isalnum():
            r -= 1
        if (l >= r):
            return True
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
    

s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "
# s = "aa"
print(isPalindrome(s))
