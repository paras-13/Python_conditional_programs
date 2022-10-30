# Program to find area of a triangle using its sides (Heron's formula)

#Taking sides of the triangle from the user
# Let their is a triangle ABC

# NOTE:- Sides to be entered in integer not in floating point.

side_AB = int(input("Enter the length of the side AB of triangle ABC in cm"))
side_BC = int(input("Enter the length of the side BC of triangle ABC in cm"))
side_AC = int(input("Enter the length of the side AC of the triangle ABC in cm"))
perimeter = side_AB + side_BC + side_AC
S = perimeter / 2                                          # Here S represents Semi_perimeter
a , b , c = S-side_AB , S-side_BC , S-side_AC

# Heron's formula = (S*a*b*c)**0.5

val = S*a*b*c
area = val**0.5
print('Area of the triangle ABC is -->',area,end=" ")
print(". Which is approximately",round(area),"cm square")