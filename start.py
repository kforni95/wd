print ("Hello world")

imie="Ala"
print(type(imie))
imie=str("Ala")
print(type(imie))
imie=imie.lower()
print(imie)

#typy liczbowe
liczba = 1
liczbaf = 4.5
print(type(liczba))
print(type(liczbaf))
print(f"{0.1:.17f}") #od wersji 3.6

#decimal lub zaokraglanie

liczba="100"
print(int(liczba))
print(int(liczba, 2))

print("Ala" + " ma " +str(5) + " kotow"  )
print("Ala ma {0}{1}{2} kotow".format(5,3,4) )
print(f"Ala ma {0}{1}{2} kotow")
kotow=123
print(f"Ala ma {kotow} kotow")
print(f"Ala ma {kotow:.4f} kotow")