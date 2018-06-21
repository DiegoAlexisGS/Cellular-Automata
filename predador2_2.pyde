"""
Galván Sandoval Diego Alexis
Matemáticas Aplicadas y Computación
Seminario de investigación en Matemáticas Aplicadas y Computación
Autómata Celular 2-D "Modelo depredador-presa"
"""
import time
nCols=75
nRows=75
contar=0
contar2=0
tim=0

def setup():  
    global nCols,nRows,grid,contar,contar2
    background(255)
    size(600,600)
    iniciar()
    

def draw():
    global nCols,nRows,grid,contar,contar2,grid
    #evolucion()
    



#Da valores iniciales a cada celular
def iniciar():
    global contar,contar2,grid
    grid=makeGrid()
    for i in range(nRows):
        for j in range(nCols):
            c=random(1)
            #normal
            if c<=0.3:
                c=0
            #presa
            elif c>=0.6 :
                c=1

            #depredador
            else:
                c=2
            grid[i][j]=Cell(j*8,i*8,8,8,c)
            grid[i][j].colour=c
            
    for i in range(nRows):
        for j in range(nCols):
            #Movimientos de los seres vivos
            grid[i][j].display()
    #Evoluciona el autómata
    valores=list(contando(grid))
    valores.append(tim)
    imp=str(valores[0])+","+str(valores[1])+","+str(valores[2])
    archivo = open("datos.txt", "r+")
    contenido = archivo.read()
    final_de_archivo=archivo.tell()
    archivo.write(imp+'\n')
    archivo.seek(final_de_archivo)
    archivo.close()
    
    return(grid)
    
#Reinicia el automata al dar clic en el mouse
def mousePressed():
    iniciar()
    

    
#Crea la latice donde viviran los automatas
def makeGrid():
    global nCols,nRows
    grid=[]
    for i in range(nRows):
        grid.append([])
        for j in range(nCols):
            grid[i].append(0)
    return grid

#Crea la celula con su tamaño y coordenadas así como la especie a la que pertenecen
class Cell():
    colour=0
    def __init__(self,X,Y,W,H,C):
        self.x=X
        self.y=Y
        self.w=W
        self.h=H
        self.c=C
        colour=self.c
    
    def display(self):
        stroke(0)
        if self.c==0:
            #neutro
            fill(255)
            rect(self.x,self.y,self.w,self.h)
        elif self.c==1:
            #prey            
            fill(0,255,0)
            rect(self.x,self.y,self.w,self.h)
        elif self.c==2:
            #predator
            fill(0,0,255)
            rect(self.x,self.y,self.w,self.h)
            
def vecindario(lattice,i,j,especie):
    numpres=0
    numdep=0
    #Los predadores se alimentan NO CONSIDERA LAS FRONTERAS
    if i!=0 and i!=74 and j!=0 and j!=74:
        if lattice[i][j].colour==2: #Si la celula es un depredador revisa su vecindario
            if lattice[i-1][j-1].colour==1:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour=0
                lattice[i][j].display()
                lattice[i-1][j-1]=Cell((j-1)*8,(i-1)*8,8,8,2)
                lattice[i-1][j-1].colour=2
                lattice[i-1][j-1].display()        
            elif lattice[i-1][j].colour==1:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour=0
                lattice[i][j].display()
                lattice[i-1][j]=Cell((j)*8,(i-1)*8,8,8,2)
                lattice[i-1][j].colour=2
                lattice[i-1][j].display()
            elif lattice[i-1][j+1].colour==1:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour=0
                lattice[i][j].display()
                lattice[i-1][j+1]=Cell((j+1)*8,(i-1)*8,8,8,2)
                lattice[i-1][j+1].colour=2
                lattice[i-1][j+1].display()
            elif lattice[i][j-1].colour==1:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour=0
                lattice[i][j].display()
                lattice[i][j-1]=Cell((j-1)*8,(i)*8,8,8,2)
                lattice[i][j-1].colour=2
                lattice[i][j-1].display()
            elif lattice[i][j+1].colour==1:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour=0
                lattice[i][j].display()
                lattice[i][j+1]=Cell((j+1)*8,(i)*8,8,8,2)
                lattice[i][j+1].colour=2
                lattice[i][j+1].display()
            elif lattice[i+1][j-1].colour==1:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour=0
                lattice[i][j].display()
                lattice[i+1][j-1]=Cell((j-1)*8,(i+1)*8,8,8,2)
                lattice[i+1][j-1].colour=2
                lattice[i+1][j-1].display()
            elif lattice[i+1][j].colour==1:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour=0
                lattice[i][j].display()
                lattice[i+1][j]=Cell((j)*8,(i+1)*8,8,8,2)
                lattice[i+1][j].colour=2
                lattice[i+1][j].display()
            elif lattice[i+1][j+1].colour==1:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour=0
                lattice[i][j].display()
                lattice[i+1][j+1]=Cell((j+1)*8,(i+1)*8,8,8,2)
                lattice[i+1][j+1].colour=2
                lattice[i+1][j+1].display()
                
            #Muerte de las celulas azules
            else:    
                if lattice[i-1][j].colour==2:
                    numdep+=1
                if lattice[i-1][j+1].colour==2:
                    numdep+=1
                if lattice[i][j-1].colour==2:
                    numdep+=1
                if lattice[i][j+1].colour==2:
                    numdep+=1
                if lattice[i+1][j-1].colour==2:
                    numdep+=1
                if lattice[i+1][j].colour==2:
                    numdep+=1
                if lattice[i+1][j+1].colour==2:
                    numdep+=1
                if numdep>=2 or numpres==0:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour==0
                    lattice[i+1][j+1]=Cell((j+1)*8,(i*8)*8,8,8,0)
                    lattice[i+1][j+1].colour=0
                    lattice[i+1][j+1].display()
    
        #Muerte de las celulas verdes            
        elif lattice[i][j].colour==1:
            if lattice[i-1][j].colour==1:
                numpres+=1
            if lattice[i-1][j+1].colour==1:
                numpres+=1
            if lattice[i][j-1].colour==1:
                numpres+=1
            if lattice[i][j+1].colour==1:
                numpres+=1
            if lattice[i+1][j-1].colour==1:
                numpres+=1
            if lattice[i+1][j].colour==1:
                numpres+=1
            if lattice[i+1][j+1].colour==1:
                numpres+=1
            if numpres>2:
                lattice[i][j]=Cell(j*8,i*8,8,8,0)
                lattice[i][j].colour==0
                lattice[i][j].display()
                
        #Crea celulas verdes ó azules
        elif lattice[i][j].colour==0:
            if lattice[i-1][j-1].colour==1:
                numpres+=1
            if lattice[i-1][j].colour==1:
                numpres+=1
            if lattice[i-1][j+1].colour==1:
                numpres+=1
            if lattice[i][j-1].colour==1:
                numpres+=1
            if lattice[i][j+1].colour==1:
                numpres+=1
            if lattice[i+1][j-1].colour==1:
                numpres+=1
            if lattice[i+1][j].colour==1:
                numpres+=1
            if lattice[i+1][j+1].colour==1:
                numpres+=1
            if lattice[i-1][j-1].colour==2:
                numdep+=1
            if lattice[i-1][j].colour==2:
                numdep+=1
            if lattice[i-1][j+1].colour==2:
                numdep+=1
            if lattice[i][j-1].colour==2:
                numdep+=1
            if lattice[i][j+1].colour==2:
                numdep+=1
            if lattice[i+1][j-1].colour==2:
                numdep+=1
            if lattice[i+1][j].colour==2:
                numdep+=1
            if lattice[i+1][j+1].colour==2:
                numdep+=1
             #Celulas verdes son creadas   
            if numpres<4:
                lattice[i][j]=Cell(j*8,i*8,8,8,1)
                lattice[i][j].colour=1
                lattice[i][j].display()
            
            #Celulas azules son creadas 
            """ 
            if numdep==2 and numpres==0:
                lattice[i][j]=Cell(j*8,i*8,8,8,2)
                lattice[i][j].colour=2
                lattice[i][j].display()
            """
            
    else:
        #Evalua esquinas superior izquierda
        if i==0 and j==0:
            if lattice[i][j].colour==2:
                if lattice[74][74].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[74][74]=Cell(74*8,74*8,8,8,2)
                    lattice[74][74].colour=2
                    lattice[74][74].display()
                    
                elif lattice[74][j].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[74][j]=Cell(j*8,74*8,8,8,2)
                    lattice[74][j].colour=2
                    lattice[74][j].display()
                
                elif lattice[74][j+1].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[74][j+1]=Cell((j+1)*8,74*8,8,8,2)
                    lattice[74][j+1].colour=2
                    lattice[74][j+1].display()
                    
                elif lattice[i][74].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i][74]=Cell(74*8,i*8,8,8,2)
                    lattice[i][74].colour=2
                    lattice[i][74].display()
                
                elif lattice[i][j+1].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i][j+1]=Cell((j+1)*8,i*8,8,8,2)
                    lattice[i][j+1].colour=2
                    lattice[i][j+1].display()
                
                elif lattice[i+1][74].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][74]=Cell(74*8,(i+1)*8,8,8,2)
                    lattice[i+1][74].colour=2
                    lattice[i+1][74].display()
                
                elif lattice[i+1][j].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][j]=Cell(j*8,(i+1)*8,8,8,2)
                    lattice[i+1][j].colour=2
                    lattice[i+1][j].display()
            
                elif lattice[i+1][j+1].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][j+1]=Cell((j+1)*8,i*8,8,8,2)
                    lattice[i][j+1].colour=2
                    lattice[i][j+1].display()
                #Muerte de las celulas azules
                else:    
                     if lattice[74][74].colour==2:
                         numdep+=1
                     if lattice[74][j].colour==2:
                         numdep+=1
                     if lattice[74][j+1].colour==2:
                         numdep+=1
                     if lattice[0][74].colour==2:
                         numdep+=1
                     if lattice[0][j+1].colour==2:
                         numdep+=1
                     if lattice[i+1][74].colour==2:
                         numdep+=1
                     if lattice[i+1][j].colour==2:
                         numdep+=1
                     if lattice[i+1][j+1].colour==2:
                         numdep+=1
                     if numdep==2 or numpres<100:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour==0
                        lattice[i][j].display()
                        
            elif lattice[i][j].colour==0:
                 if lattice[74][j-1].colour==1:
                     numpres+=1
                 if lattice[74][j].colour==1:
                     numpres+=1
                 if lattice[74][j+1].colour==1:
                     numpres+=1
                 if lattice[i][j-1].colour==1:
                     numpres+=1
                 if lattice[i][j+1].colour==1:
                     numpres+=1
                 if lattice[i+1][j-1].colour==1:
                     numpres+=1
                 if lattice[i+1][j].colour==1:
                     numpres+=1
                 if lattice[i+1][j+1].colour==1:
                     numpres+=1
                 if lattice[74][j-1].colour==2:
                      numdep+=1
                 if lattice[74][j].colour==2:
                      numdep+=1
                 if lattice[74][j+1].colour==2:
                      numdep+=1
                 if lattice[i][j-1].colour==2:
                      numdep+=1
                 if lattice[i][j+1].colour==2:
                      numdep+=1
                 if lattice[i+1][j-1].colour==2:
                      numdep+=1
                 if lattice[i+1][j].colour==2:
                      numdep+=1
                 if lattice[i+1][j+1].colour==2:
                      numdep+=1
                      #Celulas verdes son creadas
                 if numpres<5:
                     lattice[i][j]=Cell(j*8,i*8,8,8,1)
                     lattice[i][j].colour=1
                     lattice[i][j].display()
                 #Celulas azules creadas 
                    
                 if numdep==2 and numpres!=0:
                     lattice[i][j]=Cell(j*8,i*8,8,8,2)
                     lattice[i][j].colour=2
                     lattice[i][j].display()
                 
        
        #Esquina superior derecha            
        elif i==0 and j==74:
                if lattice[i][j].colour==2:
                    if lattice[74][j-1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[74][j-1]=Cell((j-1)*8,74*8,8,8,2)
                        lattice[74][j-1].colour=2
                        lattice[74][j-1].display()
                    
                    elif lattice[74][j].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[74][j]=Cell(j*8,74*8,8,8,2)
                        lattice[74][j].colour=2
                        lattice[74][j].display()
                
                    elif lattice[74][0].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[74][0]=Cell((0)*8,74*8,8,8,2)
                        lattice[74][0].colour=2
                        lattice[74][0].display()
                    
                    elif lattice[i][j-1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i][j-1]=Cell((j-1)*8,i*8,8,8,2)
                        lattice[i][j-1].colour=2
                        lattice[i][j-1].display()
                
                    elif lattice[i][0].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i][0]=Cell((0)*8,i*8,8,8,2)
                        lattice[i][0].colour=2
                        lattice[i][0].display()
                
                    elif lattice[i+1][j-1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i+1][j-1]=Cell((j-1)*8,(i+1)*8,8,8,2)
                        lattice[i+1][j-1].colour=2
                        lattice[i+1][j-1].display()
                
                    elif lattice[i+1][j].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i+1][j]=Cell(j*8,(i+1)*8,8,8,2)
                        lattice[i+1][j].colour=2
                        lattice[i+1][j].display()
            
                    elif lattice[1][0].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[1][0]=Cell((0)*8,1*8,8,8,2)
                        lattice[1][0].colour=2
                        lattice[i][0].display()
                    #Muerte de las celulas azules
                    else:
                        if lattice[74][j-1].colour==2:
                            numdep+=1
                        if lattice[74][j].colour==2:
                            numdep+=1
                        if lattice[74][0].colour==2:
                            numdep+=1
                        if lattice[i-1][0].colour==2:
                            numdep+=1
                        if lattice[0][0].colour==2:
                            numdep+=1
                        if lattice[i+1][j-1].colour==2:
                            numdep+=1
                        if lattice[i+1][j].colour==2:
                            numdep+=1
                        if lattice[0][1].colour==2:
                            numdep+=1
                            
                        if numdep<3 or numpres==0:
                            lattice[i][j]=Cell(j*8,i*8,8,8,0)
                            lattice[i][j].colour==0
                            lattice[i][j].display() 
                               
                elif lattice[i][j].colour==0:
                    if lattice[74][j-1].colour==1:
                        numpres+=1
                    if lattice[74][j].colour==1:
                        numpres+=1
                    if lattice[74][0].colour==1:
                        numpres+=1
                    if lattice[i][j-1].colour==1:
                        numpres+=1
                    if lattice[0][0].colour==1:
                        numpres+=1
                    if lattice[i+1][j-1].colour==1:
                        numpres+=1
                    if lattice[i+1][j].colour==1:
                        numpres+=1
                    if lattice[i+1][0].colour==1:
                        numpres+=1
                    if lattice[74][j-1].colour==2:
                        numdep+=1
                    if lattice[74][j].colour==2:
                        numdep+=1
                    if lattice[74][0].colour==2:
                        numdep+=1
                    if lattice[i][j-1].colour==2:
                        numdep+=1
                    if lattice[0][0].colour==2:
                        numdep+=1
                    if lattice[i+1][j-1].colour==2:
                        numdep+=1
                    if lattice[i+1][j].colour==2:
                        numdep+=1
                    if lattice[i+1][0].colour==2:
                        numdep+=1
                        #Crea celulas verdes
                    if numpres<5:
                        lattice[i][j]=Cell(j*8,i*8,8,8,1)
                        lattice[i][j].colour=1
                        lattice[i][j].display()
                    #Crea celulas azules
                    if numdep==2 and numpres!=0:
                        lattice[i][j]=Cell(j*8,i*8,8,8,2)
                        lattice[i][j].colour=2
                        lattice[i][j].display()
                    
        #Esquina inferior izquierda    
        elif i==74 and j==0:
                if lattice[i][j].colour==2:
                    if lattice[i-1][74].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i-1][74]=Cell((74)*8,(i-1)*8,8,8,2)
                        lattice[i-1][74].colour=2
                        lattice[i-1][74].display()
                    elif lattice[i-1][j].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i-1][j]=Cell((j)*8,(i-1)*8,8,8,2)
                        lattice[i-1][j].colour=2
                        lattice[i-1][j].display()
                    elif lattice[i-1][j+1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i-1][j+1]=Cell((j+1)*8,(i-1)*8,8,8,2)
                        lattice[i-1][j+1].colour=2
                        lattice[i-1][j+1].display()
                    elif lattice[i][74].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i][74]=Cell((74)*8,i*8,8,8,2)
                        lattice[i][74].colour=2
                        lattice[i][74].display()
                    elif lattice[i][j+1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i][j+1]=Cell((j+1)*8,i*8,8,8,2)
                        lattice[i][j+1].colour=2
                        lattice[i][j+1].display()
                    elif lattice[0][74].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[0][74]=Cell((74)*8,(0)*8,8,8,2)
                        lattice[0][74].colour=2
                        lattice[0][74].display()
                    elif lattice[0][0].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[0][0]=Cell(0*8,(0)*8,8,8,2)
                        lattice[0][0].colour=2
                        lattice[0][0].display()
                    elif lattice[0][1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[0][1]=Cell((1)*8,0*8,8,8,2)
                        lattice[0][1].colour=2
                        lattice[0][1].display()
                    #Muerte de las celulas azules
                    else:
                        if lattice[i-1][74].colour==2:
                            numdep+=1
                        if lattice[i-1][j].colour==2:
                            numdep+=1
                        if lattice[i-1][j+1].colour==2:
                            numdep+=1
                        if lattice[i][74].colour==2:
                            numdep+=1
                        if lattice[i][j+1].colour==2:
                            numdep+=1
                        if lattice[0][74].colour==2:
                            numdep+=1
                        if lattice[0][0].colour==2:
                            numdep+=1
                        if lattice[0][1].colour==2:
                            numdep+=1
                        if numdep>3 or numpres==0:
                            lattice[i][j]=Cell(j*8,i*8,8,8,0)
                            lattice[i][j].colour==0 
                            lattice[i][j].display()   
                elif lattice[i][j].colour==0:
                    if lattice[i-1][74].colour==1:
                        numpres+=1
                    if lattice[i-1][j].colour==1:
                        numpres+=1
                    if lattice[i-1][j+1].colour==1:
                        numpres+=1
                    if lattice[i][74].colour==1:
                        numpres+=1
                    if lattice[i][j+1].colour==1:
                        numpres+=1
                    if lattice[0][74].colour==1:
                        numpres+=1
                    if lattice[0][0].colour==1:
                        numpres+=1
                    if lattice[0][1].colour==1:
                        numpres+=1
                    if lattice[i-1][74].colour==2:
                        numdep+=1
                    if lattice[i-1][74].colour==2:
                        numdep+=1
                    if lattice[i-1][j+1].colour==2:
                        numdep+=1
                    if lattice[i][74].colour==2:
                        numdep+=1
                    if lattice[i][j+1].colour==2:
                        numdep+=1
                    if lattice[0][74].colour==2:
                        numdep+=1
                    if lattice[0][0].colour==2:
                        numdep+=1
                    if lattice[0][1].colour==2:
                        numdep+=1
                        #Crea celulas verdes
                    if numpres<4:
                        lattice[i][j]=Cell(j*8,i*8,8,8,1)
                        lattice[i][j].colour=1
                        lattice[i][j].display()
                    #Celulas azules creadas
                    """
                    if numdep==2 and numpres!==0:
                        lattice[i][j]=Cell(j*8,i*8,8,8,2)
                        lattice[i][j].colour=2
                        lattice[i][j].display()
                    """
        #Esquina inferior derecha
        elif i==74 and j==74:
                if lattice[i][j].colour==2:
                    if lattice[i-1][j-1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i-1][j-1]=Cell(((j-1))*8,(i-1)*8,8,8,2)
                        lattice[i-1][j-1].colour=2
                        lattice[i-1][j-1].display()
                    elif lattice[i-1][j].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i-1][j]=Cell((j)*8,(i-1)*8,8,8,2)
                        lattice[i-1][j].colour=2
                        lattice[i-1][j].display()
                    elif lattice[i-1][0].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i-1][0]=Cell((0)*8,(i-1)*8,8,8,2)
                        lattice[i-1][0].colour=2
                        lattice[i-1][0].display()
                    elif lattice[i][j-1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[0][j-1]=Cell((j-1)*8,0*8,8,8,2)
                        lattice[0][j-1].colour=2
                        lattice[0][j-1].display()
                    elif lattice[i][0].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[i][0]=Cell((0)*8,i*8,8,8,2)
                        lattice[i][0].colour=2
                        lattice[i][0].display()
                    elif lattice[0][j-1].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[0][j-1]=Cell((j-1)*8,(0)*8,8,8,2)
                        lattice[0][j-1].colour=2
                        lattice[i][j-1].display()
                    elif lattice[0][j].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[0][j]=Cell(j*8,(0)*8,8,8,2)
                        lattice[0][j].colour=2
                        lattice[0][j].display()
                    elif lattice[0][0].colour==1:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour=0
                        lattice[i][j].display()
                        lattice[0][0]=Cell((0)*8,0*8,8,8,2)
                        lattice[0][0].colour=2
                        lattice[0][0].display()
                    #Muerte de las celulas azules
                    else:
                        if lattice[i-1][j-1].colour==2:
                            numdep+=1
                        if lattice[i-1][j].colour==2:
                            numdep+=1
                        if lattice[i-1][0].colour==2:
                            numdep+=1
                        if lattice[i][j-1].colour==2:
                            numdep+=1
                        if lattice[i][0].colour==2:
                            numdep+=1
                        if lattice[0][j-1].colour==2:
                            numdep+=1
                        if lattice[0][j].colour==2:
                            numdep+=1
                        if lattice[0][0].colour==2:
                            numdep+=1
                        if numdep>2 or numpres==0:
                            lattice[i][j]=Cell(j*8,i*8,8,8,0)
                            lattice[i][j].colour==0
                            lattice[i][j].display()    
                elif lattice[i][j].colour==0:
                    if lattice[i-1][j-1].colour==1:
                        numpres+=1
                    if lattice[i-1][j].colour==1:
                        numpres+=1
                    if lattice[i-1][0].colour==1:
                        numpres+=1
                    if lattice[i][j-1].colour==1:
                        numpres+=1
                    if lattice[i][0].colour==1:
                        numpres+=1
                    if lattice[0][j-1].colour==1:
                        numpres+=1
                    if lattice[0][j].colour==1:
                        numpres+=1
                    if lattice[0][0].colour==1:
                        numpres+=1
                    if lattice[i-1][j-1].colour==2:
                        numdep+=1
                    if lattice[i-1][j].colour==2:
                        numdep+=1
                    if lattice[i-1][0].colour==2:
                        numdep+=1
                    if lattice[i][j-1].colour==2:
                        numdep+=1
                    if lattice[i][0].colour==2:
                        numdep+=1
                    if lattice[0][j-1].colour==2:
                        numdep+=1
                    if lattice[0][j].colour==2:
                        numdep+=1
                    if lattice[0][0].colour==2:
                        numdep+=1
                        #Creadas celulas verdes
                    if numpres<4:
                        lattice[i][j]=Cell(j*8,i*8,8,8,1)
                        lattice[i][j].colour=1
                        lattice[i][j].display()
                    """    
                    #Creadas celulas azules
                    if numdep==2:
                        lattice[i][j]=Cell(j*8,i*8,8,8,2)
                        lattice[i][j].colour=2
                        lattice[i][j].display()
                    """    
                        
            
            
        #FRONTERA SUPERIOR SIN ESQUINAS
        elif i==0 and j!=0 and j!=74:
             if lattice[i][j].colour==2:
                 if lattice[74][j-1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[74][j-1]=Cell((j-1)*8,(74)*8,8,8,2)
                     lattice[74][j-1].colour=2
                     lattice[74][j-1].display()        
                 elif lattice[74][j].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[74][j]=Cell((j)*8,(74)*8,8,8,2)
                     lattice[74][j].colour=2
                     lattice[74][j].display()
                 elif lattice[74][j+1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[74][j+1]=Cell((j+1)*8,(74)*8,8,8,2)
                     lattice[74][j+1].colour=2
                     lattice[74][j+1].display()
                 elif lattice[i][j-1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i][j-1]=Cell((j-1)*8,(i)*8,8,8,2)
                     lattice[i][j-1].colour=2
                     lattice[i][j-1].display()
                 elif lattice[i][j+1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i][j+1]=Cell((j+1)*8,(i)*8,8,8,2)
                     lattice[i][j+1].colour=2
                     lattice[i][j+1].display()
                 elif lattice[i+1][j-1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i+1][j-1]=Cell((j-1)*8,(i+1)*8,8,8,2)
                     lattice[i+1][j-1].colour=2
                     lattice[i+1][j-1].display()
                 elif lattice[i+1][j].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i+1][j]=Cell((j)*8,(i+1)*8,8,8,2)
                     lattice[i+1][j].colour=2
                     lattice[i+1][j].display()
                 elif lattice[i+1][j+1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i+1][j+1]=Cell((j+1)*8,(i+1)*8,8,8,2)
                     lattice[i+1][j+1].colour=2
                     lattice[i+1][j+1].display()    
                 #Muerte de las celulas azules
                 else:    
                     if lattice[74][j-1].colour==2:
                         numdep+=1
                     if lattice[74][j].colour==2:
                         numdep+=1
                     if lattice[74][j+1].colour==2:
                         numdep+=1
                     if lattice[i][j-1].colour==2:
                         numdep+=1
                     if lattice[i][j+1].colour==2:
                         numdep+=1
                     if lattice[i+1][j-1].colour==2:
                         numdep+=1
                     if lattice[i+1][j].colour==2:
                         numdep+=1
                     if lattice[i+1][j+1].colour==2:
                         numdep+=1
                     if numdep>2 or numpres==0:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour==0
                        lattice[i][j].display()
                        
             elif lattice[i][j].colour==0:
                 if lattice[74][j-1].colour==1:
                     numpres+=1
                 if lattice[74][j].colour==1:
                     numpres+=1
                 if lattice[74][j+1].colour==1:
                     numpres+=1
                 if lattice[i][j-1].colour==1:
                     numpres+=1
                 if lattice[i][j+1].colour==1:
                     numpres+=1
                 if lattice[i+1][j-1].colour==1:
                     numpres+=1
                 if lattice[i+1][j].colour==1:
                     numpres+=1
                 if lattice[i+1][j+1].colour==1:
                     numpres+=1
                 if lattice[74][j-1].colour==2:
                      numdep+=1
                 if lattice[74][j].colour==2:
                      numdep+=1
                 if lattice[74][j+1].colour==2:
                      numdep+=1
                 if lattice[i][j-1].colour==2:
                      numdep+=1
                 if lattice[i][j+1].colour==2:
                      numdep+=1
                 if lattice[i+1][j-1].colour==2:
                      numdep+=1
                 if lattice[i+1][j].colour==2:
                      numdep+=1
                 if lattice[i+1][j+1].colour==2:
                      numdep+=1
                      #Celulas creadas verdes
                 if numpres<5:
                     lattice[i][j]=Cell(j*8,i*8,8,8,1)
                     lattice[i][j].colour=1
                     lattice[i][j].display()
                     
                 #Celulas creadas azules
                 elif numdep==2 and numpres!=0:
                     lattice[i][j]=Cell(j*8,i*8,8,8,2)
                     lattice[i][j].colour=2
                     lattice[i][j].display()
            
        #Frntera inferior sin esquinas         
        elif i==74 and j!=0 and j!=74:
            #Forntera inferior
             if lattice[i][j].colour==2:
                 if lattice[i-1][j-1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i-1][j-1]=Cell((j-1)*8,(i-1)*8,8,8,2)
                     lattice[i-1][j-1].colour=2
                     lattice[i-1][j-1].display()        
                 elif lattice[i-1][j].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i-1][j]=Cell((j)*8,(i-1)*8,8,8,2)
                     lattice[i-1][j].colour=2
                     lattice[i-1][j].display()
                 elif lattice[i-1][j+1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i-1][j+1]=Cell((j+1)*8,(i-1)*8,8,8,2)
                     lattice[i-1][j-1].colour=2
                     lattice[i-1][j-1].display()
                 elif lattice[i][j-1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i][j-1]=Cell((j-1)*8,(i)*8,8,8,2)
                     lattice[i][j-1].colour=2
                     lattice[i][j-1].display()
                 elif lattice[i][j+1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[i][j+1]=Cell((j+1)*8,(i)*8,8,8,2)
                     lattice[i][j+1].colour=2
                     lattice[i][j+1].display()
                 elif lattice[0][j-1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[0][j-1]=Cell((j-1)*8,(0)*8,8,8,2)
                     lattice[0][j-1].colour=2
                     lattice[0][j-1].display()
                 elif lattice[0][j].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[0][j]=Cell((j)*8,(0)*8,8,8,2)
                     lattice[0][j].colour=2
                     lattice[0][j].display()
                 elif lattice[0][j+1].colour==1:
                     lattice[i][j]=Cell(j*8,i*8,8,8,0)
                     lattice[i][j].colour=0
                     lattice[i][j].display()
                     lattice[0][j+1]=Cell((j+1)*8,(0)*8,8,8,2)
                     lattice[0][j+1].colour=2
                     lattice[0][j+1].display()
            #Muerte de las celulas azules
                 else:
                     if lattice[i-1][j-1].colour==2:
                         numdep+=1    
                     if lattice[i-1][j].colour==2:
                         numdep+=1
                     if lattice[i-1][j+1].colour==2:
                         numdep+=1
                     if lattice[i][j-1].colour==2:
                         numdep+=1
                     if lattice[i][j+1].colour==2:
                         numdep+=1
                     if lattice[0][j-1].colour==2:
                         numdep+=1
                     if lattice[0][j].colour==2:
                         numdep+=1
                     if lattice[0][j+1].colour==2:
                         numdep+=1
                     if numdep>=1 or numpres==0:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour==0
                        lattice[i][j].display()
             #Genera nuevas celulas                        
             elif lattice[i][j].colour==0:
                 if lattice[i-1][j-1].colour==1:
                     numpres+=1
                 if lattice[i-1][j].colour==1:
                     numpres+=1
                 if lattice[i-1][j+1].colour==1:
                     numpres+=1
                 if lattice[i][j-1].colour==1:
                     numpres+=1
                 if lattice[i][j+1].colour==1:
                     numpres+=1
                 if lattice[0][j-1].colour==1:
                     numpres+=1
                 if lattice[0][j].colour==1:
                     numpres+=1
                 if lattice[0][j+1].colour==1:
                     numpres+=1
                 if lattice[i-1][j-1].colour==2:
                      numdep+=1
                 if lattice[i-1][j].colour==2:
                      numdep+=1
                 if lattice[i-1][j+1].colour==2:
                      numdep+=1
                 if lattice[i][j-1].colour==2:
                      numdep+=1
                 if lattice[i][j+1].colour==2:
                      numdep+=1
                 if lattice[0][j-1].colour==2:
                      numdep+=1
                 if lattice[0][j].colour==2:
                      numdep+=1
                 if lattice[0][j+1].colour==2:
                      numdep+=1
                      #celulas verdes creadas
                 if numpres<4:
                     lattice[i][j]=Cell(j*8,i*8,8,8,1)
                     lattice[i][j].colour=1
                     lattice[i][j].display()
                 #Celulas azules creadas
                 
                 if numdep==2 and numpres!=0:
                     lattice[i][j]=Cell(j*8,i*8,8,8,2)
                     lattice[i][j].colour=2
                     lattice[i][j].display()
                 
        
        #Frontera izquierda             
        elif j==0 and i!=0 and i!=74:
            if lattice[i][j].colour==2:
                if lattice[i-1][74].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i-1][74]=Cell(74*8,(i-1)*8,8,8,2)
                    lattice[i-1][74].colour=2
                    lattice[i-1][74].display()
                elif lattice[i-1][j].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i-1][j]=Cell(j*8,(i-1)*8,8,8,2)
                    lattice[i-1][j].colour=2
                    lattice[i-1][j].display()
                elif lattice[i-1][j+1].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i-1][j+1]=Cell((j+1)*8,(i-1)*8,8,8,2)
                    lattice[i-1][j+1].colour=2
                    lattice[i-1][j+1].display()
                elif lattice[i][74].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i][74]=Cell(74*8,i*8,8,8,2)
                    lattice[i][74].colour=2
                    lattice[i][74].display()
                elif lattice[i][j+1].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i][j+1]=Cell((j+1)*8,i*8,8,8,2)
                    lattice[i][j+1].colour=2
                    lattice[i][j+1].display()
                elif lattice[i+1][74].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][74]=Cell(74*8,(i+1)*8,8,8,2)
                    lattice[i+1][74].colour=2
                    lattice[i+1][74].display()
                elif lattice[i+1][j].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][j]=Cell(j*8,(i+1)*8,8,8,2)
                    lattice[i+1][j].colour=2
                    lattice[i+1][j].display()      
                elif lattice[i+1][j+1].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][j+1]=Cell((j+1)*8,(i+1)*8,8,8,2)
                    lattice[i+1][j+1].colour=2
                    lattice[i+1][j+1].display()
                #Muerte de las celulas azules
                else:    
                    if lattice[i-1][74].colour==2:
                        numdep+=1
                    if lattice[i-1][j].colour==2:
                        numdep+=1
                    if lattice[i-1][j+1].colour==2:
                        numdep+=1
                    if lattice[i][74].colour==2:
                        numdep+=1
                    if lattice[i][j+1].colour==2:
                        numdep+=1
                    if lattice[i+1][74].colour==2:
                        numdep+=1
                    if lattice[i+1][j].colour==2:
                        numdep+=1
                    if lattice[i+1][j+1].colour==2:
                        numdep+=1
                       
                    if numdep>=1 or numpres==0:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour==0
                        lattice[i][j].display()
                    
            #genera nuevas celulas
            elif lattice[i][j].colour==0:
                if lattice[i-1][74].colour==1:
                    numpres+=1
                if lattice[i-1][j].colour==1:
                    numpres+=1
                if lattice[i-1][j+1].colour==1:
                    numpres+=1
                if lattice[i][74].colour==1:
                    numpres+=1
                if lattice[i][j+1].colour==1:
                     numpres+=1
                if lattice[i+1][74].colour==1:
                     numpres+=1
                if lattice[i+1][j].colour==1:
                     numpres+=1
                if lattice[i+1][j+1].colour==1:
                     numpres+=1
                if lattice[i-1][74].colour==2:
                      numdep+=1
                if lattice[i-1][j].colour==2:
                      numdep+=1
                if lattice[i-1][j+1].colour==2:
                      numdep+=1
                if lattice[i][74].colour==2:
                      numdep+=1
                if lattice[i][j+1].colour==2:
                      numdep+=1
                if lattice[i+1][74].colour==2:
                      numdep+=1
                if lattice[i+1][j].colour==2:
                      numdep+=1
                if lattice[i+1][j+1].colour==2:
                      numdep+=1
                      #Celulas verdes
                if numpres<4:
                     lattice[i][j]=Cell(j*8,i*8,8,8,1)
                     lattice[i][j].colour=1
                     lattice[i][j].display()
                #Celulas azules creadas
                if numdep==2:
                     lattice[i][j]=Cell(j*8,i*8,8,8,2)
                     lattice[i][j].colour=2
                     lattice[i][j].display()
                
        #Frontera derecha
        elif j==74 and i!=0 and i!=74:
            if lattice[i][j].colour==2:
                if lattice[i-1][j-1].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i-1][j-1]=Cell((j-1)*8,(i-1)*8,8,8,2)
                    lattice[i-1][j-1].colour=2
                    lattice[i-1][j-1].display()
                elif lattice[i-1][j].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i-1][j]=Cell(j*8,(i-1)*8,8,8,2)
                    lattice[i-1][j].colour=2
                    lattice[i-1][j].display()
                elif lattice[i-1][0].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i-1][0]=Cell((j+1)*8,(i-1)*8,8,8,2)
                    lattice[i-1][0].colour=2
                    lattice[i][0].display()
                elif lattice[i][j-1].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i][j-1]=Cell((j-1)*8,i*8,8,8,2)
                    lattice[i][j-1].colour=2
                    lattice[i][j-1].display()
                elif lattice[i][0].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i][0]=Cell((0)*8,i*8,8,8,2)
                    lattice[i][0].colour=2
                    lattice[i][0].display()
                elif lattice[i+1][0].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][0]=Cell((0)*8,(i+1)*8,8,8,2)
                    lattice[i+1][0].colour=2
                    lattice[i+1][0].display()
                elif lattice[i+1][j].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][j]=Cell(j*8,(i+1)*8,8,8,2)
                    lattice[i+1][j].colour=2
                    lattice[i+1][j].display()      
                elif lattice[i+1][0].colour==1:
                    lattice[i][j]=Cell(j*8,i*8,8,8,0)
                    lattice[i][j].colour=0
                    lattice[i][j].display()
                    lattice[i+1][0]=Cell((0)*8,(i+1)*8,8,8,2)
                    lattice[i+1][0].colour=2
                    lattice[i+1][0].display()
                #Muerte de las celulas azules
                else:    
                    if lattice[i-1][j-1].colour==2:
                        numdep+=1
                    if lattice[i-1][j].colour==2:
                        numdep+=1
                    if lattice[i-1][0].colour==2:
                        numdep+=1
                    if lattice[i][j-1].colour==2:
                        numdep+=1
                    if lattice[i][0].colour==2:
                        numdep+=1
                    if lattice[i+1][j-1].colour==2:
                        numdep+=1
                    if lattice[i+1][j].colour==2:
                        numdep+=1
                    if lattice[i+1][0].colour==2:
                        numdep+=1
                    if numdep>=1 or numpres==0:
                        lattice[i][j]=Cell(j*8,i*8,8,8,0)
                        lattice[i][j].colour==0
                        lattice[i][j].display()
            #genera nuevas celulas
            elif lattice[i][j].colour==0:
                if lattice[i-1][j-1].colour==1:
                    numpres+=1
                if lattice[i-1][j].colour==1:
                    numpres+=1
                if lattice[i-1][0].colour==1:
                    numpres+=1
                if lattice[i][j-1].colour==1:
                    numpres+=1
                if lattice[i][0].colour==1:
                     numpres+=1
                if lattice[i+1][j-1].colour==1:
                     numpres+=1
                if lattice[i+1][j].colour==1:
                     numpres+=1
                if lattice[i+1][0].colour==1:
                     numpres+=1
                if lattice[i-1][j-1].colour==2:
                      numdep+=1
                if lattice[i-1][j].colour==2:
                      numdep+=1
                if lattice[i-1][0].colour==2:
                      numdep+=1
                if lattice[i][j-1].colour==2:
                      numdep+=1
                if lattice[i][0].colour==2:
                      numdep+=1
                if lattice[i+1][j-1].colour==2:
                      numdep+=1
                if lattice[i+1][j].colour==2:
                      numdep+=1
                if lattice[i+1][0].colour==2:
                      numdep+=1
                      #Crea celulas verdes
                if numpres<4:
                     lattice[i][j]=Cell(j*8,i*8,8,8,1)
                     lattice[i][j].colour=1
                     lattice[i][j].display()
                     #Crea celulas azules
                """     
                if numdep<2:
                     lattice[i][j]=Cell(j*8,i*8,8,8,2)
                     lattice[i][j].colour=2
                     lattice[i][j].display()
                """
                
                         
    return lattice

def contando(lattice):
    global nRows, nCols
    contar=0
    contar2=0
    for i in range(nRows):
        for j in range(nCols):
            if lattice[i][j].colour==2:
                contar+=1
            if lattice[i][j].colour==1:
               contar2+=1 
    return(contar,contar2)               
                
def evolucion():
    global nCols,nRows,contar,contar2,grid,tim
    tim+=1
    for i in range(nRows):
        for j in range(nCols):
            #Se encarga de evaluar las cellulas que no están en las orrillas
            #evalua los vecindarios
            grid=vecindario(grid,i,j,grid[i][j].colour)


    valores=list(contando(grid))
    valores.append(tim)
    imp=str(valores[0])+","+str(valores[1])+","+str(valores[2])
    archivo = open("datos.txt", "r+")
    contenido = archivo.read()
    final_de_archivo=archivo.tell()
    archivo.write(imp+'\n')
    archivo.seek(final_de_archivo)
    archivo.close()
                          