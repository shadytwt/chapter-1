import math

def area_square():
    side = float(input("Enter the length of the square's side: "))
    area = side ** 2
    print(f"Area of the square: {area:.2f}")

def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"Area of the circle: {area:.2f}")

def area_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of the triangle: {area:.2f}")

print("Choose an option:")
print("1: Calculate the area of a square")
print("2: Calculate the area of a circle")
print("3: Calculate the area of a triangle")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    area_square()
elif choice == '2':
    area_circle()
elif choice == '3':
    area_triangle()
else:
    print("Invalid choice! Please select 1, 2, or 3.")
