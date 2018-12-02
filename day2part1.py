from time import time
t = time()

IDs=[]
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

num_with_2 = 0
num_with_3 = 0

with open('inputday2') as f:
    original_IDs=list(f)

for ID in original_IDs:
    IDs.append([ID[:len(ID)-1], 0, 0])

for ID in IDs:
    for letter in letters:
        num = 0
        for character in ID[0]:
            if character == letter:
                num += 1
        if num == 2:
            ID[1] = 1
        if num == 3:
            ID[2] = 1
    if ID[1] == 1:
        num_with_2 += 1
    if ID[2] == 1:
        num_with_3 += 1

print("Number with 2:",num_with_2)
print("Number with 3:",num_with_3)
print("Checksum:",num_with_2*num_with_3)

print("The program took",time()-t, "seconds to run.")
