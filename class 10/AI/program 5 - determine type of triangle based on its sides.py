## determine type of triangle based on its sides

## get input for length of sides
side1=float(input("Enter the length of the first side: "))
side2=float(input("Enter the length of the second side: "))
side3=float(input("Enter the lenght of the third side: "))
 
## checking the type of the triangle based on sides

if side1==side2==side3:
    print("It is an equalateral triangle")
elif side1==side2 or side2==side3 or side1==side3:
    print("It is an isosceles triangle")
else:
    print("It is a scalene triangle")
