a,b=0,1
print(a)
print(b)
#Printed the first 2 numbers, Now looping through the next 8 numbers
for i in range(8):
    c = a + b
    print(c)
    a = b
    b = c
