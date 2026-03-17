s=[1,3,0,5,8]; f=[2,4,6,7,9]
a=sorted(zip(f,s))
c=1; end=a[0][0]
for x in a[1:]:
    if x[1]>=end: c+=1; end=x[0]
print(c)




s=[1,2]; f=[3,4]
print(sorted(zip(f,s)))