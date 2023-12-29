def computepay(h,r):
    if h <= 40:
        p = h * r
    elif h > 40:
        p = (40 * r) + (r * 1.5) * (h - 40)
    return p 

hrs = input("Enter Hours:")
rte = input ("Enter Rate:")
h = float(hrs)
r = float(rte)
p = computepay(h, r)
print("Pay", p)