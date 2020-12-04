import twophase_enum as tpe
import twophase_convert as tpc

def c(n, k):
    """Binomial coefficient [n choose k]."""
    if n < k:
        return 0
    if k > n // 2:
        k = n - k
    s, i, j = 1, n, 1
    while i != n - k:
        s *= i
        s //= j
        i -= 1
        j += 1
    return s
	
def phase_one(c):
	tpc.convert(c)
	return c
