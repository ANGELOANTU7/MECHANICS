import math
from tarfile import LENGTH_PREFIX
import centroid





ixx=float(0)
iyy=float(0)
cen=float(0)
c=float(0)
area=float(0)
hh=centroid.cent()
cx=hh[0]
cy=hh[1]
a=int(input("Enter no. of shapes "))

print(cx,cy)
for k in range (0,a):
    ch=int(input("Enter the type of shape 1.rec 2.semi 3.tri 4.quarter :"))
    if ch==1:
        b=float(input("Enter breath :"))
        h=float(input("Enter height :"))
        x=float(input("Enter x distance :"))
        y=float(input("Enter y distance :"))
        s=int(input("positive or negative (1/-1) : "))
        a=b*h
        if s==1:
            
            ixx=ixx+(b*(h**3)/12)+(b*h*((y-cy)**2))
            iyy=iyy+((b**3)*(h)/12)+(b*h*((x-cx)**2))


        if s==-1:
            
            ixx=ixx-(b*(h**3)/12)-(b*h*((y-cy)**2))
            iyy=iyy-((b**3)*(h)/12)-(b*h*((x-cx)**2))
        
        print(ixx,iyy)

    if ch==2:
        r=float(input("Enter Radius :"))
        x=float(input("Enter x distance :"))
        y=float(input("Enter y distance :"))
        s=int(input("positive or negative (1/-1) : "))
        a=(math.pi/2)*r**2
        if s==1:
            
            ixx=ixx+(0.11*(r**4)+(math.pi/2*(r**2))*((y-cy)**2))
            iyy=iyy+(math.pi*(r**4))/8+a*(x-cx)**2
        if s==-1:
            
            ixx=ixx-(0.11*(r**4)+(math.pi/2*(r**2))*((y-cy)**2))
            iyy=iyy-(math.pi*(r**4))/8-a*(x-cx)**2
        
        print(ixx,iyy)


    if ch==3:
        b=float(input("Enter base :"))
        h=float(input("Enter height :"))
        x=float(input("Enter x distance :"))
        y=float(input("Enter y distance :"))
        s=int(input("positive or negative (1/-1) : "))
        a=(1/2)*b*h
        if s==1:
            
            ixx=ixx+(b*(h**3)/36+((b/2)*h)*(y-cy)**2)
            iyy=iyy+( (b**3)*(h)-(b**2)*(h)*(b/2)+b*(h)*(b/2)**2 )/36 + a*(x-cx)**2
        if s==-1:
            
            ixx=ixx-(b*(h**3)/36+(b/2*h)*(y-cy)**2)
            iyy=iyy-( (b**3)*(h)-(b**2)*(h)*(b/2)+b*(h)*(b/2)**2 )/36 - a*(x-cx)**2

        print(ixx,iyy)



    if ch==4:
        r=float(input("Enter Radius :"))
        x=float(input("Enter x distance :"))
        y=float(input("Enter y distance :"))
        s=int(input("positive or negative (1/-1) : "))
        a=(math.pi/4)*r**2
        if s==1:
            
            ixx=ixx+(0.055*(r**4)+(math.pi/4*(r**2))*((y-cy)**2))
            iyy=iyy+ 0.055*(r**4)+ a*(x-cx)**2
        if s==-1:
            
            ixx=ixx-(0.055*(r**4)+(math.pi/4*(r**2))*((y-cy)**2))
            iyy=iyy- 0.055*(r**4)- a*(x-cx)**2
        
        print(ixx,iyy)
       
    print("IXX:",ixx)
    print("IYY:",iyy)
        
    




