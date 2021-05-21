text = ('this some is sample some text')
x=text.split()
word='this'
l={}
for i in set(x):
  
  if i in l.keys():
    l.update({i:x.count(i)})
  else:
    l[i]=1

print(l)
