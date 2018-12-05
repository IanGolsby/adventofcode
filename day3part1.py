#NOT COMPLETED YET ALSO I'M WAY BEHIND OOPS

from time import time
t = time()

fabric = []

for y in range(1000):
  fabric.append([])
  for x in range(1000):
    fabric[y].append(0)

with open('inputday3') as f:
  cuts = [line.rstrip('\n') for line in f]

print(cuts)

print("Total time:", time()-t,"seconds")
