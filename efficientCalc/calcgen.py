#open the calc.py file
f = open("calc.py", "w")

#adds the input and print statements
f.write("print('This is a calculator')\n")
f.write("print('Please enter the first number')\n")
f.write("a = int(input())\n")
f.write("print('Please enter the second number')\n")
f.write("b = int(input())\n")
f.write("print('Please enter the operation')\n")
f.write("op = input()\n")

#loops for addition, subtraction, multiplication, and division
for i in range(100):
    for j in range(100):
        f.write("#adds " + str(i) + " and " + str(j) + "\n")
        f.write("if op == '+' and a == " + str(i) + " and b == " + str(j) + ":\n")
        f.write("    print(" + str(i) + " + " + str(j) + ")\n")
for i in range(100):
    for j in range(100):
        f.write("#subtracts " + str(i) + " and " + str(j) + "\n")
        f.write("if op == '-' and a == " + str(i) + " and b == " + str(j) + ":\n")
        f.write("    print(" + str(i) + " - " + str(j) + ")\n")
for i in range(100):
    for j in range(100):
        f.write("#multiplies " + str(i) + " and " + str(j) + "\n")
        f.write("if op == '*' and a == " + str(i) + " and b == " + str(j) + ":\n")
        f.write("    print(" + str(i) + " * " + str(j) + ")\n")
for i in range(100):
    for j in range(100):
        f.write("#divides " + str(i) + " and " + str(j) + "\n")
        f.write("if op == '/' and a == " + str(i) + " and b == " + str(j) + ":\n")
        f.write("    print(" + str(i) + " / " + str(j) + ")\n")

#close the file
f.close()