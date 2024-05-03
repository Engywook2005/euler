# Should only be used when we have another way to impose an upper limit to recursion depth
# Better to use an iterative approach than deep recursion
import sys
sys.setrecursionlimit(2000)

def find_multiples(common_factors, limit):
    def check_multiples(candidate_number, running_total):
        for common_factor in common_factors:
            if candidate_number % common_factor == 0:
                running_total += candidate_number
                break
        next_number = candidate_number + 1
        if next_number >= limit:
            return running_total
        else:
            return check_multiples(next_number, running_total)        

    return check_multiples(1, 0)

def find_multiples_iterative(common_factors, limit):
    running_total = 0
    for candidate_number in range(1, limit):
        for common_factor in common_factors:
            if candidate_number % common_factor == 0:
                running_total += candidate_number
                break
    return running_total

output_iterative = find_multiples_iterative([3, 5], 1000)

output = find_multiples([3, 5], 1000)

print(output)

yes_or_no = " not" if output_iterative != output else ""

print(("The output of the two functions do{} match!").format(yes_or_no))
