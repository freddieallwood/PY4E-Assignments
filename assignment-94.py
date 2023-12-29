name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

words = []  

for line in handle:
    if not line.startswith("From "):
        continue 
    line = line.split()
    if len(line) > 1:  
        words.append(line[1])

counts = dict()             
for word in words:
    counts[word] = counts.get(word, 0) + 1  

print(counts)

maxval = None
maxkey = None
for key,val in counts.items():
    if maxval is None or val > maxval:
        maxkey = key
        maxval = val

print(maxkey, maxval)
