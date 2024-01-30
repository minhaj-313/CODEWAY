'''
Task - 2

'''
print("▪️▪️▪️▪️▪️Simple Calculator▪️▪️▪️▪️▪️")
print("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️")

i1 = float(input("Enter 1st Number : "))
i2 = float(input("Enter 2nd Number : "))

print("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️")
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Modulo")
print("Enter 6 for Floor Division")
print("Enter 7 for Exponential")
print("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️")

choice = int(input("Enter your Choice from 1 to 7"))

if choice == 1:
    print("Addition of Two Number is :",i1 + i2)
elif choice == 2:
    print("Subtraction of Two Number is : ",i1 - i2)
elif choice ==3:
    print("Multiplication of Two Number is : ",i1 * i2)
elif choice ==4:
    print("Division of Two Number is : ",i1 / i2)
elif choice ==5:
    print("Modulo of Two Number is : ",i1 % i2)
elif choice ==6:
    print("Floor Division of Two Number is : ",i1 // i2)
elif choice ==7:
    print("Exponential of Two Number is :",i1 ** i2)   
else:
    print("❌Invalid Input❌")
    
print("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️")    