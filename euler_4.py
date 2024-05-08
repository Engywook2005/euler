def check_palindrome(n):
    n_to_string = str(n)
    return n_to_string == n_to_string[::-1]

def find_largest_palindrome(upper, lower):
    r = range(upper, lower - 1, -1)

    for outer_num in r:
        for inner_num in r:
            product = outer_num * inner_num
            print('multiplying {} by {}'.format(outer_num, inner_num))
            if check_palindrome(product):
                return product
    
    return 0

print('largest palindrome is {}'.format(find_largest_palindrome(999, 100)))