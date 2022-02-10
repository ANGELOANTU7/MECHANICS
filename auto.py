import math
from tarfile import LENGTH_PREFIX
import centroid,os,csv
from ast import Eq

from numpy import mat
from sympy import symbols,Eq,solve


def telloption():
    with open("OPTION.csv",mode='r') as csvfile :     
        data=list(csv.reader(csvfile))                 #gotta call specfic plant csv
        csvfile.close()

        x=int(data[0][0])
        return x

def tellrec(a,b):
    with open("REC.csv",mode='r') as csvfile :     
        data=list(csv.reader(csvfile))                 #gotta call specfic plant csv
        csvfile.close()

        num=len(data)
        if a==6 and b==9:
            return num
        else:    
            x=float(data[a][b])
            return x


def tellsemi(a,b):
    with open("SEMI.csv",mode='r') as csvfile :     
        data=list(csv.reader(csvfile))                 #gotta call specfic plant csv
        csvfile.close()

        num=len(data)
        if a==6 and b==9:
            return num
        else:    
            x=float(data[a][b])
            return x

def telltri(a,b):
    with open("TRI.csv",mode='r') as csvfile :     
        data=list(csv.reader(csvfile))                 #gotta call specfic plant csv
        csvfile.close()

        num=len(data)
        if a==6 and b==9:
            return num
        else:    
            x=float(data[a][b])
            return x

def tellquad(a,b):
    with open("QUAD.csv",mode='r') as csvfile :     
        data=list(csv.reader(csvfile))                 #gotta call specfic plant csv
        csvfile.close()

        num=len(data)
        if a==6 and b==9:
            return num
        else:    
            x=float(data[a][b])
            return x

def tellcircle(a,b):
    with open("CIRCLE.csv",mode='r') as csvfile :     
        data=list(csv.reader(csvfile))                 #gotta call specfic plant csv
        csvfile.close()

        num=len(data)
        if a==6 and b==9:
            return num
        else:    
            x=float(data[a][b])
            return x

def check(a):
    if(os.path.exists("OPTION.csv") and os.path.isfile("OPTION.csv") and a==0):
        noption=telloption()
        return(noption)

    if(os.path.exists("REC.csv") and os.path.isfile("REC.csv") and a==1):
        nrec=tellrec(6,9)
        return(nrec)

    if(os.path.exists("SEMI.csv") and os.path.isfile("SEMI.csv") and a==2):
        nsemi=tellsemi(6,9)
        return(nsemi)

    if(os.path.exists("TRI.csv") and os.path.isfile("TRI.csv") and a==3):
        ntri=telltri(6,9)
        return(ntri)

    if(os.path.exists("QUAD.csv") and os.path.isfile("QUAD.csv") and a==4):
        nquad=tellquad(6,9)
        return(nquad)

    if(os.path.exists("CIRCLE.csv") and os.path.isfile("CIRCLE.csv") and a==5):
        ncircle=tellcircle(6,9)
        return(ncircle)

    else:
        return(0)






ixx=float(0)
iyy=float(0)
ixy=float(0)
cen=float(0)
c=float(0)
area=float(0)
hh=centroid.cent()
cx=hh[0]
cy=hh[1]



print(cx,cy)


nrec=check(1)
nsemi=check(2)
ntri=check(3)
nquad=check(4)
ncircle=check(5)

for k in range (0,1):
    print("dimension"," ","area","x","y","xi","yi","ixx","iyy")    
    
    for k1 in range (0,nrec):
        b=tellrec(k1,0)
        h=tellrec(k1,1)
        x=tellrec(k1,2)
        y=tellrec(k1,3)
        s=tellrec(k1,4)
        a=tellrec(k1,5)
        if s==1:
                
            ixx=ixx+(b*(h**3)/12)+(b*h*((y-cy)**2))
            iyy=iyy+((b**3)*(h)/12)+(b*h*((x-cx)**2))
            ixy=ixy+0+a*(x-cx)*(y-cy)
            print("ixx= (b*h^3)/12 + A(y-y')^2    ")

        if s==-1:
                
            ixx=ixx-(b*(h**3)/12)-(b*h*((y-cy)**2))
            iyy=iyy-((b**3)*(h)/12)-(b*h*((x-cx)**2))
            ixy=ixy+0-a*(x-cx)*(y-cy)
            print("ixx= - (b*h^3)/12 - A(x-x')^2    ")
            
        print("B",b,"x","H",h," ","IXX",ixx,"IYY",iyy,"rec")   

   
    for k2 in range (0,nsemi):
        r=tellsemi(k2,0)
        x=tellsemi(k2,1)
        y=tellsemi(k2,2)
        s=tellsemi(k2,3)
        a=tellsemi(k2,4)
        if s==1:
                
            ixx=ixx+(0.11*(r**4)+(math.pi/2*(r**2))*((y-cy)**2))
            iyy=iyy+(math.pi*(r**4))/8+a*(x-cx)**2
            ixy=ixy+0+a*(x-cx)*(y-cy)
            print("ixx= 0.11*r^4 + A(y-y')^2    ")
            
        if s==-1:
                
            ixx=ixx-(0.11*(r**4)+(math.pi/2*(r**2))*((y-cy)**2))
            iyy=iyy-(math.pi*(r**4))/8-a*(x-cx)**2
            ixy=ixy+0-a*(x-cx)*(y-cy)
            print("ixx= - 0.11*r^4 - A(y-y')^2    ")
            
        print("RADIUS",r," ","AREA",a,"IXX",ixx,"IYY",iyy,"semi")


    
    for k3 in range (0,ntri):
        b=telltri(k3,0)
        h=telltri(k3,1)
        x=telltri(k3,2)
        y=telltri(k3,3)
        s=telltri(k3,4)
        a=telltri(k3,5)
        if s==1:
                
            ixx=ixx+(b*(h**3)/36+((b/2)*h)*(y-cy)**2)
            iyy=iyy+( (b**3)*(h)-(b**2)*(h)*(b/2)+b*(h)*(b/2)**2 )/36 + a*(x-cx)**2
            ixy=ixy-(b**2)*((h**2)/72)+a*(x-cx)*(y-cy)
            print("ixx= (b*h^3)/36 + A(y-y')^2    ")
            
        if s==-1:
                
            ixx=ixx-(b*(h**3)/36+(b/2*h)*(y-cy)**2)
            iyy=iyy-( (b**3)*(h)-(b**2)*(h)*(b/2)+b*(h)*(b/2)**2 )/36 - a*(x-cx)**2
            ixy=ixy+(b**2)*((h**2)/72)-a*(x-cx)*(y-cy)
            print("ixx= ( b^3*h - b^2*h*a - b*h*a^2 )/36 + A(y-y')^2    ")

        print("BASE",b,"x","HEIGHT",h," ","IXX",ixx,"IYY",iyy,"tri")



    print(nquad)
    for k4 in range (0,nquad):
        r=tellquad(k4,0)
        x=tellquad(k4,1)
        y=tellquad(k4,2)
        s=tellquad(k4,3)
        a=tellquad(k4,4)
        if s==1:
                
            ixx=ixx+(0.055*(r**4)+(math.pi/4*(r**2))*((y-cy)**2))
            iyy=iyy+ 0.055*(r**4)+ a*(x-cx)**2
            ixy=ixy+0+a*(x-cx)*(y-cy)
            print("ixx= 0.55*r^4 + A(y-y')^2    ")
        if s==-1:
                
            ixx=ixx-(0.055*(r**4)+(math.pi/4*(r**2))*((y-cy)**2))
            iyy=iyy- 0.055*(r**4)- a*(x-cx)**2
            ixy=ixy+0-a*(x-cx)*(y-cy)
            print("ixx= - 0.55*r^4 - A(y-y')^2    ")
            
        print("RADIUS",r," ","AREA",a,"IXX",ixx,"IYY",iyy,"quad")

    
    for k5 in range (0,ncircle):
        r=tellcircle(k5,0)
        x=tellcircle(k5,1)
        y=tellcircle(k5,2)
        s=tellcircle(k5,3)
        a=tellcircle(k5,4)
        
        if s==1:
                
            ixx=ixx+((math.pi/4)*r**4+(math.pi*(r**2))*((y-cy)**2))
            iyy=iyy+ (math.pi/4)*r**4+ a*(x-cx)**2
            ixy=ixy+0+a*(x-cx)*(y-cy)
            print("ixx= (pi*r^4)/4 + A(y-y')^2    ")
        if s==-1:
                
            ixx=ixx+((math.pi/4)*r**4+(math.pi*(r**2))*((y-cy)**2))
            iyy=iyy- (math.pi/4)*r**4- a*(x-cx)**2
            ixy=ixy+0-a*(x-cx)*(y-cy)
            print("ixx= - (pi*r^4)/4 - A(y-y')^2    ")
            
        print("RADIUS",r," ","AREA",a,"IXX",ixx,"IYY",iyy,"circle")
       
ask=str(input("do you want to find ix'x' and iy'y'   (y/n): "))
if ask=='y':
    te=float(input("enter angle given if none ignore ix'x' and iy'y'"))
    ix1x1=((ixx+iyy)/2)+(ixx-iyy)/2*math.cos(2*te)-ixy*math.sin(2*te)
    iy1y1=((ixx+iyy)/2)-(ixx-iyy)/2*math.cos(2*te)+ixy*math.sin(2*te)
    ix1y1=((ixx-iyy)/2)*math.sin(2*te)+ixx*(math.cos(te)**2-math.sin(te)**2)
    tetha=math.atan((2*ixy)/(iyy-ixx))*180/(math.pi*2)
    imax=(ixx+iyy)/2+( ((ixx-iyy)/2)**2 + ixy**2 )**(1/2)
    imin=(ixx+iyy)/2-( ((ixx-iyy)/2)**2 + ixy**2 )**(1/2)

print("X CENTROID :",cx)
print("Y CENTROID :",cy)

print("IXX:",ixx)
print("IYY:",iyy)
print("IZZ",ixx+iyy)
print("IXY",ixy)

print("IX'X':",ix1x1)
print("IY'Y':",iy1y1)
print("IX'Y':",ix1y1)
print("principal axis at :",tetha)
print("I max :",imax)
print("I min :",imin)


        
    




