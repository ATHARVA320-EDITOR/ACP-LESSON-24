number = int(input("Enter a number: "))
number2 = int(input("Enter 2nd number: "))
number3= int(input("Enter 3rd number: "))
number4 = int(input("Enter 4th number: "))
list = [number, number2, number3, number4]
print("The list is:" ,list)
odd = [a for a in list if a%2!=0]
print("Odd numbers in the list are: ",odd)
