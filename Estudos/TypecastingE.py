# typecasting = é processo de converter um valor de um tipo de dado para outro manualmente.
# explicit 

name = "Cleide"
age = 52 #int
gpa = 2.1 #float
student = True

age = float(age) # de int foi para float

print(type(age))
print(age)

gpa = int(gpa) # de float foi para int

print(type(gpa))
print(gpa)  

student = str(student) # de valor booleano foi para string

print(type(student))
print(student)

# da para converter qualquer valor para qualquer coisa que quiser, até numero para booleano.    

age = bool(age) # de int para booleano

print(type(age))
print(age)