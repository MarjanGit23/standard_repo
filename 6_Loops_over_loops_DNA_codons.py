# Exercise sheet 3, 30.09.22
# 6  Loops over loops: DNA codons
'''
    1. Output all 64 DNA codons using nested loops. (Hint: Remember that loops can iterate not only over ranges,
    but also over strings. In the beginning, define a variable with valid DNA characters: DNA = "ACGT", and use it with the for loops.)
    2. You should be able to explain how old-style string formatting (which uses the modulo operator) works, based on some examples.
'''

# 1.:
# Es sollen alle 64 DNA codons ausgegeben werden, was mit verschachtelten Schleifen umgesetzt wird.
# Die 64 codons sint drei Zeichen lange Strings, die alle Möglichkeiten der Kombination der Zeichen A, G, C und T enthalten
codonnr = 1  # int-Variable, die für die Nummerierung der codons verwendet wird
DNA = "AGCT" # Hier definieren wir einen String, in dem alle Zeichen enthalten sind, die wir kombinieren wollen

for x in DNA:        # drei verschachtelte for-Schleifen laufen jeweils den string DNA (also die Zeichenfolge "AGCT" durch)
    for y in DNA:
        for z in DNA:
            print("%d: %s%s%s" % (codonnr, x, y, z))   #old style       bei jedem Durchlauf der innersten Schleife (z) wird die laufende
                                                                        # Nr (codonnr) und die Zeichenkombination (x y z) ausgegeben
            #print(str(codonnr) + ": " + x + y +z)     #new style
            codonnr += 1