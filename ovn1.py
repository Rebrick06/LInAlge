'''
Skapa en funktion f (P ) som tar en punkt P, och f¨orst reflekterar den i
planet (genom origo) vinkelr¨att mot (1, 2, 2) och sedan i planet (genom
origo) vinkelr¨att mot (−1, 3, −1).
L˚at P = (1, 1, 1), och f (n)(P ) = f (f (· · · f (P ))), d.v.s. f applicerad n
g˚anger p˚a P. Plotta punkterna P, f (P ), f (f (P )), . . . , f (n)(P ) (i en 3D-
plot), d˚
''' 

def funktion(x):
    n=(1,2,2)
    y= x-2*((x*n)/(n**2))*n

    n = (-1, 3, -1)
    y= y-2*((y*n)/(n**2))*n
