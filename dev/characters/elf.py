from .character import Character

class Elf(Character):
    def __init__(self) -> None:
        super().__init__()
        self._health  =  int(self.health * 1.2)
        self._strengh =  int(self.strengh * 1.7)
        self._defense =  int(self.defense * 1.5)

    def __str__(self) -> str:
      currentWeapon = 'no weapon at the momment' if self.weapon is None else 'with a ' + self.weapon.name
      return f"Greetings, I am an Elf of ancient wisdom and grace. At level {self.level}, I possess {self.experience} experience points, {self.strengh} strength, and {self.defense} defense. I am equipped with {currentWeapon}. {self.show_inventory()}"
    
    def show_inventory(self) -> str:
      if not self._inventory:
          return 'I carry no itens for now.'
      else:
          items = ', '.join(item.name for item in self._inventory)
          return f'For now i posses: {items}'