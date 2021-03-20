typing = input("What is the typing of the Pokemon? ")

def effective(typing):
  secondary = False
  for x in range(len(typing)):
    if typing[x] == ' ':
      secondary = True
      primary_type = typing[:x]
      secondary_type = typing[x+1:]
      break
    primary_type = typing

  # weakness chart
  weakness={
        "normal" : ["fighting"],
        "fire" : ["water", "ground", "rock"],
        "water": ["grass", "electric"],
        "electric": ["ground"],
        "grass": ["fire", "ice", "poison", "bug", "flying"],
        "ice": ["fire", "fighting", "rock", "steel"],
        "fighting": ["flying", "psychic", "fairy"],
        "poison": ["ground", "psychic"],
        "ground": ["grass", "water", "ice"],
        "flying": ["electric", "ice", "rock"],
        "psychic": ["bug", "dark", "ghost"],
        "bug": ["rock", "flying", "fire"],
        "rock": ["fighting", "ground", "water", "grass", "steel"],
        "ghost": ["ghost", "dark"],
        "dragon": ["ice", "dragon", "fairy"],
        "dark": ["fighting", "fairy", "bug"],
        "steel": ["fire","fighting", "ground"],
        "fairy": ["steel", "poison"]
    }

  # resistance chart
  resist={
    "normal" : [],
    "fire" : ["fire", "grass", "ice", "steel", "bug", "fairy"],
    "water": ["fire", "water", "ice", "steel"],
    "electric": ["electric", "flying", "steel"],
    "grass" : ["electric", "grass", "water", "ground"],
    "ice": ["ice"],
    "fighting": ["bug", "dark", "rock"],
    "poison": ["grass", "fighting", "poison", "bug", "fairy"],
    "ground": ["poison", "rock"],
    "flying": ["grass", "fighting", "bug"],
    "psychic": ["psychic", "fighting"],
    "bug": ["grass", "fighting", "ground"],
    "rock": ["normal", "fire", "poison", "flying"],
    "ghost": ["poison", "bug"],
    "dragon": ["electric", "grass", "fire", "water"],
    "dark": ["ghost", "dark"],
    "steel": ["rock", "normal", "grass", "electric", "ice", "flying", "psychic", "bug", "dragon", "steel", "fairy"],
    "fairy": ["fighting","bug", "dark"]
  }

  # immunities chart
  immune={
    "normal" : ["ghost"],
    "flying" : ["ground"],
    "ground" : ["electric"],
    "ghost" : ["normal", "fighting"],
    "steel" : ["poison"],
    "dark" : ["psychic"],
    "fairy" : ["dragon"]
  }

  # determine all weaknesses
  if secondary:
    weaknesses = weakness[primary_type] + weakness[secondary_type]
  else:
    weaknesses = weakness[primary_type]

  # group x2 and x4 weaknesses
  twox_w = []
  fourx_w = []
  has_fourweak = False
  for x in range(len(weaknesses)):
    if weaknesses[x] not in twox_w:
      twox_w.append(weaknesses[x])
    else:
      fourx_w.append(weaknesses[x])
      has_fourweak = True
      twox_w.remove(weaknesses[x])

  # determine all resistances
  if secondary:
    resistances = resist[primary_type] + resist[secondary_type]
  else:
    resistances = resist[primary_type]

  # group x2 and x4 resistances
  twox_r = []
  fourx_r = []
  has_fourresist = False
  for x in range(len(resistances)):
    if resistances[x] not in twox_r:
      twox_r.append(resistances[x])
    else:
      fourx_r.append(resistances[x])
      has_fourresist = True
      twox_r.remove(resistances[x])

  # neutralize x2 resistance and weakness
  twoweak = twox_w[:]
  tworesist = twox_r[:]
  for x in range(len(twox_w)):
    if twox_w[x] in twox_r:
      twoweak.remove(twox_w[x])
      tworesist.remove(twox_w[x])

  # determine all immunities
  is_immune = False
  if primary_type in immune:
    immunities = immune[primary_type]
    is_immune = True
  else:
    immunities = []
  if secondary:
    if secondary_type in immune:
      immunities += immune[secondary_type]
      is_immune = True


  # remove immunites from all weakness and resistances
  if len(immunities) != 0:
    for x in range(len(immunities)):
      if immunities[x] in twoweak:
        twoweak.remove(immunities[x])
      if immunities[x] in tworesist:
        tworesist.remove(immunities[x])
      if immunities[x] in fourx_w:
        fourx_w.remove(immunities[x])
      if immunities[x] in fourx_r:
        fourx_r.remove(immunities[x])

  # output information
  print(f'2 times weak to {twoweak}')
  if len(fourx_w) != 0:  
    print(f'4 times weak to {fourx_w}')
  if len(tworesist) != 0:
    print(f'2 times resists {tworesist}')
  if len(fourx_r) != 0:
    print(f'4 times resists {fourx_r}')
  if len(immunities) != 0:
    print(f'Immune to {immunities}')

effective(typing)
