side_a=float(input("Enter the dimensions of the first side"))
side_b=float(input("Enter the dimensions of the second side"))
side_c=float(input("Enter the dimensions of the third side"))
if side_a + side_b >side_c and side_b + side_c > side_a and side_a + side_c > side_b:
    print("The dimensions you have entered are",side_a,side_b,side_c,"They will form a triangle")
else:
    print("The dimensions you have entered are",side_a,side_b,side_c,"They will not form a triangle")