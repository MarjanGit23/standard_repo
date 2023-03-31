# 4  Ransom note

# Solution 1                               --> aus der Angabe übernommen
def can_construct(target, source):
    """Determines if string `target` can be constructed using characters from string `source`."""
    source = list(source)    # Der string source wird in eine Liste umgewandelt, source=magazine
    for el in target:        # Das target wird Zeichen für Zeichen el durchgelaufen, target=ransom_note
        try: #er probiert obs überhaupt in source vorkommt, sonstmacht er except ValueError
            i = source.index(el)  # In i wird der Index gespeichert, wo in Source, dasselbe Zeichen wie el steht, also Position
            source[i] = None # Dort wo das Zeichen el steht in der Liste source, wird es hiermit auf None gesetzt, was dem löschen entspricht
        except ValueError:  # the `index` method raises ValueError if item is absent
            return False #wenn das Zeichen el in Source garnicht enthalten ist liefert die Fkt false zurück
    return True #er liefert True, wenn er jedes Zeichen in ransom_note also target gefunden in der ausreichenden Anzahl



# Solution 2
'''For each letter in magazine:
    Count how often it occurred (save the counts in a count table: letter -> count)
For each letter in ransom_note:
    If the letter occurs in the count table, reduce its count by 1
    If it doesn't occur in the count table, or its count is 0, return "false" and stop
Return "true" and stop'''
# Wir brauchen für eine ein count_table ist eine Zähltabelle(in der zu jedem in Magazine=source vorkommenden Buchstaben, die Anzahl seines Vorkommens 
# gespeichert wird)  

def can_construct2(target, source):

    count_table = dict()                 # count_table ein leeres dictionary zuweisen, dt: Wir legen ein Dictionary an, damit
    # weiß der PC, dass die Variable count_table ein Dictionary zugewiesen ist, was ein abstarct Data Typ ist

    for el in source:                    # source Zeichen für Zeichen durchgehen
        if el in count_table:            # Kommt das Zeichen bereits als key im dictionary vor,
            count_table[el] += 1         # wird der value um 1 erhöht.
        else:
            count_table[el] = 1          # Wenn nicht, wird ein neues Element mit dem Zeichen als key und 1 als value in das dict aufgenommen.
                                         # Ergebnis: das dictionary count_table enthält nun zu jedem Buchstaben, der in source vorkommt, die Angabe, wie oft er vorkommt.
    for el in target:                    # target Zeichen für Zeichen durchgehen
        if el in count_table:            # Wenn es in der count_table einen key gibt, der dem Zeichen entspricht,
            if count_table[el] > 0:      # wird geprüft, ob der Zähler größer 0 ist
                count_table[el] -= 1     # Wenn ja, Zähler um 1 reduzieren.
            else:                        # Sonst abbrechen (False retournieren), weil das Zeichen im source nicht in ausreichender Anzahl vorkommt
                return False
        else:                            # Gibt es erst gar keinen key, der dem aktuellen Zeichen entspricht, kann gleich abgebrochen werden.
            return False
    return True                          # Wenn die for-Schleife nicht vorzeitig abgebrochen wurde, kann das target mit Zeichen aus source gebildet werden, also True retournieren.





ransom_note = "aac"
magazine = "abab"
#bei ihm angabe in der angabe steht ausführen mit can_ construct(ransom_note, magazine), dabei 
# gibts aber keine Ausgabe, weil der Return Wert nicht geprintet wird
# Eine Möglichkeit ist so:
#if(can_construct(ransom_note, magazine)):
 #   print("Ransom note can be constructed by using the letters from magazine.")
#else:
 #   print("Ransom note can NOT be constructed by using the letters from magazine.")

# oder man printed einfach den Return-Wert
print(can_construct(ransom_note, magazine))

#if(can_construct2(ransom_note, magazine)):
 #   print("Ransom note can be constructed by using the letters from magazine.")
#else:
 #   print("Ransom note can NOT be constructed by using the letters from magazine.")

# Timing comparison
'''import random
import string

lengths = [10, 100, 1000, 10000, 100000, int(1e6)]
for length in lengths:
    # We'll simply use random data of given length
    ransom_note = [random.choice(string.ascii_letters) for el in range(length)]
    magazine = [random.choice(string.ascii_letters) for el in range(length)]
    print(f"{len(ransom_note)=}, {len(magazine)=}")
    %timeit can_construct(ransom_note, magazine)
    %timeit can_construct2(ransom_note, magazine)'''