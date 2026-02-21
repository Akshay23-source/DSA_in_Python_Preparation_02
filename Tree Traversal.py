class N:
    def __init__(s,v): s.v=v; s.l=s.r=None
def inorder(r):
    if r:
        inorder(r.l); print(r.v); inorder(r.r)
t=N(1); t.l=N(2); t.r=N(3)
inorder(t)





def pre(r):
    if r:
        print(r.v); pre(r.l); pre(r.r)
pre(t)