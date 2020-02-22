#!/usr/bin/env python3

def calculate_damage(attacker_type,defender_type,attack,defense):
	effectiveness={('fire', 'water'): 0.5, ('fire', 'electric'): 1, ('fire', 'grass'): 2, ('water', 'fire'): 2, ('water', 'electric'): 0.5, ('water', 'grass'): 0.5, ('electric', 'fire'): 1, ('electric', 'water'): 2, ('electric', 'grass'): 1, ('grass', 'fire'): 0.5, ('grass', 'water'): 2, ('grass', 'electric'): 1}
	atk_def=(attacker_type,defender_type)
	dmg_modifier = effectiveness[atk_def] if atk_def in effectiveness else 0.5
	dmg = 50 * (attack/defense) * dmg_modifier

	return dmg

def equals_check(a,b):
	return a == b
def test_me():
	print(equals_check(calculate_damage("fire", "water", 100, 100), 25))
	print(equals_check(calculate_damage("grass", "water", 100, 100), 100))
	print(equals_check(calculate_damage("electric", "fire", 100, 100), 50))
	print(equals_check(calculate_damage("grass", "electric", 57, 19), 150))
	print(equals_check(calculate_damage("grass", "water", 40, 40), 100))
	print(equals_check(calculate_damage("grass", "fire", 35, 5), 175))
	print(equals_check(calculate_damage("fire", "electric", 10, 2), 250))


test_me()
