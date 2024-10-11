#estructura sim
a=200
b=207
if b > a:
    print(b,"es mayor que ",a)


#escritura doble
if a>b :
    print(a,"es mayor que ",b)
else:
    print(a,"no es mayor que ",b)

#condicion Multiplie
if a> b:
    print(a,"es ayor que",b)
elif a<b:
    print(a,"es menor que ",b)
else:
    print(a,"es igual que",b)
# conicione enlazadas
x=28
if x >10 :
    print("por encima de diez")
    if x >20:
        print("y tambien por encima de 20")
    else:
        print("pero no por encima de 20")
#parametros end
print("studiar los sabados ",end=" ")
print("es genial")
#parametros sep
print("daniela","luis","carlos","camila")#agrega un espacio por defecto
print("daniela","luis","carlos","camila",sep="")#Quita el espacio
print("daniela","luis","carlos","camila",sep=",")#agrega una coma

print("daniela","luis","carlos","camila",sep="-",end="_curso_python")#implementacion end y sep
