from random import randint

losuj = randint(1,25)
odpowiedz = -1
razy = 0
print("Mini-gra Zgadnij Liczbę by Dajnosix" )
print("Gra inspirowana kursami na Youtube.")
print("Podaj w przedziale od 1 - 25!")

while odpowiedz != losuj:
    razy += 1
    odpowiedz = int(input("Podaj liczbę: "))
    if odpowiedz > losuj:
        print("Wylosowana liczba jest mniejsza od wpisanej przez ciebie!")
    elif odpowiedz < losuj:
        print("Wylosowana liczba jest większa od wpisanej przez ciebie!")
print("Gratulacje! Ogadłeś prawidłową liczbę za", razy, "razem.")