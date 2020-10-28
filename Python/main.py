a = 100
print(a)

a = 'test'
print(a)

f = 0
print(f)

f = 'testt'
print(f)

a = 'janko'
b = 99
print(a+str(b))

f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
  global f
  print(f)
  f = "changing global variable"
someFunction()
print(f)