text = ('this some is sample some text this is second')
x=text.split()
word='this'
index=[]
for i in range(len(x)):
  if x[i]==word:
    index.append(i)
    x[i]=x[i].upper()
    '''
for j in index:
  x[j]=x[j].upper()'''
str1=" "
print(str1.join(x))
