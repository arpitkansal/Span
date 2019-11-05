def modulo_multiplicative_inverse(A, M):

    gcd, x, y = extended_euclid_gcd(A, M)
    if x < 0:
        x += M
    return x

def extended_euclid_gcd(a, b):

    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return [old_r, old_s, old_t]
A = 10
p = 3
for i in range(3,A+1):
    if (i%2==0):
        p = 3*(p+1)
    else:
        p = (p-1)*3

q = 3**A
M = 10**9 +7
r = modulo_multiplicative_inverse(q,M)
ans = (p%M * r) % M
print(ans)