import sys, string, math
def reduceN( n, k1) :
	if k1 <= 0 : return n

	if n == 0 : return 10	# Fail
	p1 = reduceN(n//10, k1)*10 + n%10
	p2 = reduceN(n//10, k1-1)
	if p1 < p2 :
		return p1
	else :
		return p2

n,k1 = input().split()
n,k1 = int(n),int(k1)
print(reduceN(n,k1))
