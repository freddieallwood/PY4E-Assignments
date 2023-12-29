score = input("Enter Score: ")
try:
    s = float(score)
except:
    s = -1
if s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6 and s >= 0:
    print("F")
elif s < 0:
    print("Number not entered")