print(10>20)
print(10<20)
print(10>=20)
print(10<=20)
print(10==20)
print(10!=20)

#string concatenation
name='John'
name1='Doe'
full= name,name1
print(full)

#string repetition
print(name * 3)

#conditional statement 
    # a block of code will be executed until some condition is satisfied
    # 1.if statement
    # 2.if else statement
    # 3.else if statement
    # 4.nested if statement
    # 5.switch statement

# climate = "raining"
# if climate == "raining":
#     print("Take an umbrella")
# else:
#     print("No need for an umbrella")

# trip = input("Long Drive : ")
# if trip == "yes":
#     print("Enjoy your trip!")
# else:
#     print("Stay home and relax")

#else if

# car = input("tell your favorite car: ")
# if car == "BMW":
#     print("You like BMW car ")
# elif car == "Suzuki":
#     print("You like Suzuki car ")
# elif car == "Toyota":
#     print("You like Toyota car ")
# elif car == "TATA":
#     print("You like TATA car ")
# elif car == "Mahindra":
#     print("You like Mahindra car ")
# elif car == "range rover":
#     print("You like range rover car ")
# elif car == "Jaguar":
#     print("You like Jaguar car ")


# house = "not-villa"
# if house == "villa":
#     print("You live in a villa")
# else:
#     print("You live in a apartment")

cost=input("Enter the cost of the item: ")
if int (cost) < 1000 :
    print("You can buy the item")
else:
    print("You cannot buy the item")   

bill = int(input("Enter the bill amount: "))
if bill > 1000:
    discount = bill * 0.1
    finalprice = bill - discount
    print(finalprice)
elif bill > 2000:
    discount = bill * 0.2
    finalprice = bill - discount
    print(finalprice)
elif bill > 3000:
    discount = bill * 0.3
    finalprice = bill - discount
    print(finalprice)
elif bill > 4000:
    discount = bill * 0.4
    finalprice = bill - discount
    print(finalprice)
elif bill > 999:
    print("No discount will be given")