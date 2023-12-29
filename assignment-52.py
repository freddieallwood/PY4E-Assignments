largest = None
smallest = None

while True:
    num = input("Enter a number:")
    if num == "done":
        break
    else:
        try:
            n = float (num)
            if largest is None:
                largest = n
            elif largest < n:
                largest = n
            if smallest is None:
                smallest = n
            elif smallest > n:
                smallest = n
        except:
            print ("Invalid input")

print ("Maximum is", int(largest))
print ("Minimum is", int(smallest))

            