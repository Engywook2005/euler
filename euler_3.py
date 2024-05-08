import math

def is_prime(n):
    upper_limit = math.sqrt(n)
    pointer = 2
    while pointer <= upper_limit:
        print('pointer is {}'.format(pointer))
        if(n % pointer == 0):
            return False
        pointer += 1
    return True        

def find_prime_factor(n):
    upper_limit = math.sqrt(n)
    prime_factors = []
    divisor = 2

    while divisor <= upper_limit:
        if is_prime(divisor):
            print('dividing by {}'.format(divisor))
            if n % divisor == 0:
                prime_factors.append(divisor)
        divisor += 1

    return prime_factors    

prime_factors = find_prime_factor(60)

print(prime_factors)


# print(find_prime_factor(600851475143))

print(is_prime(25))