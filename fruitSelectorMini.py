print("Welcome to the :) Boring Fruit Selector.") 
like_fruit = input("Hallo, what is your name? ")
    print("Hallo,", like_fruit, "which fruit do you prefer? ")
box_fruits = {1:"Apple", 2:"Orange",
3:"Banana"}
for num in range(1, 4):
    print(num, box_fruits[num])
name = input("Which one is Your favourite? ")
if name == "1":
    print("Nice! Healthy choice")
elif name == "2":
    print("Sweet, Excellent Choice!")
else:
    print("Lovely, njoy the fruit")


    
