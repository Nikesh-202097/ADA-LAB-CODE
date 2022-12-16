def expo(a, n):
    if n == 0:
        return 1
    result = expo(a, n // 2)
    if n % 2 == 0:
        result = result * result
    else:
        result = a * result * result
    return result


def isPrime(n):
    m = n - 1
    for a in range(2, n):
        E = expo(a, m)
        if E % n != 1:
            return False
    return True

num = int(input("Enter a number: "))
if isPrime(num):
    print("Number is prime")
else:
    print("Number is not prime")