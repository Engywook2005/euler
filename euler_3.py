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
        if is_prime(divisor):
        #    print('dividing by {}'.format(divisor))
            if n % divisor == 0:
                prime_factors.append(divisor)
                quotient = n / divisor
                if is_prime(quotient):
                    prime_factors.append(math.floor(quotient))
                print('{} by {} found'.format(divisor, math.floor(quotient)))    
        divisor += 1

    return prime_factors    

print(find_prime_factor(600851475143))

#print(find_prime_factor(34))

#print(is_prime(25))