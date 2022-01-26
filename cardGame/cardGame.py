import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]

random.shuffle(cardList)

ListCardPLayer1 = []
ListCardPLayer2 = []


def drawCard(howManyCard, forWho):
    for i in range(0, howManyCard):
        card = cardList.pop()
        forWho.append(card)


drawCard(5, ListCardPLayer1)
drawCard(5, ListCardPLayer2)

print(ListCardPLayer1)
print(ListCardPLayer2)