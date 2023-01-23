def gip(a,b):
    return (a**2 + b**2)**(1/2)

def arithmetic(a,b,c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    else:
        print("Fail")
        
def square_parameters(a):
    P = 4 * a
    S = a ** 2
    d = a * 2 ** (1/2)
    return P, S, d

def is_prime(a):
    d = 0
    for i in range(1,a+1):
        if a % i == 0:
            d += 1
            
    if a <= 0:
        print('NO')
    elif d == 1:
        print('1 is not simple and complex')
    elif d == 2:
        print("Simple")
    else:
        print('Complex')

def is_palindrome(a):
    return a == a[::-1]