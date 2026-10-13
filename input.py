name = input("What is your name? ")
print("Hai Mr. " + name)

label = "== Menu == "
namaMenu = "Burger || Rice || Potato \n"
price = "Rp. 10.000 || Rp. 5000 || Rp. 20000"


menu = namaMenu + price



# Program menu
ask = input("What you need right now? ")
if ask == "Menu":
    print("okay, i can help you")
    print(label)
    print(menu)
    print("what you want sir? ")
    input()
    print("thank you " + name)
else:
    print("get out!!")