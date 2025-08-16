time=int(input("Enter time in hours: "))
time = float(input("Enter time in hours: "))
if time < 6:
    print("you can easily go to institution")
elif time < 7:
    print("you can go but bit late to institution")
elif time < 7.5:
    print("you can take leave")
elif time == 8:
    print("your class is from online")
elif time > 8:
    print("you should not go to institution")
