import pytest

from dev.characters import Character, Orc
from dev.items import Weapons

@pytest.fixture
def char():
    return Character()

@pytest.fixture
def orc():
    return Orc()

def test_character_must_start_with_no_inventory(char):
    assert len(char.inventory) == 0

def test_character_must_start_with_no_weapon(char):
    assert char.weapon == None

def test_character_must_start_level_one(char):
    assert char.level == 1

def test_character_add_weapon_to_inventory(char):
    char.add_inventory(Weapons.DRAGON_HAMMER)
    assert len(char.inventory) == 1
    assert char.inventory[0].name == "Dragon Hammer"

def test_character_dont_add_weapon_inexistent_to_inventory(char):
    with pytest.raises(ValueError) as e:
      char.add_inventory("Dragon Hammer")
    assert 'ValueError' in str(e)

def test_character_equip_weapon(char):
    char.add_inventory(Weapons.DRAGON_HAMMER)
    char.equip_weapon(Weapons.DRAGON_HAMMER)
    assert len(char.inventory) == 0
    assert char.weapon == Weapons.DRAGON_HAMMER


def test_character_dont_equip_weapon_inexistent(char):
    char.add_inventory(Weapons.DRAGON_HAMMER)
    with pytest.raises(ValueError) as e:
      char.equip_weapon("Dragon Hammer")
    assert 'ValueError' in str(e)

def test_character_dont_equip_weapon_not_in_inventory(char):
    with pytest.raises(ValueError) as e:
      char.equip_weapon(Weapons.DRAGON_HAMMER)
    assert 'ValueError' in str(e)

def test_character_levels_up(char):
    char.gain_experience(1000)
    assert char.level == 11

def test_character_gain_status_on_level(char):
  char.gain_experience(150)
  assert char.level == 2
  assert char.strengh == 8
  assert char.defense == 8
  assert char.health == 380
  assert char.experience == 50


def test_character_attack_another_player(char, orc):
  char.attack(orc)
  assert orc.health == 418

def test_character_attack_another_player_with_weapon(char, orc):
  char.add_inventory(Weapons.DRAGON_HAMMER)
  char.equip_weapon(Weapons.DRAGON_HAMMER)
  char.attack(orc)
  assert orc.health == 386

def test_character_attack_with_defense(char, orc):
  char.add_inventory(Weapons.DRAGON_HAMMER)
  char.equip_weapon(Weapons.DRAGON_HAMMER)
  orc.attack(char)
  assert char.health == 300