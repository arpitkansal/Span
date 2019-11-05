import sys
import math
sys.setrecursionlimit(77200)
def countP(n, k):
    dp = [[0 for i in range(k + 1)]
          for j in range(n + 1)]

    # Base cases
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(k + 1):
        dp[0][k] = 0

    # Fill rest of the entries in
    # dp[][] in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if (j == 1 or i == j):
                dp[i][j] = 1
            else:
                dp[i][j] = (j * dp[i - 1][j] +
                            dp[i - 1][j - 1])

    return dp[n][k]


def getSubsets(k, n, arr):
    ls = []
    arr2 = set(arr)
    for n in arr2:
        while n % 2 == 0:
            ls.append(2)
            n = n / 2

        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3, int(math.sqrt(n)) + 1, 2):

            # while i divides n , print i ad divide n
            while n % i == 0:
                ls.append(i)
                n = int(n / i)

            # Condition if n is a prime
        # number greater than 2
        if n > 2:
            ls.append(int(n))
    ps = set(ls)
    ps2 = list(ps)
    primeSum = 0
    for i in ls:
        primeSum += i

    ans = countP(primeSum, k)
    return primeSum

print(getSubsets(3,3,[1,2,6]))
print(countP(7,2))
