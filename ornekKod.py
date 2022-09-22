import random
import time

AsilDeste = {"Sinek As": 1, "Sinek 2": 2, "Sinek 3": 3, "Sinek 4": 4, "Sinek 5": 5, "Sinek 6": 6, "Sinek 7": 7,
             "Sinek 8": 8, "Sinek 9": 9, "Sinek 10": 10, "Sinek J": 20, "Sinek Q": 11, "Sinek K": 12, "Karo As": 1,
             "Karo 2": 2, "Karo 3": 3, "Karo 4": 4, "Karo 5": 5, "Karo 6": 6, "Karo 7": 7, "Karo 8": 8, "Karo 9": 9,
             "Karo 10": 10, "Karo J": 20, "Karo Q": 11, "Karo K": 12, "Kupa As": 1, "Kupa 2": 2, "Kupa 3": 3,
             "Kupa 4": 4, "Kupa 5": 5, "Kupa 6": 6, "Kupa 7": 7, "Kupa 8": 8, "Kupa 9": 9, "Kupa 10": 10, "Kupa J": 20,
             "Kupa Q": 11, "Kupa K": 12, "Maca As": 1, "Maca 2": 2, "Maca 3": 3, "Maca 4": 4, "Maca 5": 5, "Maca 6": 6,
             "Maca 7": 7, "Maca 8": 8, "Maca 9": 9, "Maca 10": 10, "Maca J": 20, "Maca Q": 11, "Maca K": 12}
# AsilDeste.remove("Maca 3")
TemelDeste = ["Sinek As", "Sinek 2", "Sinek 3", "Sinek 4", "Sinek 5", "Sinek 6", "Sinek 7", "Sinek 8", "Sinek 9",
              "Sinek 10", "Sinek J", "Sinek Q", "Sinek K", "Karo As", "Karo 2", "Karo 3", "Karo 4", "Karo 5", "Karo 6",
              "Karo 7", "Karo 8", "Karo 9", "Karo 10", "Karo J", "Karo Q", "Karo K", "Kupa As", "Kupa 2", "Kupa 3",
              "Kupa 4", "Kupa 5", "Kupa 6", "Kupa 7", "Kupa 8", "Kupa 9", "Kupa 10", "Kupa J", "Kupa Q", "Kupa K",
              "Maca As", "Maca 2", "Maca 3", "Maca 4", "Maca 5", "Maca 6", "Maca 7", "Maca 8", "Maca 9", "Maca 10",
              "Maca J", "Maca Q", "Maca K"]
Eksilecek = ["Sinek As", "Sinek 2", "Sinek 3", "Sinek 4", "Sinek 5", "Sinek 6", "Sinek 7", "Sinek 8", "Sinek 9",
             "Sinek 10", "Sinek J", "Sinek Q", "Sinek K", "Karo As", "Karo 2", "Karo 3", "Karo 4", "Karo 5", "Karo 6",
             "Karo 7", "Karo 8", "Karo 9", "Karo 10", "Karo J", "Karo Q", "Karo K", "Kupa As", "Kupa 2", "Kupa 3",
             "Kupa 4", "Kupa 5", "Kupa 6", "Kupa 7", "Kupa 8", "Kupa 9", "Kupa 10", "Kupa J", "Kupa Q", "Kupa K",
             "Maca As", "Maca 2", "Maca 3", "Maca 4", "Maca 5", "Maca 6", "Maca 7", "Maca 8", "Maca 9", "Maca 10",
             "Maca J", "Maca Q", "Maca K"]

BenimDeste = []
BilginDestesi = []
Orta = []

BenimToplananlar = []
BilginToplananlar = []

# dictionary deger verme
# sozluk = {'Sinek 1':1,'Sinek 2':2}
# a = "Sinek 1"
# if(sozluk[a]== 1):
#    print("ahdsf")

# BenimDeste = ["Sinek 3"]
# if(AsilDeste[BenimDeste[0]]==3):
#    print("abcd")
Giris = """
Welcome, You Mortal!
Wanna Challenge Me In Pishti?

LETS START THEN!!!
"""
print(Giris)
ks = 52
for i in range(0, 4):
    s = random.randint(0, ks - i - 1)
    Orta.append(Eksilecek[s])
    Eksilecek.remove(Eksilecek[s])

ks = 48

while len(Eksilecek) != 0:
    print("ORTADA: {}\n".format(Orta[len(Orta) - 1]))
    for i in range(0, 4):
        s = random.randint(0, ks)
        BenimDeste.append(Eksilecek[s])
        Eksilecek.remove(Eksilecek[s])
        ks -= 1
    for i in range(0, 4):
        s = random.randint(0, ks - 1)
        BilginDestesi.append(Eksilecek[s])
        Eksilecek.remove(Eksilecek[s])
        ks -= 1
    n = 4
    m = 4
    while True:
        print("DESTEN: ", end="")
        for i in range(0, n):
            print(BenimDeste[i], end="- ")
        n -= 1
        print("\n")
        for i in range(0, 1):
            secim = input("Hangi karti oynayacaksin? ")
            if (secim == "Sinek J" or secim == "Maca J" or secim == "Karo J" or secim == "Kupa J"):
                for k in range(0, len(Orta)):
                    BenimToplananlar.append(Orta[k])
                Orta.clear()
                Orta.append("/")
                BenimDeste.remove(secim)
            elif (Orta[Orta[len(Orta) - 1]] == '/'):
                Orta.append(secim)
            elif (BenimDeste.__contains__(secim)):
                if (AsilDeste[Orta[len(Orta) - 1]] == AsilDeste[secim]):

                    for k in range(0, len(Orta)):
                        BenimToplananlar.append(Orta[k])
                    Orta.clear()
                    Orta.append("/")
                    BenimDeste.remove(secim)
                else:
                    Orta.append(secim)
                    BenimDeste.remove(secim)
            else:
                continue

        print("\nORTADA: {}\n".format(Orta[len(Orta) - 1]))
        time.sleep(1)
        # bilgisayarin hamlesi

        #        for a in range(0,len(BilginDestesi)):
        #           kard = BilginDestesi[a]
        #           if(AsilDeste[Orta[len(Orta)-1]] == AsilDeste[kard]):
        #        kosul = BilginDestesi.__contains__("Sinek J") or BilginDestesi.__contains__("Maca J") or BilginDestesi.__contains__("Kupa J") or BilginDestesi.__contains__("Karo J")
        if (len(Orta) >= 5):
            if (BilginDestesi.__contains__("Sinek J")):
                Orta.append("Sinek J")
                #                for k in range(0,len(Orta)):
                l = 0
                while l < len(Orta):
                    BilginToplananlar.append(Orta[l])
                    Orta.clear()
                    Orta.append("/")
                    BilginDestesi.remove("Sinek J")
                    l += 1
            elif (BilginDestesi.__contains__("Maca J")):
                Orta.append("Maca J")
                l = 0
                while l < len(Orta):
                    BilginToplananlar.append(Orta[l])
                    Orta.clear()
                    Orta.append("/")
                    BilginDestesi.remove("Maca J")
                    l += 1
            elif (BilginDestesi.__contains__("Karo J")):
                Orta.append("Karo J")
                l = 0
                while l < len(Orta):
                    BilginToplananlar.append(Orta[l])
                    Orta.clear()
                    Orta.append("/")
                    BilginDestesi.remove("Karo J")
                    l += 1
            elif (BilginDestesi.__contains__("Kupa J")):
                Orta.append("Kupa J")
                l = 0
                while l < len(Orta):
                    BilginToplananlar.append(Orta[l])
                    Orta.clear()
                    Orta.append("/")
                    BilginDestesi.remove("Kupa J")
                    l += 1
            else:
                l = 0
                while l < m:
                    if (AsilDeste[BilginDestesi[l]] == AsilDeste[Orta[len(Orta) - 1]]):
                        print("Bilgisayar oynadi: {}".format(BilginDestesi[l]))
                        l2 = 0
                        while l2 < len(Orta):
                            BilginToplananlar.append(Orta[l2])
                            l2 += 1
                        Orta.clear()
                        Orta.append("/")
                        BilginDestesi.remove(BilginDestesi[l])
                        break
                    else:
                        if (l == m - 1):
                            Orta.append(BilginDestesi[l])
                            BilginDestesi.remove(BilginDestesi[l])

                    l += 1


        # lenOrta <5
        else:
            l = 0
            while l < m:
                if (AsilDeste[BilginDestesi[l]] == AsilDeste[Orta[len(Orta) - 1]]):
                    print("Bilgisayar oynadi: {}".format(BilginDestesi[l]))
                    l2 = 0
                    while l2 < len(Orta):
                        BilginToplananlar.append(Orta[l2])
                        l2 += 1
                    Orta.clear()
                    Orta.append("/")
                    BilginDestesi.remove(BilginDestesi[m])
                    break
                else:
                    if (l == m - 1):
                        if (BilginDestesi[l] != "Sinek J" and BilginDestesi[l] != "Karo J" and BilginDestesi[
                            l] != "Kupa J" and BilginDestesi[l] != "Maca J"):
                            Orta.append(BilginDestesi[l])
                            BilginDestesi.remove(BilginDestesi[l])
                        else:
                            l -= 1
                            if (BilginDestesi[l] != "Sinek J" and BilginDestesi[l] != "Karo J" and BilginDestesi[
                                l] != "Kupa J" and BilginDestesi[l] != "Maca J"):
                                Orta.append(BilginDestesi[l])
                                BilginDestesi.remove(BilginDestesi[l])
                            else:
                                l -= 1
                                if (BilginDestesi[l] != "Sinek J" and BilginDestesi[l] != "Karo J" and BilginDestesi[
                                    l] != "Kupa J" and BilginDestesi[l] != "Maca J"):
                                    Orta.append(BilginDestesi[l])
                                    BilginDestesi.remove(BilginDestesi[l])
                                break

                l += 1
        time.sleep(1)
        print("\nORTADA: {}\n".format(Orta[len(Orta) - 1]))

        m -= 1

        if (m == 0 and n == 0):
            break

