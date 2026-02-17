def f(n): return 1 if n==0 else n*f(n-1)
print(f(5))



def f(n):
    if n==0: return
    f(n-1); print(n)
f(5)
