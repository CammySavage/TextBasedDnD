import random

modifier = {
    1: -5,
    2: -4,
    3: -4,
    4: -3,
    5: -3,
    6: -2,
    7: -2,
    8: -1,
    9: -1,
    10: 0,
    11: 0,
    12: 1,
    13: 1,
    14: 2,
    15: 2,
    16: 3,
    17: 3,
    18: 4,
    19: 4,
    20: 5,
    21: 5,
    22: 6,
    23: 6,
    24: 7,
    25: 7,
    26: 8,
    27: 8,
    28: 9,
    29: 9,
    30: 10
}


class CharacterCreation:
    """Functions used to create a character to use for the game."""

    def __init__(self, name: str):
        """Initialise character object"""
        self.name = name
        self.strength = random.randint(1, 30)
        self.dexterity = random.randint(1, 30)
        self.constitution = random.randint(1, 30)
        self.wisdom = random.randint(1, 30)
        self.intelligence = random.randint(1, 30)
        self.charisma = random.randint(1, 30)
        self.userClass = ""
        self.proficiency = 2
        self.bonusAct = ""

        # sets up stat modifiers
        self.strMod = modifier[self.strength]
        self.dexMod = modifier[self.dexterity]
        self.conMod = modifier[self.constitution]
        self.intMod = modifier[self.intelligence]
        self.chaMod = modifier[self.charisma]

    def choose_class(self):
        print("You may choose a class from Barbarian, Bard, Cleric,"
              " Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, "
              "Warlock or Wizard. Each comes with their own strengths."
              " Choose wisely.")
        self.userClass = input().lower()
        if self.userClass == "barbarian":
            


# Barbarian
# Bard
# Cleric
# Druid
# Fighter
# Monk
# Paladin
# Ranger
# Rogue
# Sorcerer
# Warlock
# Wizard

# def print_character(self):

character = CharacterCreation("cem")
character.choose_class()
print(character.userclass)