ziemniaki = float(input(f"Podaj cenę 1 kg zmieniaków: "))
print(f"Cena ziemniaków = {ziemniaki:.2} zł/kg")

koszt_5kg = ziemniaki * 5
print(f"Koszt 5 kg ziemniaków: ", koszt_5kg, "zł")

print()

ile_ziemniakow = float(input(f"Ile kg ziemniaków chcesz kupić: "))
cena_ziemniaki = ziemniaki * ile_ziemniakow

print(f"Cena {ile_ziemniakow} kg ziemniaków = {cena_ziemniaki:.2} zł")

print()

ziemniaki = float(input(f"Podaj cenę 1 kg zmieniaków: "))
ile_ziemniakow = float(input(f"Ile kg ziemniaków chcesz kupić: "))
wynik_ziemniaki = ziemniaki * ile_ziemniakow

print()

banany = float(input(f"Podaj cenę 1 kg bananów: "))
ile_bananów = float(input(f"Ile kg bananów chcesz kupić: "))
cena_bananow = banany * ile_bananów

print()

suma = wynik_ziemniaki + banany * ile_bananów
print(f"Za ziemniaki i banany zapłacisz: ", suma, "zł.")

if wynik_ziemniaki > cena_bananow:
    print("Za ziemniaki trzeba zapłacić więcej niż za banany.")
elif wynik_ziemniaki < cena_bananow:
    print("Za banany trzeba zapłacić więcej niż za ziemniaki.")
else:
    cena_bananow == wynik_ziemniaki
    print("Banany kosztują tyle samo co ziemniaki.")