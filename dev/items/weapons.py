from enum import Enum

class Weapons(Enum):
    SWORD_OF_FURY   = ("Sword of Fury", 71, 33)
    STONECUTTER_AXE = ("Stonecutter Axe", 50, 18)
    DRAGON_HAMMER   = ("Dragon Hammer", 32, 11)
    BLESSED_SHIELD  = ("Blessed Shield", 10, 68)

    def __init__(self, name, attack, defense) -> None:
        self._name = name
        self._attack = attack
        self._defense = defense

    @property
    def name(self) -> str:
        return self._name

    @property
    def attack(self) -> int:
        return self._attack

    @property
    def defense(self) -> int:
        return self._defense
