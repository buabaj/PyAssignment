# function to ask how many fibonacci numbers to generate and print them

def mem_fib(n, _cache={}):
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n


n = int(input("How many Fibonacci numbers would you like to generate?: "))

for i in range(n):
    print(mem_fib(i))
