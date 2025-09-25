n = int(input("enter the number of terms"))
next = 0
prev = 0
curr = 1
for i in range(n):
    print(curr)
    next = prev + curr
    prev = curr
    curr = next