string=input()
alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in alpha:
  string=string.replace(i, '!')
print(len(string))