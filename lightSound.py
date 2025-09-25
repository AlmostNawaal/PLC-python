s = "light travels faster than sound."
l=s.split()
l[0] = l[0].upper()
l[-1] = l[-1].upper()
del l[1]
print(" ".join(l))
