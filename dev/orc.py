from character import Character

class Orc(Character):
    def __init__(self) -> None:
        super().__init__()
        self._health  =  int(self.health * 1.4)
        self._strengh =  int(self.strengh * 2.2)
        self._defense =  int(self.defense * 1)

    def __str__(self) -> str:
      currentWeapon = 'ORC NO WEAPON' if self.weapon is None else 'ORC HAVE ' + self.weapon.name.upper()
      return f"RAAR! ME ORC. ORC FIGHT! ORC LEVEL {self.level} WITH {self.experience} XP! ME {self.strengh} STRONG AND {self.defense} DEFENSE. {currentWeapon}! {self.show_inventory()}"
    
    def show_inventory(self) -> str:
      if not self._inventory:
          return 'ORC NO ITENS IN BAG'
      else:
          items = ', '.join(item.name for item in self._inventory)
          return f'ORC HAVE {items.upper()}'