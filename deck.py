import random

class Card:
    def __init__(self, suit:str, number: int) -> None:
        self.suit = suit
        self.number = number

    def __repr__(self):
        return f'{self.suit} of {self.number}`'

class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.makeDeck()

    def makeDeck(self):
        suits = ['♠️', "♣️", "♥️", "♦️"]
        faces = [*range(2,11)]
        faces.extend(["Ace", "Jack", "Queen", "King"])
        for suit in suits:
            for face in faces:
                self.cards.append(Card(suit, face))
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def drawRandomCards(self, number:int=1) -> list[Card]:
        return [random.choice(self.cards) for _ in range(0,number+1)]

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    r1 = deck.drawRandomCards(5)
    print(r1)
