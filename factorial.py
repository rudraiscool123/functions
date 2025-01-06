def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print('factroial of 0:', factorial(0))
print('factroial of 1:', factorial(1))
print('factroial of 2:', factorial(2))
print('factroial of 5:', factorial(5))
print('factroial of 10:', factorial(10))