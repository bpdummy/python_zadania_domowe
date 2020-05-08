ziemniaki = float(input(f"Podaj cenę 1 kg zmieniaków: "))
print(f"Cena ziemniaków = " ,ziemniaki, "zł/kg")

koszt_5kg = ziemniaki * 5
print(f"Koszt 5 kg ziemniaków: ", koszt_5kg, "zł")

print()

ile_ziemniakow = float(input(f"Ile kg ziemniaków chcesz kupić: "))
koszt_ziemniakow = ziemniaki * ile_ziemniakow

print(f"Cena {ile_ziemniakow} kg ziemniaków = {koszt_ziemniakow:.2} zł")

print()

ziemniaki = float(input(f"Podaj cenę 1 kg zmieniaków: "))
ile_ziemniakow = float(input(f"Ile kg ziemniaków chcesz kupić: "))
koszt_ziemniakow = ziemniaki * ile_ziemniakow

print()

banany = float(input(f"Podaj cenę 1 kg bananów: "))
ile_bananow = float(input(f"Ile kg bananów chcesz kupić: "))
koszt_bananow = banany * ile_bananow

print()

suma = koszt_ziemniakow + banany * ile_bananow
print(f"Za ziemniaki i banany zapłacisz: ", suma, "zł.")

if koszt_ziemniakow > koszt_bananow:
    print("Za ziemniaki trzeba zapłacić więcej niż za banany.")
elif koszt_ziemniakow < koszt_bananow:
    print("Za banany trzeba zapłacić więcej niż za ziemniaki.")
elif koszt_bananow == koszt_ziemniakow:
    print("Banany kosztują tyle samo co ziemniaki.")