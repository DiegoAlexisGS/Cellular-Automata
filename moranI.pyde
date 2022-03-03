"""
Simulador del índice de Moran
Utiliza la I de Moran dada por Moran en su artículo y la versión que 
incluye la matriz W construida bajo un vecindario tipo Torre.
Utiliza una lattice de 25x25 
"""
from random import uniform

#Tamaño de la lattice
nCols=25
nRows=25

#Inicialización 
def setup():
    background(255)
    global nCols,nRows,grid
    size(500,550)
    cond=0
    evalua(cond)
    
#Dibuja nuestra lattice 
def draw():
    global nCols,nRows,grid
    #valor=int(random(0,4))
    #evalua(valor)


def mousePressed():
    valor=int(random(0,4))
    evalua(valor)

def evalua(condicion):
    background(255)
    grid=makeGrid()
    media=0
    value=0
    id=0
    for i in range(nRows):
        for j in range(nCols):
            c,value=condition(condicion,i,j)
            grid[i][j]=Cell(j*20,i*20,20,20,c,value,id)
            grid[i][j].colour=c
            grid[i][j].display()
            media+=value
            id+=1
    res,lista=vecindario(grid)
    media=media/(nRows*nCols)
    i_0,i_1,c=idemoran(grid,media,res,lista)
    #print((lista))
    s = "I= "+str(round(i_1,4))+"  ,  "+"c= "+str(round(c,4))
    fill(230,0,38);
    textSize(20)
    text(s, 125, 515,500, 50)
                    
#Lattice de 25x25
def makeGrid():
    global nCols, nRows
    grid=[]
    for i in range(nRows):
        grid.append([])
        for j in range(nCols):
            grid[i].append(0)
    return (grid)


#Clase célula
class Cell():
    def __init__(self,X,Y,W,H,C,L,ID):
        self.x=X
        self.y=Y
        self.w=W
        self.h=H
        self.c=C
        self.l=L
        self.id=ID
    def display(self):
        stroke(0)
        fill(self.c)
        rect(self.x,self.y,self.w,self.h)

#Crea aleatoriedad o patrones
def condition(p,x,y):     #p es la condición, x,y son las coordenadas
    #1 Condicion inicial aleatoria
    #0 Condición de patrón 
    v=0
    #Versión totalmente aleatoria, I=0
    if p==0:
        co=uniform(0,1)
        if co<0.3:
            #Color blanco valor 0
            v=co*10
            co=255
        elif (co>=0.3 and co<0.6):
            #Color gris valor 5
            v=co*10
            co=200
        else:
            #Color negro valor 10
            v=co*10
            co=10
            
    #Versión no aleatoria. Clusters no muy marcados I>0
    elif p==1:
        if ((x>=3 and x<11) or (x>=14 and x<22)) and ((y>=3 and y<11) or (y>=14 and y<22)):
            #Colores negros y grises
            v=uniform(0,0.6)   
            co=255*v             
        else:
            #Colores blancos y grises claros
            v=v=uniform(0.66,1)
            co=255*v
    
    #Versión no aleatoria. Clusters muy marcados I>0.5
    elif p==2:
        if ((x>=3 and x<11) or (x>=14 and x<22)) and ((y>=3 and y<11) or (y>=14 and y<22)):
            #Colores negros y grises
            v=uniform(0,0.3)   
            co=255*v             
        else:
            #Colores blancos y grises claros
            v=v=uniform(0.66,1)
            co=255*v
    elif p==3:
        if (x+y)%2==0:
            v=v=uniform(0,0.3)
            co=255*v
        else:
            v=v=uniform(0.66,1)
            co=255*v
                
    return(co,v)    
     

    
#Calcula la I de Moran
def idemoran(lattice,promedio,matrizw,new):
    global nCols,nRows
    suma1=0 #Primer término
    suma2=0 #Segundo término
    deno=0#denominador
    
    """
    I de Moran con la fórmula original
    """
    
    #Calcula el primer término de la expresión
    for i in range(nRows):
        for j in range(nCols-1):
            suma1+=(lattice[i][j].l-promedio)*(lattice[i][j+1].l-promedio)
    
    #Calcula el segundo término de la expresión                
    for i in range(nRows-1):
        for j in range(nCols):
            suma2+=(lattice[i][j].l-promedio)*(lattice[i+1][j].l-promedio)
    
    #Calcula el denominador de la expresión            
    for i in range(nRows):
        for j in range(nCols):
            deno+=(lattice[i][j].l-promedio)**2
    
    I_0=((nRows*nCols)*(suma1+suma2))/((2*nRows*nCols-nRows-nCols)*deno)    
            
    """
    I de Moran y c de Geary calculado con la matriz W
    """
    #Calculo del numerador y denominador
    numerador=0
    denominador=0
    sumaW=0
    sumac=0
    N=nCols*nCols
    for i in range(N):
        for j in range(N):
            numerador+=matrizw[i][j]*(new[i]-promedio)*(new[j]-promedio)
            sumaW+=matrizw[i][j]
            sumac+=matrizw[i][j]*((new[i]-new[j])**2)
        denominador+=(new[i]-promedio)**2
    I_1=(N*(numerador)/(sumaW*(denominador))) #Expresión de la I de Moran
    c=((N-1)*sumac)/(2*sumaW*(denominador)) #Expresión de la c de Geary 
    
    """
    C de Geary
    """

       
                               
    return(I_0,I_1,c)
                    

#Función que llena la matriz W con 0 o 1 
def vecindario(mapa):
    global nRows, nCols
    N=nRows*nCols #Número de columnas de la matriz W
    W=[] #Se crea la matriz W solo con ceros
    new=[]
    for p in range(N):
        W.append([0]*N)
    index=0
    
    #Proceso que evalua un vecindario tipo torre y llena la matriz W con 1's
    for i in range(nRows):
        for j in range(nCols):
            new.append(mapa[i][j].l)
            #Evalua la esquina superior izquierdaj
            if (i==0 and j==0):
                v1=mapa[i+1][j].id
                v2=mapa[i][j+1].id
                for k in [v1,v2]:
                    W[index][k]=1
                index+=1
                
            #Evalua la esquina superior derecha
            if ((i==0) and j==(nCols-1)):
                v1=mapa[i+1][j].id
                v2=mapa[i][j-1].id
                for k in [v1,v2]:
                    W[index][k]=1
                index+=1
            
            #Evalua la esquina inferior izquierda
            if (i==(nRows-1) and j==0):
                v1=mapa[i-1][j].id
                v2=mapa[i][j+1].id
                for k in [v1,v2]:
                    W[index][k]=1
                index+=1
                
            #Evalua la esquina inferior derecha
            if (i==(nRows-1) and j==(nCols-1)):
                v1=mapa[i-1][j].id
                v2=mapa[i][j-1].id
                for k in [v1,v2]:
                    W[index][k]=1
                index+=1
            
            #Evalua la parte superior
            if (i==0) and (j>0 and j<(nCols-1)):
                v1=mapa[i+1][j].id
                v2=mapa[i][j-1].id
                v3=mapa[i][j+1].id
                for k in [v1,v2,v3]:
                    W[index][k]=1
                index+=1
            
            #Evalua la parte inferior
            elif (i==(nRows-1)) and (j>0 and j<(nCols-1)):
                v1=mapa[i-1][j].id
                v2=mapa[i][j-1].id
                v3=mapa[i][j+1].id
                for k in [v1,v2,v3]:
                    W[index][k]=1
                index+=1
            
            #Evalua la parte izquierda
            elif (i>0 and i<(nRows-1)) and (j==0):
                #Obtiene los valores
                v1=mapa[i-1][j].id
                v2=mapa[i+1][j].id
                v3=mapa[i][j+1].id
                #Barre la matriz
                for k in [v1,v2,v3]:
                    W[index][k]=1
                index+=1
                
            #Evalua la parte derecha
            elif ((i>0 and i<(nRows-1)) and (j==(nCols-1))):
                #Obtiene los valores
                v1=mapa[i-1][j].id
                v2=mapa[i+1][j].id
                v3=mapa[i][j-1].id
                #Barre la matriz
                for k in [v1,v2,v3]:
                    W[index][k]=1
                index+=1
                
            #Solo evalua el centro
            elif (i>0 and j>0) and (i<(nRows-1) and j<(nCols-1)):
                #Obtiene los valores
                v1=mapa[i-1][j].id
                v2=mapa[i+1][j].id
                v3=mapa[i][j-1].id
                v4=mapa[i][j+1].id
                #Barre la matriz
                for k in [v1,v2,v3,v4]:
                    W[index][k]=1
                index+=1
                
    return(W,new)
                
            
        
            
    
        
                            
                                                    
