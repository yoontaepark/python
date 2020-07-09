def computepay(h,r):
    if h>40:
        payment = 40*r + (h-40)*1.5*r
    else:
        payment = h*r
    return payment

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate:")
r = float(rate)

p = computepay(h,r)

print('Pay',p)
