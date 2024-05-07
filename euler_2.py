def fib(limit, divisor):
    score = 0
    iterations = 0

    last_value = 0
    current_value = 1

    while current_value <= limit:
        iterations += 1
        next_value = last_value + current_value
        last_value = current_value
        current_value = next_value
        if current_value % divisor == 0:
            score += current_value

    return score

print(fib(4000000, 2))