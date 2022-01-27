"""
Write a short game in which you have 5 moves one way through the CHAMBER.

Every time you have the chance to meet dear box or NOTHING

The boxes have different colors.

The color of the box indicates how rare the box is.
green   - 75%
orange - 20%
purple - 4%
gold (legendary) - 1%

Set that there is a 40% chance that you will not meet anything,
60% that will be a box. Set gold as what can "fall out" of the box:

green - 1000,
orange  - 4000,
purple - 9000,
gols - 16000

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
    Colours.Green: 75,
    Colours.Orange: 20,
    Colours.Purple: 4,
    Colours.Gold: 1
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
