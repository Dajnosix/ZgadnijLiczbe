from random import randint

random = randint(1,25)
answer = -1
times = 0

print("Mini-gra Zgadnij Liczbę by Dajnosix" )
print("Gra inspirowana kursami na Youtube.")
print("Podaj liczbę w przedziale od: 1-25!")

while answer != random:
    times += 1
    try:
        answer = int(input("Podaj liczbę: "))
        if answer > random:
            print("Wylosowana liczba jest mniejsza od tej napisanej przez ciebie!")
        elif answer < random:
            print("Wylosowana liczba jest większa od tej wpisanej przez ciebie!")
    except ValueError:
        print("Nie podałeś liczby, bądź jest ona nie prawidłowa")
        answer = -1

print(f"Gratulacje! Ogadłeś prawidłową liczbę za {times} razem.")