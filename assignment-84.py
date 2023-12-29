filename = input("putfilename:")
fh = open(filename)
lst = list()

for line in fh:
    bosh = line.rstrip().split()
    for word in bosh:
        if word in lst:
            continue
        else:
            lst.append(word)
            
lst.sort()
print(lst)
