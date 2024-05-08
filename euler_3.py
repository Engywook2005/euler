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

def find_prime_factor(n):
    upper_limit = math.sqrt(n)
    prime_factors = []
    divisor = 2

    while divisor <= upper_limit:
        if n % divisor == 0: # performance MUCH better if this is checked first. Limits number of checks on whether a number is prime
            if is_prime(divisor):
                prime_factors.append(divisor)
                quotient = n / divisor
                if is_prime(quotient):
                    prime_factors.append(math.floor(quotient))
                print('{} by {} found'.format(divisor, math.floor(quotient)))    
        divisor += 1
    print(prime_factors)
    return prime_factors    

print(max(find_prime_factor(600851475143)))