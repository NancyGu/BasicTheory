# Fibonacci
# method 1 : use a list to save the middle result
def Fibonacci(x):
    x_list = []
    for v in range(x + 1):
        if v == 0 or v == 1:
            x_list.append(1)
        else:
            x_list.append( x_list[v-1] + x_list[v-2])
    return x_list[len(x_list) - 1 ]

# method 2: use recursion
def Fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return Fib(x-1) + Fib(x-2)

print(Fibonacci(10))
print(Fib(10))