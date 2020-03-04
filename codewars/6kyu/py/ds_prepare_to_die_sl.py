def souls(character, build):
    warrior={'level':4, 'stats':[11,8,12,13,13,11,9,9]}
    knight={'level':5, 'stats':[14, 10, 10, 11, 11, 10, 9, 11]}
    wanderer={'level':3, 'stats':[10, 11, 10, 10, 14, 12, 11, 8]}
    thief={'level':5, 'stats': [9, 11, 9, 9, 15, 10, 12, 11]}
    bandit={'level':4, 'stats': [12, 8, 14, 14, 9, 11, 8, 10]}
    hunter={'level':4, 'stats': [11, 9, 11, 12, 14, 11, 9, 9]}
    sorcerer={'level':3, 'stats':[8, 15, 8, 9, 11, 8, 15, 8]}
    pyromancer={'level':1, 'stats':[10, 12, 11, 12, 9, 12, 10, 8]}
    cleric={'level':2, 'stats':[11, 11, 9, 12, 8, 11, 8, 14]}
    deprived={'level':6, 'stats':[11, 11, 11, 11, 11, 11, 11, 11]}
    characters={'warrior':warrior, 'knight':knight, 'wanderer':wanderer, 'thief':thief, 'bandit':bandit, 'hunter':hunter, 'sorcerer':sorcerer, 'pyromancer':pyromancer, 'cleric':cleric, 'deprived':deprived}
    chosen_class=characters[character]
    early_souls=[0,0,673,690,707,724,741,758,775,793,811,829]
    later_souls=lambda x:round(pow(x,3)*0.02 + pow(x,2) * 3.06 + 105.6 * x - 895)
    new_level=(sum(build)-sum(chosen_class['stats']))+chosen_class['level']
    souls=0
    souls_required=0
    start_level=chosen_class['level']+1
    print(start_level,new_level)
    for i in range(start_level,new_level+1):
    	souls_required+=(early_souls[i] if i < 12 else later_souls(i))

    return f"Starting as a {character}, level {new_level} will require {souls_required} souls."
#TODO:Add this to the test cases.
"""
souls('deprived', [11, 11, 11, 11, 11, 11, 11, 11]),'Starting as a deprived, level 6 will require 0 souls.'
souls('pyromancer', [10, 12, 11, 12, 9, 12, 11, 8]),'Starting as a pyromancer, level 2 will require 673 souls.'
souls('pyromancer', [16, 12, 11, 12, 9, 12, 10, 8]),'Starting as a pyromancer, level 7 will require 4293 souls.'
souls('pyromancer', [16, 12, 11, 12, 9, 12, 13, 8]),'Starting as a pyromancer, level 10 will require 6672 souls.'
souls('pyromancer', [16, 12, 11, 12, 9, 12, 13, 10]),'Starting as a pyromancer, level 12 will require 8348 souls.'
souls('knight', [16, 12, 21, 16, 22, 11, 16, 18]),'Starting as a knight, level 51 will require 274802 souls.'
souls('wanderer', [18, 25, 13, 12, 34, 13, 30, 26]),'Starting as a wanderer, level 88 will require 1355843 souls.'
"""
