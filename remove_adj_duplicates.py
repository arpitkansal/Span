import collections
class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        s = collections.deque(S)
        s.append('0')
        count = 0
        while (len(s) > 1 and count != len(s)):

            if s[0] == s[1]:
                s.popleft()
                s.popleft()
                count = 0
            else:
                s.append(s.popleft())
                count += 1
            print(s)
        while (s[-1] != '0'):
            s.append(s.popleft())
        s.remove('0')
        return ''.join(s)