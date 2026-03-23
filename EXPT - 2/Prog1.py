p = int(input("Enter the principal amount:"))
t = int(input("Enter the TIme Period (in years):"))
r = int(input("Enter the rate of interest:"))
si = (p*t*r)/100
amp = p*(1+r/100)**t
ci = amp - p
print("Simple Interest:",si)
print("Compound Interest:",ci)