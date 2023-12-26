n = int(input('enter a number '))
for i in range(2,n):
    if n % i == 0:
        print(n,'is a not prime number')
        break
    else:
        print(n, 'IS A PRIME NUMBER')
        break