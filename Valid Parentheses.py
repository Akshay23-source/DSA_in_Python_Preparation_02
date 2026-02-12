s="()[]{}"; st=[]
for c in s:
    if c in "([{": st.append(c)
    elif not st or "([{".index(st.pop())!=")]}".index(c):
        print(False); break
else: print(True)




s="(()())"; c=0
for x in s: c+=1 if x=="{}" else -1
print(c==0)
