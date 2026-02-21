def h(r):
    if not r: return 0
    return 1+max(h(r.l),h(r.r))
print(h(t))


def c(r):
    return 0 if not r else 1+c(r.l)+c(r.r)
print(c(t))