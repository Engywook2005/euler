import math

def find_next_pointer(n, list):
    idx = list.index(n)
    if n < len(list):
        return list[idx + 1]
    return - 1


def erastothenes(n):
    upper_limit = math.floor(math.sqrt(n))
    all_primes = list(range(2, n))
    pointer = 2
    while pointer < upper_limit and pointer > 0:
        print('pointer is {}'.format(pointer))
        for num in all_primes:
            if num != pointer and num % pointer == 0: 
                print('removing {}'.format(num))
                all_primes.remove(num)
        pointer = find_next_pointer(pointer, all_primes)        
    return all_primes

def find_prime_factor(n):
    all_primes = erastothenes(n)
    print(all_primes)

    while len(all_primes) > 0:
        candidate = all_primes.pop()
        if n % candidate == 0:
            return candidate
        
    return n

print(find_prime_factor(101))      
# print(find_prime_factor(600851475143))