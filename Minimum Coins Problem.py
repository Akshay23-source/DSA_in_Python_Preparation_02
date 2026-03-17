coins=[5,2,1]; v=11; c=0
for x in coins:
    c+=v//x
    v%=x
print(c)





v=7; coins=[5,2,1]; c=0
for x in coins: c+=v//x; v%=x
print(c)