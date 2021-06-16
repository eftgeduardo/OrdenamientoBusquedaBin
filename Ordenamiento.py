import mysql.connector
import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MSI\SQLEXPRESS;'
                      'Database=Martin_Proyecto;'
                      'Trusted_Connection=yes;')


def quicksortStrings(A,min,max):
    #picking pivot
    pivot=A[max][1]# [ [2,"loque necesito"]]
    #while(min<max):
    j=min-1
    for i in range(min,max+1):
        if(A[i][1]<=pivot):
            j+=1
            A[i],A[j]=A[j],A[i]
    if((max-min)<3):
        return
    quicksortStrings(A,min,j-1)
    quicksortStrings(A,j+1,max)


def busquedaBinaria(A,max,min,palabra):
    puntoMedio=int((min+max)/2)#buscar el punto medio
    valor=A[puntoMedio]
    if ((max-min)==1):  
        return -1
    if(palabra==valor):#valor en el punto medio es el valor buscado(?)
        return puntoMedio
    elif (palabra>valor):#valor buscado es mayor que punto medio (?)
        min=puntoMedio #nuevo rango de minimo
        return busquedaBinaria(A,max,min,palabra)
    else:
        max=puntoMedio #nuevo rango de maximo
        return busquedaBinaria(A,max,min,palabra)

def BusquedaSecuencial(A,x,paso):
    print("busquedaSecuencial")
    j=0
    while(True):
        if(x+j+paso==len(A) or x+j-1<0):
            break
        if(A[x]==A[x+j+paso]):
            j+=paso
        else:
            break
    return j

def busqueda(A,palabra):
    B={}
    for i in range(len(A)):
        B[i]=A[i][1]
    x=busquedaBinaria(B,len(B),-1,palabra)
    if(x==-1):
        print("{} no existe",palabra)
        return
    encontrado=1
    encontrado+=BusquedaSecuencial(B,x,1)#va hacia en frente
    j=BusquedaSecuencial(B,x,-1) #va hacia atras
    x=x+j    
    encontrado+=abs(j)
    print("{} se encuentra {}".format(palabra,encontrado))
    for i in range(x,x+encontrado):
        print("Linea: {}, Id de Estación: {}".format(A[i][2],A[i][3]))

def main():
    cursor=conn.cursor()
    query='Select * FROM Estaciones'
    cursor.execute(query)
    j=0
    A={}
    for row in cursor:
        A[j]=row
        j+=1

    quicksortStrings(A,0,len(A)-1)
    x=input("Escriba estacion:")
    busqueda(A,x)





if __name__=='__main__':
    main()

     