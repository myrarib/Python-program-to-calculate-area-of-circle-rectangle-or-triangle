#program to calculate area of circle, rectangle or triangle
#created on: November 1st 2020
#By: Myra Ribeiro

print("Welcome to the program that calculates the area of specific shapes!")

#prompt user to enter the shape they want to calculate
name = input("Please enter the name of the shape in which you want to calculate the area of (rectangle, circle, triangle) - do not put a space inbetween the shape name and the colon. Shape name:")

#calculate area of rectangle	
if name == "rectangle":
    #define rectangle length and width
	length = float(input("Please enter rectangle length:"))
	width = float(input("please enter rectangle width:"))
	#calculate rectangle area
	area_of_rectangle = length*width
	print("area of the rectangle is...", area_of_rectangle)
#calculare area of triangle
elif name == "triangle":
    #define triangle base and height
	base = float(input("please enter triangles base:"))
	height = float(input("please enter triangles height:"))
	#calculate triangle area
	area_of_triangle = base*height/2
	print("area of triangle is...",area_of_triangle)
#calculate area of circle
elif name == "circle":
    #define what the radius of circle is
	radius = float(input("please enter circle radius:"))
	#calculate circle area
	area_of_circle = radius**2*3.14
	print("area of circle is...",area_of_circle)
else: print("Sorry! none of those are options, please try again and enter either circle, triangle, or rectangle! (make sure you don't have any spaces)")

print("Thank you for using the program!")



