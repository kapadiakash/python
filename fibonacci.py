a = 1
b = 2 
c = 2
x = int(input("Enter a number: "))
print(a,b,c,end=',')
for i in range(1,x):
    c=a+b
    a=b
    b=c
    print(c,end=',')