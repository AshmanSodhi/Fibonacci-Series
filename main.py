length = int(input("Enter the Length of the Series: "))
def a(num):
    if num==0:
        return 0
    else:
        pa = 0
        ca = 1
        for i in range(0,num):
            print(pa)
            na = pa+ca
            pa = ca
            ca = na
        return pa

print(a(length))
