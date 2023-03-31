
# 7  Counting even numbers
'''

 1. Write a program that prints the even numbers between 1 and (not including) 10. In the end, it should output a message
    "We have x even numbers", where x corresponds to the number of even numbers, and a message "The product of these number
    is y", where y corresponds to the product of these numbers. You may find this video useful. (It uses the modern f-strings
    formatting. As an exercise, replace it using the old-style string formatting.)
 2. If you executed the code within Ipython (e.g. in a Jupyter notebook), execute it as a stand-alone script.

'''


count = 0     # Es wird eine int-Variable als Zähler angelegt
product = 1   # weitere int-Variable für das Produkt aller geraden Zahlen wird angelegt

for x in range(1, 10):   # range liefert hier die Werte von 1 bis 9, die mit x durchgegangen werden
    if x % 2 == 0:       # Wenn x gerade Zahl (durch 2 ohne Rest teilbar),
        print(x)          # wird x ausgegeben,
        count += 1              # der Zähler der geraden Zahlen um 1 erhöht
        product = product * x   # und die bisher im product gespeichert Zahl mit der aktuellen geraden Zahl multipliziert und wieder
                                # in product gespeichert

print("We have %d even numbers" % (count))       # Die Zahl der geraden Zahlen ausgeben

print("The product of these numbers is %d" % (product))   # Das Produkt ausgeben