print("packing")
def display(*n):
    print(n)
    print(*n)
    s=0
    for i in n:
        print(i)
        s+=i
    return s
print(display(1,2,3))
print(display(10,20,30))
print("unpacking")
def Display(a,b,c):
    print(a,b,c)
l = [10,20,30]
Display(*l)
print(*l)# *l seperates each element and prints them.
print(l)#l is list so prints[10,20,30]

