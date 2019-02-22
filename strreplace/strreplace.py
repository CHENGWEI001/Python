class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        # return self.stringReplaceJiuzhang(a, b, s)
        return self.stringReplaceMy(a, b, s)
    def stringReplaceJiuzhang(self, a, b, s):
        # Write your code here
        seed = 33
        mod = 1000000007
        ans = 0
        mxLen = -1
        aHash = []
        sHash = []
        base = []
        for i in a:
            ans = 1
            mxLen = max(mxLen, len(i))
            for j in i:
                ans = (ans * seed + ord(j) - ord('a')) % mod
            aHash.append(ans)
        ans = 1
        sHash.append(ans)
        mxLen = max(mxLen, len(s))
        for i in s:
            ans = (ans * seed + ord(i) - ord('a')) % mod
            sHash.append(ans)
        ans = 1
        base.append(ans)
        for i in range(mxLen):
            ans = ans * seed % mod
            base.append(ans)
        ret = [i for i in s]
        i = 0
        while i < len(s):
            maxLen = -1
            index = 0
            for j in range(len(a)):
                lenaj = len(a[j])
                l = i + 1
                r = i + lenaj
                if r > len(s):
                    continue
                sHashValue = (sHash[r] - base[r - l + 1] * sHash[l - 1] % mod + mod) % mod
                aHashValue = (aHash[j] - base[lenaj] + mod) % mod
                print("i:%d, j:%d, sHashCode:%d, aHash[%d]:%d"%(i, j, sHashValue, j, aHashValue))
                if sHashValue == aHashValue and lenaj > maxLen:
                    maxLen = lenaj
                    index = j
            if maxLen != -1:
                for j in range(maxLen):
                    ret[i + j] = b[index][j]
                i = i + maxLen - 1
            i = i + 1
        return "".join(ret)
    def stringReplaceMy(self, a, b, s):
        # declare hash constant
        # SEED = 31
        # BASE = 1000000
        SEED = 33
        BASE = 1000000007

        # build hashcode for A, and record maxLen of A
        aHash = []
        maxLen = 0
        for str in a:
            hashCode = 0
            maxLen = max(maxLen, len(str))
            for c in str:
                hashCode = (hashCode * SEED + ord(c) - ord('a')) % BASE
            aHash.append(hashCode)

        # build hashcode for s
        sHash = [] # sHash[i] : hash code for s[:i+1]
        hashcode = 0
        for c in s:
            hashcode = (hashcode * SEED + ord(c) - ord('a')) % BASE
            sHash.append(hashcode)

        # build SEED ^ M table
        powerM = [1]
        for i in range(maxLen):
            # powerM = powerM + [powerM[-1] * SEED % BASE]
            val = powerM[-1] * SEED % BASE
            powerM.append(val)

        ret = list(s)

        # looping
        i = 0
        while i < len(s):
            maxLen = 0
            maxj = 0
            for j in range(len(a)):
                lenj = len(a[j])
                if (len(s)-i < lenj or lenj < maxLen):
                    continue
                sHashCode = (sHash[i+lenj-1] \
                - ((sHash[i-1] if i > 0 else 0) * powerM[lenj] % BASE)) % BASE
                if sHashCode < 0:
                    sHashCode += BASE
                # print("i:%d, j:%d, sHashCode:%d, aHash[%d]:%d"%(i, j, sHashCode, j, aHash[j]))
                #if sHashCode == aHash[j] and s[i:i+lenj] == a[j]:
                if sHashCode == aHash[j]:
                    if lenj > maxLen:
                        maxLen = lenj
                        maxj = j
            if maxLen > 0:
                for k in range(maxLen):
                    ret[i+k] = b[maxj][k]
                i += maxLen
            else:
                i += 1
        return "".join(ret)

    def stringReplaceUsingDict(self, a, b, s):
        # build up hashtable
        ht = {}
        sizeSet = set()
        for i in range(len(a)):
            ht[a[i]] = i
            sizeSet.add(len(a[i]))
        sizeList = sorted(list(sizeSet), reverse=True)
        print(sizeList)


        # first loop is from left
        # second loop is for each left, loop from right to check substr of s
        i = 0
        while i < len(s):
            for l in sizeList:
                if len(s)-i < l:
                    continue
                if s[i:i+l] in ht:
                    s = s[:i] + b[ht[s[i:i+l]]] + s[i+l:]
                    i += l-1
                    break
            i += 1
        return s
def main():
  print("hello!")
  with open("11.in") as file:
      lines = [line.strip() for line in file]
  arr = lines[0][1:-1].split(',')
  a = [l.strip('\"') for l in arr]
  arr = lines[1][1:-1].split(',')
  b = [l.strip('\"') for l in arr]
  s = lines[2][1:-1]
  # print(a)
  # print(b)
  # print(s)

  sol = Solution()
  print(sol.stringReplace(a, b, s))

if __name__ == "__main__":
    main()