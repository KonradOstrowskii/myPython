"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

Za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Boxes got difrrents color.

Color of the box means how rare is the box.

green - 75%
orange  - 20%
purple - 4%
gold (legedary) - 1%

Ustaw, że jest 40% szansy, że nie spotkasz niczego. 60%, że będzie skrzynka.

Ustaw złoto jako to co może "wypaść" ze skrzynki:
zielony - 1000,
pomaranczowy - 4000,
fioletowy - 9000,
zlota - 16000

1 1 0+1
4 2 1 +1
9 3 2+1
16 4 3 +1

Pamiętaj o:
1) czystym kodzie
2) nazywaniu zmiennych tak by bylo samoopisujace sie
3) spróbuj napisać program po angielsku

"""
import random
from enum import Enum

Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
    Event.Chest: 0.6,
    Event.Empty: 0.4
}
eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())


Colours = Enum('Colour ', {'Green': 'VeryCommon',
                           'Orange': 'Common',
                           'Purple': 'Rare',
                           'Gold': 'ExtraRare'
                           }
               )

chestColoursDictionary = {
    Colours.Green:  75,
    Colours.Orange: 20,
    Colours.Purple: 4,
    Colours.Gold:   1
}
chestColourList = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())

rewardsForChests = {
    chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
    for reward in range(len(chestColourList))
}

lengthGame = 5
goldCollected = 0

print("""Hey let's start the game,
There is 5 moves during which you can get 5 chest with gold,
We prepare: green chest wich contains 1000,
orange chest wich contains 4000,
purple chest wich contains 9000,
gold chest wich contains 16000""")

while lengthGame > 0:
    gamerAnswer = input("Let's go?")
    if (gamerAnswer == "yes"):
        print("So ,let's see how lucky You are")
        drawnEvent = random.choices(eventList, eventProbability)[0]
        if (drawnEvent == Event.Chest):
            print("You've drawn a CHEST")
            drawnColour = random.choices(
                chestColourList, chestColourProbability)[0]
            print("The chest  :", drawnColour,
                  "this box is :", drawnColour.value)
            gamerReward = rewardsForChests[drawnColour]
            goldCollected = goldCollected + gamerReward
        elif(drawnEvent == Event.Empty):
            print("There was no box , sorry")

    else:
        print("You have to finish ")
        continue

    lengthGame = lengthGame - 1
print("Congratulation, you have collected : ", goldCollected)
