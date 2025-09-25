d={}
n = int(input("enter no of key calur pairs:"))
while n > 0:
    kvp= input("enter key-value pair:<key:value>:")
    l = kvp.split(':')
    d[l[0]]=l[1]
    n-=1
print(d)