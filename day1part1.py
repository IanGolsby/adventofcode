import time as t
s = t.time()
z = 0
with open('input') as f:
	x = list(f)
	for l in x:
		z+=int(l[0:len(l)-1])
		print(z)
print(t.time()-s)

#	runtime: about 4.2 seconds :\
