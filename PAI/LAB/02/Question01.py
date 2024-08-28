def trapezoid(a,b,h):
    area = ((a+b)/2)*h
    return area


def parallelogram(b,h):
    area = b*h
    return area


def cylinder(r,h):
    area = 2*3.14*r*h + 2*3.14*r*r
    return area


def volume(r,h):
    volume = 3.14 * r * r * h
    return volume

a = int(input("Enter the value of Base A: "))
b = int(input("Enter the value of Base B: "))
h = int(input("Enter the height: "))
print("The area of trapezoid: ", trapezoid(a,b,h))

B = int(input("Enter the Base: "))
H = int(input("Enter the height: "))
R = int(input("Enter the Radius: "))
print("The area of parallelogram: ", parallelogram(B,H))
print("The area of cylinder: ", cylinder(R,H))
print("The surface volume of cylinder: ", volume(R,H))