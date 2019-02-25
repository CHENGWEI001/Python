class Solution:
    """
    @param s: a string
    @return: nothing
    """

    def validPalindromeUtil(self, s, lo, hi, allowError, leftStr, rightStr):
        palStr = None
        while lo < hi:
            if s[lo] != s[hi]:
                if allowError == 0:
                    return None
                palStr = self.validPalindromeUtil(s, lo + 1, hi, allowError - 1, leftStr[:], rightStr[:])
                if palStr is not None:
                    return palStr
                palStr = self.validPalindromeUtil(s, lo, hi - 1, allowError - 1, leftStr[:], rightStr[:])
                if palStr is not None:
                    return palStr
                return None
            leftStr += s[lo]
            rightStr += s[hi]
            lo += 1
            hi -= 1
        mid = ""
        if lo == hi:
            mid = s[lo]
        return leftStr + mid + rightStr

def main():
    sol = Solution()
    str = "abcda"
    print(sol.validPalindromeUtil(str, 0, len(str) - 1, 3, "", ""))

if __name__ == "__main__":
    main()
