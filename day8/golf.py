q=open('i').read().split("\n")
t=0
for n in q:
 d,x,f,s,e=[""]*10,n.split(" | "),[],[],len;j=x[0].split()
 for v in j:
  if e(v)==2:d[1]=v
  elif e(v)==3:d[7]=v
  elif e(v)==4:d[4]=v
  elif e(v)==7:d[8]=v
  elif e(v)==5:f.append(v)
  else:s.append(v)
 for j in range(3):
  p=set(d[1]).difference(s[j])
  if e(p)==1:d[6]=s.pop(j);break
 l=''
 for j in range(3):
  p=set(d[6]).difference(f[j])
  if e(p)==1:d[5]=f.pop(j);l=p.pop();break
 if l in s[1]:s.reverse()
 if l in f[1]:f.reverse()
 d[0],d[9],d[2],d[3],r=s[0],s[1],f[0],f[1],""
 for v in x[1].split():
  for k in d:
   if set(v)==set(k):r+=str(d.index(k))
 t+=int(r)
print(t)