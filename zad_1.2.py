print("***INSTRUKCJA***")
print("poniedziałek = 1")
print("wtorek = 2")
print("środa = 3")
print("czwartek = 4")
print("piątek = 5")
print("sobota = 6")
print("niedziela = 7")

dzien_oddania = int(input(f"Podaj dzień tygodnia, w który oddałeś buty do szewca: "))

print()

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

czas_naprawy = float(input(f"Podaj czas naprawy mierzony w dniach 1-7: "))


