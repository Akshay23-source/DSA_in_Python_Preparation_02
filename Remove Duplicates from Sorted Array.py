a=[1,2,3,4,4,2]
u=[a[0]]
for x in a[1:]:
    if x!=u[-1]:u.append(x)
    print(u)
    
    
    a=[1,1,2,3,3]
print(len(set(a)))
