from kivy import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '700')


import random

from kivy.properties import StringProperty, BooleanProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

import variables

class Ana(Screen):

    theme = SoundLoader.load("audio/godfather.wav")
    theme.loop = True
    theme.volume = 0.12

    strt = SoundLoader.load("audio/strt.wav")

    ll = [SoundLoader.load("audio/1.wav"),SoundLoader.load("audio/2.wav"),SoundLoader.load("audio/3.wav"),SoundLoader.load("audio/4.wav"),SoundLoader.load("audio/5.wav"),SoundLoader.load("audio/6.wav"),SoundLoader.load("audio/7.wav"),SoundLoader.load("audio/8.wav"),SoundLoader.load("audio/9.wav"),SoundLoader.load("audio/10.wav"),SoundLoader.load("audio/11.wav"),SoundLoader.load("audio/12.wav"),SoundLoader.load("audio/13.wav"),SoundLoader.load("audio/14.wav"),SoundLoader.load("audio/15.wav"),SoundLoader.load("audio/16.wav"),SoundLoader.load("audio/17.wav")]

    def on_kv_post(self, *largs):
        self.themeSong()
        Clock.schedule_interval(self.randomBSgo,12)

    def themeSong(self):
        self.theme.play()

    def randomBSgo(self,dt):
        rn = random.randint(0, 16)
        self.ll[rn].play()

    def clean_vals(self):
        variables.Eksilecek = variables.TemelDeste.copy()
        variables.BenimPuan = 0
        variables.BilginPuan = 0
        variables.BenimToplananlar.clear()
        variables.OnunToplananlar.clear()
        variables.OnunDestesi.clear()
        variables.BenimDestem = ["","","",""]
        variables.MyTurn = True
        variables.DecidingMid = False
        variables.ForS = True



class EndWindow(Screen):
    fsval = BooleanProperty(True)
    yw = SoundLoader.load("audio/youwon.wav")
    nbdy = SoundLoader.load("audio/nobody.wav")
    iwon = SoundLoader.load("audio/iwon.wav")
    def on_enter(self, *args):
        #self.displayPoints()
        pass

    def clean(self):
        self.fsval = True
        self.ids.head.text = "oyun bitti"
        self.ids.herPoints.text = ""
        self.ids.myPoints.text = ""
        self.ids.herWords.text = ""
        self.ids.rec.source = "images/normaldark.png"

    def displayPoints(self):
        for i in variables.BenimToplananlar:
            if (i == "Karo_10"):
                variables.BenimPuan += 3
            if (i == "Sinek_2"):
                variables.BenimPuan += 2
            if (i == "Sinek_As" or i == "Maca_As" or i == "Karo_As" or i == "Kupa_As"):
                variables.BenimPuan += 1
            if (i == "Sinek_J" or i == "Maca_J" or i == "Karo_J" or i == "Kupa_J"):
                variables.BenimPuan += 1
        for i in variables.OnunToplananlar:
            if (i == "Karo_10"):
                variables.BilginPuan += 3
            if (i == "Sinek_2"):
                variables.BilginPuan += 2

            if (i == "Sinek_As" or i == "Maca_As" or i == "Karo_As" or i == "Kupa_As"):
                variables.BilginPuan += 1
            if (i == "Sinek_J" or i == "Maca_J" or i == "Karo_J" or i == "Kupa_J"):
                variables.BilginPuan += 1

        if (len(variables.OnunToplananlar) > len(variables.BenimToplananlar)):
            variables.BilginPuan += 3
        if (len(variables.BenimToplananlar) > len(variables.OnunToplananlar)):
            variables.BenimPuan += 3

        self.ids.myPoints.text = "Sen:\n\n{} Puan".format(variables.BenimPuan)
        self.ids.herPoints.text = "Bilgisayar:\n\n{} Puan".format(variables.BilginPuan)
        if variables.BenimPuan > variables.BilginPuan:
            self.ids.head.text = "KAZANDIN"
            self.ids.herWords.text = "Oh nooo... You won\nYou lucky bastard"
            self.ids.rec.source = "images/saddark.png"
            self.yw.play()
        elif variables.BenimPuan < variables.BilginPuan:
            self.ids.head.text = "KAYBETTIN"
            self.ids.herWords.text = "Easy peasy"
            self.ids.rec.source = "images/happydark.png"
            self.iwon.play()
        elif variables.BenimPuan == variables.BilginPuan:
            self.ids.head.text = "BERABERE"
            self.ids.herWords.text = "Neither of us has won, I guess"
            self.ids.rec.source = "images/normaldark.png"
            self.ids.rec.source = "images/normaldark.png"
            self.nbdy.play()

        #Bi degisken daha ekleyip menuye donerken sifirla, butun ekranlarda da bunu yap



class Game(Screen):
    Slot1Source = ""
    Slot2Source = ""
    Slot3Source = ""
    Slot4Source = ""

    MidSource = ""



    def ToTheEnd(self, dt):
        self.clean()
        self.ids.res.disabled = False
        App.get_running_app().root.current = "EndWindow"


    def on_kv_post(self, *largs): # Too early during initialization on_enter() dene
        print("Ne zamanannnn") #Heeeeeeeeee     OK bi baslangic tusu alzim ozmn
        self.ids.FirstImage.opacity = 0
        self.ids.SecondImage.opacity = 0
        self.ids.ThirdImage.opacity = 0
        self.ids.FourthImage.opacity = 0
        self.ids.MidImage.opacity = 0
        #self.distributeTheCards(0.6)
        #Clock.schedule_once(self.ToTheEnd, 0.5)


    def distributeTheCards(self, dt):
        print("EKSİLECEKLER: ")
        print(variables.Eksilecek)
        if variables.Eksilecek != 0:
            if variables.DecidingMid == False:
                for i in range(0, 4):
                    rn = random.randint(0, len(variables.Eksilecek)-1)
                    variables.Orta.append(variables.Eksilecek[rn])
                    variables.Eksilecek.remove(variables.Eksilecek[rn])
                variables.DecidingMid = True


            for i in range(0,4): #Onun Kartlari
                rn = random.randint(0,len(variables.Eksilecek)-1)
                variables.OnunDestesi.append(variables.Eksilecek[rn])
                variables.Eksilecek.remove(variables.Eksilecek[rn])

            for i in range(0,4): #Benim Kartlarim
                rn = random.randint(0, len(variables.Eksilecek)-1)
                variables.BenimDestem[i] = (variables.Eksilecek[rn])
                variables.Eksilecek.remove(variables.Eksilecek[rn])

            self.displayImages()

        else:
            print("Oyun Bitti") #Sonra dusun

    def displayImages(self):

        s1 = variables.BenimDestem[0]
        s2 = variables.BenimDestem[1]
        s3 = variables.BenimDestem[2]
        s4 = variables.BenimDestem[3]
        if(len(variables.Orta) != 0): m = variables.Orta[len(variables.Orta) - 1]
        else: m = ""

        if s1 != "":
            self.Slot1Source = "cardImages/{}.png".format(s1)
            self.ids.FirstImage.source = self.Slot1Source
            self.ids.FirstImage.opacity = 1
        else:
            self.ids.FirstImage.source = ""
            self.ids.FirstImage.reload()
            self.ids.FirstImage.opacity = 0

        if s2 != "":
            self.Slot2Source = "cardImages/{}.png".format(s2)
            self.ids.SecondImage.source = self.Slot2Source
            self.ids.SecondImage.opacity = 1
        else:
            self.ids.SecondImage.source = ""
            self.ids.SecondImage.reload()
            self.ids.SecondImage.opacity = 0

        if s3 != "":
            self.Slot3Source = "cardImages/{}.png".format(s3)
            self.ids.ThirdImage.source = self.Slot3Source
            self.ids.ThirdImage.opacity = 1
        else:
            self.ids.ThirdImage.source = ""
            self.ids.ThirdImage.reload()
            self.ids.ThirdImage.opacity = 0

        if s4 != "":
            self.Slot4Source = "cardImages/{}.png".format(s4)
            self.ids.FourthImage.source = self.Slot4Source
            self.ids.FourthImage.opacity = 1
        else:
            self.ids.FourthImage.source = ""
            self.ids.FourthImage.reload()
            self.ids.FourthImage.opacity = 0

        if m != "":
            self.MidSource = "cardImages/{}.png".format(m)
            self.ids.MidImage.source = self.MidSource
            self.ids.MidImage.opacity = 1
        else:
            self.ids.MidImage.source = ""
            self.ids.MidImage.reload()
            self.ids.MidImage.opacity = 0

        self.Engine()


    def ClickedFirstSlot(self):
        card = variables.BenimDestem[0]
        if card != "" and variables.MyTurn:
            variables.BenimDestem[0] = ""
            self.displayImages()
            self.YouPlayed(card)

    def ClickedSecondSlot(self):
        card = variables.BenimDestem[1]
        if card != "" and variables.MyTurn:
            variables.BenimDestem[1] = ""
            self.displayImages()
            self.YouPlayed(card)

    def ClickedThirdSlot(self):
        card = variables.BenimDestem[2]
        if card != "" and variables.MyTurn:
            variables.BenimDestem[2] = ""
            self.displayImages()
            self.YouPlayed(card)

    def ClickedFourthSlot(self):
        card = variables.BenimDestem[3]
        if card != "" and variables.MyTurn:
            variables.BenimDestem[3] = ""
            self.displayImages()
            self.YouPlayed(card)

    def YouPlayed(self, playedCard):
        variables.MyTurn = False

        if ((playedCard == "Sinek_J" or playedCard == "Maca_J" or playedCard == "Karo_J" or playedCard == "Kupa_J") and (len(variables.Orta) != "0")):
            variables.Orta.append(playedCard)
            for k in range(0, len(variables.Orta)):
                variables.BenimToplananlar.append(variables.Orta[k])
            variables.Orta.clear()

        elif (len(variables.Orta) == 0):
            variables.Orta.append(playedCard)

        else:
            if (variables.AsilDeste[variables.Orta[len(variables.Orta) - 1]] == variables.AsilDeste[playedCard]):
                if len(variables.Orta) == 1: variables.BenimPuan += 10; print("PISTIIII")
                variables.Orta.append(playedCard)
                for k in range(0, len(variables.Orta)):
                    variables.BenimToplananlar.append(variables.Orta[k])
                variables.Orta.clear()
            else:
                variables.Orta.append(playedCard)

        self.displayImages()

    def hasFittingCard(self, midCard): #ComputerPlays() Sub-Function
        numeric_value = variables.AsilDeste[midCard]
        for card in variables.OnunDestesi:
            if numeric_value == variables.AsilDeste[card]:
                return True
        return False

    def hasJoker(self): #ComputerPlays() Sub-Function
        if variables.OnunDestesi.__contains__("Sinek_J") or variables.OnunDestesi.__contains__("Maca_J") :
            return True
        elif variables.OnunDestesi.__contains__("Kupa_J") or variables.OnunDestesi.__contains__("Karo_J") :
            return True
        else:
            return False

    def whichCardTho(self, Type_of_Card): #ComputerPlays() Sub-Function
        if Type_of_Card == "joker":
            for cards in variables.OnunDestesi:
                if cards == "Sinek_J":
                    return "Sinek_J"
                elif cards == "Kupa_J":
                    return "Kupa_J"
                elif cards == "Karo_J":
                    return "Karo_J"
                elif cards == "Maca_J":
                    return "Maca_J"
        elif Type_of_Card == "num":
            numeric_value = variables.AsilDeste[variables.Orta[len(variables.Orta)-1]]
            for card in variables.OnunDestesi:
                if numeric_value == variables.AsilDeste[card]:
                    return card
    def firstCardThatIsntJoker(self):
        temp_list = variables.OnunDestesi.copy()
        if temp_list.__contains__("Sinek_J"):
            temp_list.remove("Sinek_J")
        if temp_list.__contains__("Karo_J"):
            temp_list.remove("Karo_J")
        if temp_list.__contains__("Kupa_J"):
            temp_list.remove("Kupa_J")
        if temp_list.__contains__("Maca_J"):
            temp_list.remove("Maca_J")

        if len(temp_list) == 0:
            return ""
        else:
            return temp_list[0]

    def ComputerPlays(self, dt):
        variables.MyTurn = True
        if len(variables.Orta) > 0:
            print(variables.Orta[len(variables.Orta)-1])
            print(self.hasFittingCard(variables.Orta[len(variables.Orta)-1]))
            print(self.hasJoker())

        if len(variables.Orta) > 0:
            mid = variables.Orta[len(variables.Orta)-1]
            bool1 = self.hasFittingCard(mid)
            bool2 = self.hasJoker()
            if bool1 is True: #Sayisal Denk Bir Karta Sahip
                cardToPlay = self.whichCardTho("num")
                if len(variables.Orta) == 1: variables.BilginPuan += 10; print("PISTIIII")
                variables.OnunDestesi.remove(cardToPlay)
                variables.Orta.append(cardToPlay)
                for i in variables.Orta:
                    variables.OnunToplananlar.append(i)
                variables.Orta.clear()
            elif (bool2 is True and len(variables.Orta) > 4): #2sine de girdi aaaa fixed, i guess...
                cardToPlay = self.whichCardTho("joker")
                variables.OnunDestesi.remove(cardToPlay)
                variables.Orta.append(cardToPlay)
                for i in variables.Orta:
                    variables.OnunToplananlar.append(i)
                variables.Orta.clear()
            else:
                nojoker_card = self.firstCardThatIsntJoker()
                if nojoker_card != "":
                    variables.Orta.append(nojoker_card)
                    variables.OnunDestesi.remove(nojoker_card)
                elif nojoker_card == "":
                    print(variables.OnunDestesi)
                    cardToPlaym = self.whichCardTho("joker")
                    variables.OnunDestesi.remove(cardToPlaym)
                    variables.Orta.append(cardToPlaym)
                    for i in variables.Orta:
                        variables.OnunToplananlar.append(i)
                    variables.Orta.clear()
        elif len(variables.Orta) == 0:
            nojoker_card = self.firstCardThatIsntJoker()
            if nojoker_card != "":
                variables.Orta.append(nojoker_card)
                variables.OnunDestesi.remove(nojoker_card)
            elif nojoker_card == "":
                cardToPlay = self.whichCardTho("joker")
                variables.OnunDestesi.remove(cardToPlay)
                variables.Orta.append(cardToPlay)

        if(len(variables.Eksilecek)==0): print("Kartlar bitti ALOOOOOO")
        print(variables.BenimDestem, variables.OnunDestesi)
        self.displayImages()

        if(len(variables.Eksilecek)==0 and len(variables.OnunDestesi)==0):
            Clock.schedule_once(self.ToTheEnd, 0.5)
            return None


    Line = StringProperty("")
    def Wait(self, dt):
        self.Line = "W A I T"
    def Wait2(self, dt):
        self.Line = "W A I T ."
    def Wait3(self, dt):
        self.Line = "W A I T . ."
    def Wait4(self, dt):
        self.Line = "W A I T . . ."
    def Wait5(self, dt):
        self.Line = ""
    def Engine(self):
        if variables.MyTurn == False:
            Clock.schedule_once(self.Wait, 0.1)
            Clock.schedule_once(self.Wait2, 0.3)
            Clock.schedule_once(self.Wait3, 0.5)
            Clock.schedule_once(self.Wait4, 0.7)
            Clock.schedule_once(self.Wait5, 0.9)
            Clock.schedule_once(self.ComputerPlays, 0.9)
        if len(variables.OnunDestesi) == 0 and len(variables.Eksilecek) != 0:

            Clock.schedule_once(self.distributeTheCards, 0.6)

    def clean(self):
        self.ids.FirstImage.source = ""
        self.ids.FirstImage.reload()
        self.ids.FirstImage.opacity = 0

        self.ids.SecondImage.source = ""
        self.ids.SecondImage.reload()
        self.ids.SecondImage.opacity = 0

        self.ids.ThirdImage.source = ""
        self.ids.ThirdImage.reload()
        self.ids.ThirdImage.opacity = 0

        self.ids.FourthImage.source = ""
        self.ids.FourthImage.reload()
        self.ids.FourthImage.opacity = 0

        self.ids.MidImage.source = ""
        self.ids.MidImage.reload()
        self.ids.MidImage.opacity = 0






class Manager(ScreenManager):
    pass

kv = Builder.load_file("cardGame.kv")

class CardApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    CardApp().run()

""" Stack Overflow
def clear_image(self):
        self.ids.img2.source = ''
        self.ids.img2.reload()
"""