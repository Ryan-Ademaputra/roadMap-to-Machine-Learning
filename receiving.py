
# Program mengecek umur
birth = int(input('birth: '))
age = 2026 - birth

print(age)


# Program pesanan part II

## kamus lokal
menu = {
    'burger' : 10000,
    'mie ayam' : 20000,
    'kentang' : 300000
}

payment = {
        'Qr',
        'Debit',
        'Transfer',
        'cash'
}

## conversation
name = str(input('Whats is your name? '))
print("Welcome " + name)

## algoritma I
ask = str(input("What can i help you? "))
if ask == ("Menu"): 
    print(menu)
else:
    print("We don't have that")

## algortima II
checkout = str(input('i want to buy: '))
if checkout in (menu):
    print(f"this is the price: Rp{menu[checkout]}")
else :
    print("sorry we dont have that")

## algoritma III
print("what will you choose for this payment? ")
choose = str(input('i will choose: '))
if choose in (payment):
    print("this is your payment")
else:
    print ("sorry we dont have that payment..")







