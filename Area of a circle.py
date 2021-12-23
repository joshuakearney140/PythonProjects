
class bcolors:
    WARNING = '\033[91m'
    ENDC = '\033[0m'

print("Area calculator is running...")
print("This is in cm")


reinput = True
while True:
    shape = input("What shape would you like to find the area of Circle or triangle C/T: ")

    if shape.upper() =='C':

        radius = float(input("Insert the radius of the circle in cm: "))
        areac = 3.14159 * radius ** 2
        print("The area of your circle is " + str(areac))
        break

    if shape.upper() == 'T':

        base = float(input("What is the base of your triangle? "))
        height = float(input("What is the height of your triangle? "))
        areat = 0.5 * base * height
        print("Answer is " + str(areat))
        break

    elif len(shape) <= 0:
        print(f"{bcolors.WARNING}Please enter a value!{bcolors.ENDC}")

    else:
        print(f"{bcolors.WARNING}Error Please Enter C/T!{bcolors.ENDC}")
        reinput = True
