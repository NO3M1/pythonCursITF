
'''
Calculator impozit masina
In functie de cm cubi ai masinii, dorim sa afisam impozitul
    - cc < 0 => invalid
    - cc < 1000 => 70.50 lei
    - cc < 2400 => 159.90 lei
    - pentru restul valorilor => 900 lei
Afisati impozitul.


'''

# ce variabile avem nevoie? ce tip de date?

cc = 150
#cc = int(input('cc este:'))
impozit = 0

# ce structura avem nevoie ca sa calculam impozitul?
if (cc < 0):
    print("valoare cc invalida")
elif (cc < 1000):
    impozit = 70.50
elif (cc < 2400):
    impozit = 159.90
else:
    impozit = 900


# afisat impozitul

print(f'Impozitul dvs este {impozit} lei')