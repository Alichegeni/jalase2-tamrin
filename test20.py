n = []
a = 0
b = 1
if n < 0:
    print("Incorrect input")
elif n == 0:
    a=0
    
elif n == 1:
    b=1
    
    
else:
    for i in range(2,n):
        c = a + b
        a = b
        b = [c]

print(b)