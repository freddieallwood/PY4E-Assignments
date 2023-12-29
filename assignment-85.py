fname = input("Enter file name: ")
fh = open(fname)
count = 0 
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):  # Corrected typo here
        count = count + 1 
        lst = line.split()
        print(lst[1])

print("There were", count, "lines in the file with From as the first word")
