def fib(n, depth=0):
    indent = "  " * depth
    print(f"{indent}fib({n}) called")

    if n == 0:
        print(f"{indent}Returning 0")
        return 0
    if n == 1:
        print(f"{indent}Returning 1")
        return 1
    result = fib(n-1, depth+1) + fib(n-2,depth+1)
    print(f"{indent}Returning {result} for fib{n}")
    return result 
n = 5
print(f"Final Result: fib({n}) = {fib(n)}")