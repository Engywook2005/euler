import math

def is_prime(n):
    upper_limit = math.sqrt(n)
    pointer = 2
    while pointer <= upper_limit:
        # print('pointer is {}'.format(pointer))
        if(n % pointer == 0):
            return False
        pointer += 1
    return True        

def append_prime_factors(n, found):
    print('appending {}'.format(n))
    found.append(n) # since by reference no need to return it. May be safer to clone it

def find_prime_factor(n):
    upper_limit = math.sqrt(n)
    prime_factors = []
    divisor = 2

    if is_prime(n):
        prime_factors.append(n)

    while divisor <= upper_limit:
        if n % divisor == 0: # performance MUCH better if this is checked first. Limits number of checks on whether a number is prime
            if is_prime(divisor):
                append_prime_factors(divisor, prime_factors)
                quotient = math.floor(n / divisor)
                if is_prime(quotient):
                    append_prime_factors(quotient, prime_factors)
        divisor += 1
    print(prime_factors)
    return prime_factors    

#print(max(find_prime_factor(100)))
print(max(find_prime_factor(600851475143)))