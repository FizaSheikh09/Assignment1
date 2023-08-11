first = int(input("Enter the number you want : "))
print("You entered number : " +str(first))
if 0 <= first <= 10:
    print("Low range")
elif 11 <= first <= 50:
    print("medium range")
elif 51 <= first <= 100:
    print("high range")
else :
    print("Out Of Range")

