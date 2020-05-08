wzrost = float(input(f"Podaj swój wzrost w cm: "))
waga = float(input(f"Podaj swoją wagę w kg: "))

wzrost_m = wzrost / 100

bmi = waga / wzrost_m ** 2

print()

print(f"Twoje BMI wynosi: {bmi:.2f}")

print()

if bmi < 15.99:
    print("Jesteś wygłodzony i masz znaczną niedowagę. Powinieneś jeść jeszcze więcej.")
elif 16 <= bmi <= 16.99:
    print("Jesteś wychudzony i masz niedowagę. Powinieneś jeść więcej.")
elif 17 <= bmi <= 18.49:
    print("Masz niedowagę. Zjedz troszkę.")
elif 18.5 <= bmi <= 24.99:
    print("Twoja waga jest optymalna.")
elif 25 <= bmi <= 29.99:
    print("Masz lekką nadwagę. Ogranicz jedzenie kalorycznych posiłków.")
elif 30 <= bmi <= 34.99:
    print("Masz otyłość I stopnia. Ogranicz ilość zjadanych pokarmów, zacznij się odchudzać.")
elif 35 <= bmi <= 39.99:
    print("Masz otyłość II stopnia. To może zagrażać Twojemu życiu i zdrowiu. Dieta w Twoim przypadku jest konieczna.")
elif bmi >= 40:
    print("Masz otyłość III. Jeśli nie zaczniesz się ograniczać i nie przejdziesz na dietę, niedługo umrzesz.")
