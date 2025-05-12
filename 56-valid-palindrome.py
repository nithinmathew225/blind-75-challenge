class Solution:
    def isPalindrome(self, s: str) -> bool:
        # length = len(s)
        # is_palindrome = True
        # if length > 1:
        #     first = 0
        #     last = length - 1
        #     while first != last :
        #         if s[first] == s[last]:
        #             first += 1
        #             last -= 1
        #         else :
        #             is_palindrome = False
        #             break
        # return is_palindrome
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


                

        
