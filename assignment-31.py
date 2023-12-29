hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
if h <= 40:
    x=h*r
    print(x)
elif h > 40:
    x=(40*r)+(r*1.5)*(h-40)
    print(x)