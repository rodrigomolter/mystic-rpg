from character import Character
from orc import Orc
from elf import Elf
from human import Human
from weapons import Weapons

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
  print(human.status())
  orc.attack(human)
  print(human.status())






if __name__ == "__main__":
  main()