# 0 1 2 3 4 5 6 7  8  9  10 ... <- index
# 0 1 1 2 3 5 8 13 21 34 55 ... <- Fibonacci number
# ^^^
#
# 0 1 1 2 3
#
# base cases
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n - 1) + fib(n - 2)

# cache = {}

# def fib(n):
#     if n == 0: return 0  # base case
#     if n == 1: return 1  # base case
# #     if n <= 1: return n # -> replace the 2 top lines
#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)
#     return cache[n]

# for i in range(1, 10):
#     print(f'{i}: {fib(i)}')




# Bottom-up dynamic programming
#
# Start from the base case and work up forward the number

def fib(n):

    f = [0, 1]

    if n <= 1: return f[n]

    for _ in range(n-1):

        next_fib = f[-1] + f[-2]

        f.append(next_fib)

    return f[-1]

for ii in range(2, 12):
    print(fib(ii))
