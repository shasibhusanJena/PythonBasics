# time complexity O(n) ?
# why r is i+1 in even size ?
# where we are checking if even or odd str ?
# ow to find best solution on leetcode ?
class Solution:
    def longestPalindrome(s:str):
        res = ""
        resLen = 0

        for i in range(len(s)):
            print("i value is",i)
            # Odd size palindrom
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                    print("odd res",res," resLen ",resLen)
                l -= 1
                r += 1

            # Even size palindrom
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                    print("even res", res, " resLen ", resLen)
                l -= 1
                r += 1

        return res

if __name__ == '__main__':
    res =Solution.longestPalindrome("abcbapqrmrqp")
    print(res)