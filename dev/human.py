from character import Character

class Human(Character):
    def __init__(self) -> None:
        super().__init__()
        self._health  =  int(self.health * 1.3)
        self._strengh =  int(self.strengh * 1.4)
        self._defense =  int(self.defense * 1.8)

    def __str__(self) -> str:
      currentWeapon = 'no weapon' if self.weapon is None else 'a ' + self.weapon.name
      return f"Hello, I am a Human from the Kingdom of Rohan. At level {self.level}, I have {self.experience} experience points, {self.strengh} strength, and {self.defense} defense, armed with {currentWeapon}. {self.show_inventory()}"
    
    def show_inventory(self) -> str:
      if not self._inventory:
          return 'My inventory is empty.'
      else:
          items = ', '.join(item.name for item in self._inventory)
          return f'I have in my inventory a {items.upper()}'