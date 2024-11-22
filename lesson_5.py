import calculator as cal

num_1 = int(input("Input 1 num: "))
num_2 = int(input("Input 1 num: "))
znak = input("Input znak: ")
if znak == "+":
    print(cal.add(num_1, num_2))
elif znak == "-":
    print(cal.subtract(num_1, num_2))
elif znak == "*":
    print(cal.multiply(num_1, num_2))
elif znak == "/":
    print(cal.divide(num_1, num_2))
else:
    print("Not define!!!")


