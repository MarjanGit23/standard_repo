'''You have this list:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

   1. Write code thats output all list items smaller than 9.
   2. After you have written the code, design some test cases to show that it works as expected.
   3. Instead of printing the items, create a new list and append the items from the old list that match the condition. In the end, print the list.
   4. Ask the user for input, and output only the list items smaller than the given value.
   5. Save the last version (the one which interacts with the user) as a Python script and execute it from the command line.'''


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # Das ist die vorgegebene Liste
b = []                                      # Es wird eine leere list angelegt, in der dann jene Elemente aus a kommen, die kleiner sind,
                                            # als der "Grenzwert"
val = int(input("Grenzwert eingeben:"))     # Der Benutzer soll den Grenzwert eingeben, der von input gelieferte String wird 
                                            #  der Funktion int() übergeben, die einen integer-Wert retourniert. Dieser wird in der
                                            # Variable val gespeichert

for i in a: # Diese for-Schleife geht alle Elemente der list a durch
    if i < val:  # Es wird gefragt, ob das aktuelle Element < als a (der Grenzwert) ist
        b.append(i) # Wenn ja, wird der Wert des Elements der list b angehängt

for i in b: # Diese for-Schleife geht die jetzt befüllte list b durch
    print(i)  # und gibt alle Werte aus