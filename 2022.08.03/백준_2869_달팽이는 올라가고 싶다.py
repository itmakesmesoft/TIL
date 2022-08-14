a,b,v = map(int, input().split())
x=(v-b)/(a-b)
if x!=int(x):
  x=int(x)+1
print(int(x))