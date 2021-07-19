from banca import bancaGiveCard
from cards import cards
import menu as mn
import resourses as rsc
from msvcrt import getch

class player:
    def __init__(self, playerName):
        # player's states
        self.active = False
        self.player_passed = False

        # player's own data
        self.player_name = playerName
        self.player_score = 0.0
        self.player_coins = 100
    """Boleans"""
    # check if this player is active
    def checkActive(self):
        return self.active
    # set focus on this player
    def setActive(self):
        self.active = True   
    # this player lost the focus
    def setNotActive(self):
        self.active = False
    # Bolean: if player pass 7.5 points, the player lost
    def isPassed(self) -> bool:
        if self.player_score > 7.5:
            return True
        else:
            return False

    def isPassedCard(self, card) -> bool:
        if self.player_score + cards.getScore(self, card) > 7.5:
            return True
        else:
            return False
    # set the player just passed 7.5 points
    def setPassed(self):
        self.player_passed = True
    # set the player still playing
    def setNotPassed(self):
        self.player_passed = False

    """getters"""
    def getName(self):
        return self.player_name

    def getScore(self) -> float:
        return self.player_score

    def getCoins(self):
        return float(self.player_coins)

    def getData(self):
        return ( 
        self.active,
        self.player_passed,
        self.player_name,
        self.player_score,
        self.player_coins)
    """setters"""
    def setName(self, name):
        self.player_name = name
    
    def setScore(self, score):
        self.player_score = score

    """Methods"""
    # the player get a card from the bank.
    def getCard(self, deck):
        card = bancaGiveCard(deck)
        return card
    
    # depent of which card the player received, this compute his score.
    def addScore(self, card):
        self.player_score += cards.getScore(self, card)


    """player logic"""
    def jugadorTurn(self, deck):
        self.setActive()
        while not self.isPassed() and self.checkActive():
            mn.playing(self.player_name)
            rsc.sleep(0.3)

            # el jugador toma una carta del deck.
            card =  str(self.getCard(deck))
            mn.getCard(card)

            if self.isPassedCard(card):
                input("\t\tse ha pasado.")
                self.setPassed()
                self.setNotActive()
                self.setScore(0.0)
                # break
            else:
                self.addScore(card)
                mn.getActualScore(self.getScore())
                print("¿Te plantas? si/no - s/n")
                yesornot = rsc.recibir_eleccion_str()
                if yesornot == "y" or yesornot == "si" or yesornot == "s" :
                    print("Te has platando con una puntación de ", self.getScore())
                    # break
                    self.setNotActive()
                elif yesornot == "n" or yesornot == "no":
                    continue                
            print("press any key to continue.. final del turno")
            getch()
        self.setNotActive()

        """Banca Logic"""
    def bancaTurn(self, deck):
        self.setActive()
        while not self.isPassed() and self.checkActive():
            mn.playing(self.player_name)
            # rsc.sleep(3)

            # el jugador toma una carta del deck.
            card =  str(self.getCard(deck))
            mn.getCard(card)

            if self.isPassedCard(card):
                input("\t\tse ha pasado.")
                self.setPassed()
                self.setNotActive()
                self.setScore(0.0)
                # break
            else:
                self.addScore(card)
                mn.getActualScore(self.getScore())
                print("¿Te plantas? si/no - s/n")
                yesornot = rsc.recibir_eleccion_str()
                if yesornot == "y" or yesornot == "si" or yesornot == "s" :
                    print("Te has platando con una puntación de ", self.getScore())
                    # break
                    self.setNotActive()
                elif yesornot == "n" or yesornot == "no":
                    continue                
            print("press any key to continue.. final del turno")
            getch()
        self.setNotActive()
