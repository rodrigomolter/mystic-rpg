from characters import *
from items import Weapons

def main():
  citizen = Character()
  # print(citizen)
  orc = Orc()
  # print(orc)

  elf = Elf()
  # print(elf)

  human = Human()
  # print(human)

  print(orc.add_inventory(Weapons.DRAGON_HAMMER))
  print(orc.equip_weapon(Weapons.DRAGON_HAMMER))
  orc.gain_experience(20)
  orc.gain_experience(80)
  human.add_inventory(Weapons.BLESSED_SHIELD)
  human.equip_weapon(Weapons.BLESSED_SHIELD)
  print(human.status())
  orc.attack(human)
  print(human.status())






if __name__ == "__main__":
  main()