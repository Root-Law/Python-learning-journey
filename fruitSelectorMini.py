
name = input("Would you like some fruit? ")

box_fruits = {1:"Apple", 2:"Orange",
3:"Banana"}

for num in range(1, 4):
    print(num, box_fruits[num])
    
name = input("Which one is Your favourite? ")


if name == "1":
    print("Nice")
elif name == "2":
    print("Sweet, is a Excellent Choices!")
else:
    print("Lovely")


    