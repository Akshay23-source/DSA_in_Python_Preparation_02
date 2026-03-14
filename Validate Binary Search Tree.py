def isbst(a):
    for i in range(len(a)-1):
        if a[i]>=a[i+1]: return False
    return True
print(isbst([1,2,3,4]))


a=[1,2,3,4]
print(all(a[i]<a[i+1] for i in range(len(a)-1)))