#----------------------------------------------------Lattice size--------------------------------------------------------------------
nCols=75
nRows=75
n=0
xp,yp=670,590-1/12
flag=False
#----------------------------------------------------Begining-------------------------------------------------------------------------
def setup():
    global nCols,nRows,grid
    background(240)
    size(1200,600)
    iniciar()
    num=count(grid)
    line(670,590-1/12,1200,590-1/12)
    line(670,590-1/12,670,1)
    delay(100)
    
    
#----------------------------------------------------Draw our lattice-----------------------------------------------------------------
def draw():
    global nCols,nRows,grid,n,xp,yp,flag
    if flag==True:
        n+=1
        print(n) 
        evolucion()
        number=count(grid)
        #print(number)
        xp,yp=graph(number,n,xp,yp)
        delay(100)
        
def mousePressed():
    global nCols,nRows,grid,flag
    iniciar()
    flag=True
    
    
    
    

        
#----------------------------------------------------Begining Conditional ------------------------------------------------------------     
def iniciar():
    global grid,count
    grid=makeGrid()
    for i in range(nRows):
        for j in range(nCols):
            c=0
            grid[i][j]=Cell(j*8,i*8,8,8,c)
            grid[i][j].colour=c
            grid[i][j].display()
            if i==10 and j==50: #Our infected person
                c=1
                grid[i][j]=Cell(j*8,i*8,8,8,c)
                grid[i][j].colour=c
                grid[i][j].display()
    return(grid)

#------------------------------------------------------25X25 Lattice------------------------------------------------------------------
def makeGrid():
    global nCols,nRows
    grid=[]
    for i in range(nRows):
        grid.append([])
        for j in range(nCols):
            grid[i].append(0)
    return(grid)

#------------------------------------------------------Cell class---------------------------------------------------------------------
class Cell():
    colour=0
    def __init__(self,X,Y,W,H,C):
        self.x=X
        self.y=Y
        self.w=W
        self.h=H
        self.c=C #colour
        colour=self.c
        
    def display(self):
        stroke(0)
        if self.c==0:
            #Healthy
            fill(50)
            rect(self.x,self.y,self.w,self.h)
        elif self.c==1:
            #Sick
            fill(0,0,255)
            rect(self.x,self.y,self.w,self.h)
#----------------------------------------------------Disease spreading-----------------------------------------------------------------
def evaluation(lattice,i,j):
    if i!=0 and i!=74 and j!=0 and j!=74:
        if lattice[i][j].colour==1:
             a=0.1
             if lattice[i-1][j-1].colour==0:
                 val=random(1)
                 if val<a:
                    lattice[i-1][j-1]=Cell((j-1)*8,(i-1)*8,8,8,1)
                    lattice[i-1][j-1].colour=1
                    lattice[i-1][j-1].display()
                        
             if lattice[i-1][j].colour==0:
                 val=random(1)
                 if val<a:
                     lattice[i-1][j]=Cell((j)*8,(i-1)*8,8,8,1)
                     lattice[i-1][j].colour=1
                     lattice[i-1][j].display()
                
             if lattice[i-1][j+1].colour==0:
                 val=random(1)
                 if val<a:
                     lattice[i-1][j+1]=Cell((j+1)*8,(i-1)*8,8,8,1)
                     lattice[i-1][j+1].colour=2
                     lattice[i-1][j+1].display()
                
             if lattice[i][j-1].colour==0:
                 val=random(1)
                 if val<a:
                     lattice[i][j-1]=Cell((j-1)*8,(i)*8,8,8,1)
                     lattice[i][j-1].colour=1
                     lattice[i][j-1].display()
                
             if lattice[i][j+1].colour==0:
                 val=random(1)
                 if val<a:
                     lattice[i][j+1]=Cell((j+1)*8,(i)*8,8,8,1)
                     lattice[i][j+1].colour=1
                     lattice[i][j+1].display()
                 
             if lattice[i+1][j-1].colour==0:
                 val=random(1)
                 if val<a:
                     lattice[i+1][j-1]=Cell((j-1)*8,(i+1)*8,8,8,1)
                     lattice[i+1][j-1].colour=1
                     lattice[i+1][j-1].display()
                
             if lattice[i+1][j].colour==0:
                 val=random(1)
                 if val<a:
                     lattice[i+1][j]=Cell((j)*8,(i+1)*8,8,8,1)
                     lattice[i+1][j].colour=1
                     lattice[i+1][j].display()
                
             if lattice[i+1][j+1].colour==0:
                 val=random(1)
                 if val<a:
                     lattice[i+1][j+1]=Cell((j+1)*8,(i+1)*8,8,8,1)
                     lattice[i+1][j+1].colour=1
                     lattice[i+1][j+1].display()     
    return(lattice)      
#--------------------------------------------------------------------evolution--------------------------------------------------------------------          
def evolucion():
    global nCols,nRows,grid
    for i in range(nRows):
        for j in range(nCols):
            grid=evaluation(grid,i,j)

def count(lattice):
    global nCols,nRows,grid
    num=0
    for i in range(nRows):
        for j in range(nCols):
            num+=lattice[i][j].colour
    return(num)

def graph(number,n,xp,yp):
    fill(255)
    rect(600,0,600,90)
    fill(0)
    ellipse(670+8*n/2, 590-number/12,4,4)
    
    line(xp,yp,670+8*n/2, 590-number/12)
    fill(0);
    textSize(30)
    text("Infected cells",850,20,500,50)
    text(str(number),900,50,500,50)
    for i in range(13):
        line(665,590-500*i/12,1200,590-500*i/12)
        line(670+500*i/12,93,670+500*i/12,600)
    return(670+8*n/2,590-number/12)

                                                                                                                                                                                                                                                               
