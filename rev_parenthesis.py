import collections

class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = list()
        dq = collections.deque()
        stck = collections.deque()
        stck = list()
        i = 0
        while (i < len(s) and s[i] != '('):
            ans.append(s[i])
            i += 1

        while (i < len(s) and s[i] != ')'):
            stck.append(s[i])
            i += 1

        i += 1

        if s.count('(') == 0:
            return s
        #print(stck[0])
        #print(stck[-1])
        #print(stck[0]=='(')
        while len(stck)>0 and stck.count('(')!= 0:
            print("in")
            #print(stck[-1] != '(')
            while (stck[-1] != '('):
                x = stck.pop()
                dq.append(x)
            if len(stck)>0:
                #print("in")
                stck.pop()

            while (len(dq) > 0):
               # print("in")
                x = dq.popleft()
                stck.append(x)

            while (i < len(s) and s[i] != ')'):
                stck.append(s[i])
                i += 1
                #print("in")
            i += 1
        ans.extend(stck)
        while (i < len(s)):
            ans.append(s[i])
            i += 1
        #print(ans)
        return ''.join(ans)

s1 = Solution()
print(s1.reverseParentheses("abcd(ef)(gh)"))

"fluao nbqyt sj"