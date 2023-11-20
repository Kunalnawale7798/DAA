#Write a program non-recursive and recursive program to calculate Fibonacci numbers and 
#analyze their time and space complexity.
def fibonacci_iterative(n):
    if n <= 1:
        return n

    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    n = 8

    # Iterative Fibonacci
    result_iterative = fibonacci_iterative(n)
    print(f"The {n}-th Fibonacci number (iterative) is: {result_iterative}")

    # Recursive Fibonacci
    result_recursive = fibonacci_recursive(n)
    print(f"The {n}-th Fibonacci number (recursive) is: {result_recursive}")
