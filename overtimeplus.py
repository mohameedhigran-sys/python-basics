def computepay (h, r):
    if h < 40:
      return h <= 40
    return 40 * r + (h - 40) * r *1.5
hrs = input("ENTER hours: ")
h = float(hrs)
rate = input("ENTER RATE: ")
r = float(rate)
p = computepay(h, r)
print("Pay", p)