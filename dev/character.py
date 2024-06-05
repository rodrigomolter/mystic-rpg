from weapons import Weapons

class Character():
  def __init__(self) -> None:
    self._health = 300
    self._strengh = 7
    self._defense =  5
    self._level =  1
    self._experience = 0
    self._inventory = []
    self._weapon = None


  def __str__(self) -> str:
    currentWeapon = 'no weapon' if self.weapon is None else 'a ' + self.weapon.name
    return f"Hello! I am simple citizen of level {self.level} with {self.experience} experience points, {self.strengh} strength and {self.defense} defense. I'm equipped with {currentWeapon} and {self.show_inventory()}"
  
  def equip_weapon(self, weapon: Weapons) -> str:
     if not isinstance(weapon, Weapons):
       raise ValueError(f"Invalid Weapon: {weapon}. Must be of WEAPONS type")
     
     if weapon not in self.inventory:
       raise ValueError(f"Invalid Weapon: {weapon}. Weapon not find in the inventory")
     
     self.inventory.remove(weapon)
     if self.weapon is not None:
        self.add_inventory(weapon)

     self._weapon = weapon
     return f"{weapon.name} equipped! It has {weapon.attack} attack and {weapon.defense} defense"

  
  def add_inventory(self, weapon: Weapons) -> str:
    if not isinstance(weapon, Weapons):
      raise ValueError(f"Invalid Weapon: {weapon}. Must be of WEAPONS type")

    if len(self.inventory) == 5:
      return "Sorry! Looks like your inventory is full!"

    self.inventory.append(weapon)
    return f"{weapon.name} added to inventory!"
  
  def show_inventory(self) -> str:
    if not self._inventory:
        return 'I have no items in my inventory'
    else:
        items = ', '.join(item.name for item in self._inventory)
        return f'I have these items in the inventory: {items}'
  
  def gain_experience(self, amount: int) -> int:
    self._experience += amount
    if self.experience >= 100:
      self.level_up()

    return self.experience

  def level_up(self):
    if self.experience >= 100:
      self._level += 1
      self._experience -= 100
      self._defense += 3
      self._strengh += 1

  def status(self) -> str:
    return f"Health: {self.health}\nStrengh: {self.strengh}\nDefense: {self.defense}\nLevel: {self.level}\nExp: {self.experience}\nWeapon: {self.weapon}"  

  def got_hit(self, amount):
    if amount > 0 and self.health > 0:
      self._health -= amount

  def attack(self, enemy):
    weapon_attack = 0 if self.weapon is None else self.weapon.attack
    weapon_defense = 0 if enemy.weapon is None else enemy.weapon.defense
    damage = (self.strengh + weapon_attack) - (enemy.defense + weapon_defense)
    enemy.got_hit(damage)

  @property
  def weapon(self):
    return self._weapon
  
  @property
  def defense(self):
    return self._defense
  
  @property
  def strengh(self):
    return self._strengh
  
  @property
  def health(self):
    return self._health
  
  @property
  def level(self):
    return self._level
  
  @property
  def experience(self):
    return self._experience
  
  @property
  def inventory(self):
    return self._inventory