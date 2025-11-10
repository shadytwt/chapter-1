a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))


if (a + b >= c) and (a + c >= b) and (b + c >= a):
    print("\nYes, the given sides can form a triangle.")

   
    if a == b == c:
        print("This is an Equilateral triangle.")
    elif a == b or a == c or b == c:
        print("This is an Isosceles triangle.")
    else:
        print("This is a Scalene triangle.")

else:
    print("\nNo, the given sides cannot form a triangle.")
