def multiply(x, y, z):
    return x * y * z

def divide(x, y): 
    return x / y

print("Select operation.")
print("1. wheat")
print("2. Canola")
print("3. Oats and triticale")
print("4. Lentils")
print("5. Safflower")
print("6. Barley")
print("7. Lupin (narrow leaf)")
print("8. chickpea (desi)")
print("9. Field pea")
print("10. Lupin (broad leaf)")
print("11. Chickpea (kabuli)")
print("12. Faba bean")
while True:
    choice = input("Enter choice: ")
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'):
        num1 = float(input("Enter average of heads per 1m2: "))
        num2 = float(input("Enter average of grains per heads: "))
        pog = 10000
        y = "t/ha Yield "
        if choice == '1':
            num3 = 3.4
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '2':
            num3 = 0.4
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '3':
            num3 = 4
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '4':
            num3 = 3
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '5':
            num3 = 3.8
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '6':
            num3 = 4.2
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '7':
            num3 = 16
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '8':
            num3 = 18
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '9':
            num3 = 20
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '10':
            num3 = 30
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '11':
            num3 = 40
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        elif choice == '12':
            num3 = 50
            nock = multiply(num1, num2, num3)
            print(divide(nock, pog),y)

        break
    else:
        print("Invalid Input")
