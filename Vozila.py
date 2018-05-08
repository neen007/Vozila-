# -*- coding: utf-8 -*-

class Vozila:
    def __init__(self, marka, model, kilometri, servis):
        self.marka = marka
        self.model = model
        self.kilometri = kilometri
        self.servis = servis

    def promijeni_kilometri (self, novi_kilometri):
        self.kilometri = novi_kilometri

    def promijeni_servis (self, novi_datum):
        self.servis = novi_datum


def main():
    print "_______________________________________________"
    print ("Dobrodošli u program za evidenciju vozila !!")
    print "_______________________________________________"

    vozila=[]

    while True:
        print ""
        print "Odaberi jednu opciju:"
        print "1) Ispiši sva vozila koja posjeduje firma."
        print "2) Dodaj novo vozilo."
        print "3) Dodaj nove kilometre."
        print "4) Dodaj novi datum servisa."
        print "5) KRAJ."

        choice = raw_input("Odaberi jednu opciju? (1,2,3,4,5)")
        print ""

        if choice.lower() == "1":
            sva_vozila(vozila)
        elif choice.lower() == "2":
            dodaj_novo_vozilo(vozila)
        elif choice.lower() == "3":
            dodaj_novi_kilometri(vozila)
        elif choice.lower() == "4":
            dodaj_novi_servis(vozila)
        elif choice.lower() == "5":
            print "_____________________________________________________________________"
            print "Hvala Vam što ste koristili program za vozila. Želim Vam ugodan dan!!"
            print "_____________________________________________________________________"
            break
        else:
            print "Žao mi je, ali ne razumijem Vaš izbor. Odaberite jedan broj između 1, 2, 3, 4, 5. "


def sva_vozila(vozila):
    if vozila == []:
        print "Niste unijeli još ni jedno vozilo u bazu !!! "
        print "Molimo Vas da odaberete opciju da unesete novo vozilo."
    else:
        for index, vozilo in enumerate(vozila):
            print "%s) %s %s sa %s km prošao do sada. Prošli servis je bio: %s" % (index + 1, vozilo.marka, vozilo.model,vozilo.kilometri, vozilo.servis)


def stvori_vozilo(marka, model, kilometri, servis, vozila):
    novo_vozilo = Vozila(marka=marka, model=model, kilometri=kilometri, servis=servis)
    vozila.append(novo_vozilo)
    return


def dodaj_novo_vozilo(vozila):
    marka = raw_input("Unesite marku vozila:")
    model = raw_input("Unesite model vozila:")
    kilometri = raw_input("Unesite kilometre za vozilo:")
    servis = raw_input("Unesite datum servisa:")

    rezultat = stvori_vozilo(marka, model, kilometri, servis, vozila)

    if rezultat:
        print "."
    else:
        print "Ispravno si unio novo vozilo %s %s!" % (marka, model)

def odaberi_vozilo(vozila):
    print "Odaberite broj kraj vozila koje želite promijeniti."
    print ""
    sva_vozila(vozila)
    print ""
    odabir = raw_input("Koje vozilo želite odabrati? ")
    return vozila[int(odabir) - 1]

def dodaj_novi_kilometri(vozila):
    oda_vozilo = odaberi_vozilo(vozila)

    print "Odabrano vozilo: %s %s sa %s km." % (oda_vozilo.marka, oda_vozilo.model, oda_vozilo.kilometri)
    print ""
    novi_kilometri = raw_input("Koliko kilometara želite dodati postojećem vozilu?")
    print ""

    oda_vozilo.promijeni_kilometri(novi_kilometri)
    print "Novi kilometri za vozilo %s %s su sad: %s." % (oda_vozilo.marka, oda_vozilo.model, oda_vozilo.kilometri)

def dodaj_novi_servis(vozila):

    odr_vozilo = odaberi_vozilo(vozila)

    print "Vozilo odabrano: %s %s sa datumom servisa: %s." % (odr_vozilo.marka, odr_vozilo.model, odr_vozilo.servis)
    print ""
    novi_servis = raw_input("Koji je novi datum servisa za ovo vozilo? (DD.MM.GGGG) ")
    print ""
    odr_vozilo.promijeni_servis(novi_datum=novi_servis)
    print "Dodan novi datum servisa!"


if __name__ == "__main__":
    main()






