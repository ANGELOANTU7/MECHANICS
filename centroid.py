import math,csv,os

from click import option



def puto (a):
    aa="OPTION.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerows([a]) 
        csvfile.close()
    print("done")

def putrec (a):
    aa="REC.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerows([a]) 
        csvfile.close()
    print("done")

def putsemi (a):
    aa="SEMI.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerows([a]) 
        csvfile.close()
    print("done")

def puttri (a):
    aa="TRI.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerows([a]) 
        csvfile.close()
    print("done")

def putquad (a):
    aa="QUAD.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerows([a]) 
        csvfile.close()
    print("done")

def putcircle (a):
    aa="CIRCLE.csv"
    with open(aa,mode='a',newline="") as csvfile :     #feeding each values to csv
        mywriter=csv.writer(csvfile)
        mywriter.writerows([a]) 
        csvfile.close()
    print("done")


def check():
    if(os.path.exists("OPTION.csv") and os.path.isfile("OPTION.csv")):
        os.remove("OPTION.csv")

    if(os.path.exists("REC.csv") and os.path.isfile("REC.csv")):
        os.remove("REC.csv")

    if(os.path.exists("SEMI.csv") and os.path.isfile("SEMI.csv")):
        os.remove("SEMI.csv")

    if(os.path.exists("TRI.csv") and os.path.isfile("TRI.csv")):
        os.remove("TRI.csv")

    if(os.path.exists("QUAD.csv") and os.path.isfile("QUAD.csv")):
        os.remove("QUAD.csv")

    if(os.path.exists("CIRCLE.csv") and os.path.isfile("CIRCLE.csv")):
        os.remove("CIRCLE.csv")




def cent():


    check()
    a=int(input("Enter no. of shapes "))



    ixx=float(0)
    cen=float(0)
    c=float(0)
    c1=float(0)
    area=float(0)

    


    for k in range (0,a):
        ch=int(input("Enter the type of shape 1.rec 2.semi 3.tri 4.quarter 5.circle :"))
        puto([ch])

        if ch==1:
            b=float(input("Enter breath :"))
            h=float(input("Enter height :"))
            x=float(input("Enter x distance :"))
            y=float(input("Enter y distance :"))
            s=int(input("positive or negative (1/-1) : "))
            a=b*h
            rec=[b,h,x,y,s,a]
            putrec(rec)
            if s==1:
                c=c+a*x
                c1=c1+a*y
                area=area+a

            if s==-1:
                c=c-a*x
                c1=c1-a*y
                area=area-a
            


        if ch==2:
            r=float(input("Enter Radius :"))
            x=float(input("Enter x distance :"))
            y=float(input("Enter y distance :"))
            s=int(input("positive or negative (1/-1) : "))
            a=(math.pi/2)*r**2
            semi=[r,x,y,s,a]
            putsemi(semi)
            if s==1:
                c=c+a*x
                c1=c1+a*y
                area=area+a
            if s==-1:
                c=c-a*x
                c1=c1-a*y
                area=area-a
        
        


        if ch==3:
            b=float(input("Enter base :"))
            h=float(input("Enter height :"))
            x=float(input("Enter x distance :"))
            y=float(input("Enter y distance :"))
            s=int(input("positive or negative (1/-1) : "))
            a=(1/2)*b*h
            tri=[b,h,x,y,s,a]
            puttri(tri)
            if s==1:
                c=c+a*x
                c1=c1+a*y
                area=area+a
            if s==-1:
                c=c-a*x
                c1=c1-a*y
                area=area-a
       
        
        if ch==4:
            r=float(input("Enter Radius :"))
            x=float(input("Enter x distance :"))
            y=float(input("Enter y distance :"))
            s=int(input("positive or negative (1/-1) : "))
            a=((math.pi)*r**2)/4
            quad=[r,x,y,s,a]
            putquad(quad)
            if s==1:
                c=c+a*x
                c1=c1+a*y
                area=area+a
            if s==-1:
                c=c-a*x
                c1=c1-a*y
                area=area-a
          
        if ch==5:
            r=float(input("Enter Radius :"))
            x=float(input("Enter x distance :"))
            y=float(input("Enter y distance :"))
            s=int(input("positive or negative (1/-1) : "))
            a=((math.pi)*r**2)
            circle=[r,x,y,s,a]
            putcircle(circle)
            if s==1:
                c=c+a*x
                c1=c1+a*y
                area=area+a
            if s==-1:
                c=c-a*x
                c1=c1-a*y
                area=area-a


    cen=c/area
    cen1=c1/area
    print("X CENTROID:",cen)
    print("Y CENTROID:",cen1)

    return(cen,cen1)


