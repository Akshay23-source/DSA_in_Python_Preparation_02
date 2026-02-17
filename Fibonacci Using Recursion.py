def f(n): return n if n<2 else f(n-1)+f(n-2)
print(f(6))


def f(n): return 0 if n==0 else n+f(n-1)
print(f(5))
