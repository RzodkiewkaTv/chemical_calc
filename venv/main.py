import os
uwaga = input("UWAGA! PROGRAM W NIEKTÓRYCH TERMINALACH MOŻE POSIADAĆ DEFEKTY W POSTACI ZNAKÓW OZNACZAJĄCYCH KOLOR"
              "\n PROSZĘ OTWÓRZ PROGRAM W WERSJI BEZ KOLORÓW JESLI WYSTĘPUJĄ U CIEBIE PROBLEMY!"
              "\n Kliknij dowolny przycisk aby zacząć")

os.system("cls")

print("1.Procent masowy")
programwyboru = float(input("Jakiego programu chcesz użyć?:"))


def procentmasowyprogram():
    print('\033[34m',"Procent masowy",'\033[32m',"by",'\033[31m' ,"Rz0Dev", "ver: 1.0",
          '\033[33m',"\nWitaj w moim programie kalkulującym Procent Masowy! \nPoznaj kilka zasad którę musisz znać aby ",
                     "używać poprawnie programu.", '\033[35m',"\n1.Zapisuj symbole pierwiastków jako duże litery! "
                                                              "\n(Tak na prawde nie musisz bo program jest idioto odporny)",
          "\n2.Masz do wyboru jako zdefiniowane pierwiastki:", "\nH -Wodór", "\nC -Węgiel", "\nO -Tlen",
          "\n3.Siur remika nie istnieje", "\n4.To co ci wyjdzie przepisz do zeszytu :)",
          '\033[33m', "\nTo tyle, miłego liczenia!")
    print('\033[39m')

    #uproszczenia
    #ZROB SPALANIE NIECALKOWITE I CALKOWITE MORDKO

    #zmienne
    wodor = float(1)
    wegiel = float(12)
    tlen = float(16)
    chele = str(input("Podaj symbol pierwiastka którego chcesz obliczyć: "))
    chelehowm = float(input("Podaj ile razy twój pierwiastek występuje w twoim związku:"))
    allmass = float(input("Podaj masę całego związku: "))

    def chomass():

        if chele == "C" or chele == "c":
            cmassfirst = wegiel
            cmass = cmassfirst * chelehowm
        elif chele == "H" or chele == "h":
            cmassfirst = wodor
            cmass = cmassfirst * chelehowm
        elif chele == "O" or chele == "o":
            cmassfirst = tlen
            cmass = cmassfirst * chelehowm
        else:
            jebaccie = str("Napotkano błąd!")
            return jebaccie

        return cmass

    def procentmasowy(chomass):

        error = "Błąd!"
        print('\033[36m')
        massprdev = chomass() / allmass
        massprend = round(massprdev * 100, 2)
        if massprend <= 100:
            return massprend
        else:
            return error

    print('\033[36m')

    print("%", chele, "=", chomass(), ":", allmass, "x 100 =",procentmasowy(chomass),"%")
    #print("Proces procentowania:")
    #print("%", element, "=", cmass, ":", allmass,"=",procentmasowy(),"%")

    #print("Twój procent masowy dla ", cmass,"u, wynosi: ", procentmasowy(), "%")





if programwyboru == 1:
    os.system("cls")
    procentmasowyprogram()
else:
    os.system("cls")
    print('\033[31m')
    print("Napotkano błąd!")

#print('\033[32m')
#print("TAK czy NIE?")
#jeszcze = str(input("Czy chcesz zacząć od nowa? :"))

#if jeszcze == "TAK" or "tak" or "Tak":
   # os.system("cls")
   # procentmasowyprogram()
#elif jeszcze == "NIE" or "nie" or "Nie":
  #  os.system("cls")
print('\033[39m')
endscript = input("Kliknij dowolny klawisz żeby zakończyć.")



