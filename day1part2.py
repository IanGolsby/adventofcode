import time as t
time = t.time()
z = [0]
t = True
with open('input') as f:
    xs = list(f)
    x=[]
    for i in range(500):
        x.extend(xs)
    if t:
        for L in range(len(x)):
            old = z[L]
            new = x[L]
            z.append(old+(int(new[0:len(new)])))
            for n in range(len(z)-2):
                if z[n]==z[len(z)-1]:
                    print("THE ANSWER IS: "+str(z[n]))
                    t = False
print(t.time()-time)
