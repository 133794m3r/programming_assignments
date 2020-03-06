select pokemon_name, (multipliers.multiplier*pokemon.str*1.0) as "modifiedStrength",element from pokemon join multipliers on pokemon.element_id = multipliers.id where "modifiedStrength" >= 40 Order By "modifiedStrength" DESC 
