print("***INSTRUKCJA***")
print("poniedziałek = 1")
print("wtorek = 2")
print("środa = 3")
print("czwartek = 4")
print("piątek = 5")
print("sobota = 6")
print("niedziela = 7")
print("***************")

print()

dzien_oddania = int(input(f"Podaj dzień tygodnia, w który oddałeś buty do szewca: "))

if dzien_oddania == 1:
    print("Dzień oddania butów do szewca to poniedziałek")
elif dzien_oddania == 2:
    print("Dzień oddania butów do szewca to wtorek")
elif dzien_oddania == 3:
    print("Dzień oddania butów do szewca to środa")
elif dzien_oddania == 4:
    print("Dzień oddania butów do szewca to czwartek")
elif dzien_oddania == 5:
    print("Dzień oddania butów do szewca to piątek")
elif dzien_oddania == 6:
    print("Dzień oddania butów do szewca to sobota")
elif dzien_oddania == 7:
    print("Dzień oddania butów do szewca to niedziela")
else:
    print("Podałeś nieprawidłową wartość")

print()

czas_naprawy = float(input(f"Podaj czas naprawy mierzony w dniach: "))
dzien_odbioru = (dzien_oddania + czas_naprawy) % 7

if dzien_odbioru == 1:
    print("Dzień odbioru butów od szewca to poniedziałek")
elif dzien_odbioru == 2:
    print("Dzień odbioru butów od szewca to wtorek")
elif dzien_odbioru == 3:
    print("Dzień odbioru butów od szewca to środa")
elif dzien_odbioru == 4:
    print("Dzień odbioru butów od szewca to czwartek")
elif dzien_odbioru == 5:
    print("Dzień odbioru butów od szewca to piątek")
elif dzien_odbioru == 6:
    print("Dzień odbioru butów od szewca to sobota")
elif dzien_odbioru == 7:
    print("Dzień odbioru butów od szewca to niedziela")
