num = int(input("Enter a number to print its multiplication table: "))

print("Multiplication Table for", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
