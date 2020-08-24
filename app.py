numbers = input("Entrer 10 numbers" for i in range(10))
odds = [ x for x in numbers if x % 2 == 1 ]
if odds:
    print(max(odds))
else:
    print("all numbers are even")
