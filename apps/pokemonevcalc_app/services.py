import math
from .models import Nature, Type, Stat
from collections import deque


class Calculation:
    def __init__(self):
        self.base_power = 0
        self.attack_modifier = 0
        self.defense_modifier = 0
        self.final_modifier = 0
        self.base_power_2 = 0
        self.attack_modifier_2 = 0
        self.defense_modifier_2 = 0
        self.final_modifier_2 = 0
        self.attack = 0
        self.defense = 0


class APIService:

    
    
    # public Pokemon getPokemon(String pokemonName:
    #     Optional<Pokemon> tempPokemon = pokemonRepo.findByIdentifier(pokemonName)
    #     if tempPokemon.isPresent():
    #         return tempPokemon[)
    #     }
    #     else:
    #         return None
    #     }
    # }
    
    # public Move getMove(String move:
    #     Optional<Move> tempMove = moveRepo.findByIdentifier(move)
    #     if tempMove.isPresent():
    #         return tempMove[)
    #     }
    #     else:
    #         return None
    #     }
    # }
    
    
    # public String lowerStringRemoveDashes(String s:
    #     return s.toLowerCase().replace(' ', '-')
    # }
    
    
    # public Ability getAbility(String ability:
    #     Optional<Ability> tempAbility = abilityRepo.findByIdentifier(ability)
    #     if tempAbility.isPresent():
    #         return tempAbility[)
    #     }
    #     else:
    #         return None
    #     }
    # }
    
    def get_type(self, type):
        t = Type.objects.get(identifier=type) 
        return t
    
    # public Type get_type(Long id:
    #     Optional<Type> tempType= typeRepo.findById(id)
    #     if tempType.isPresent():
    #         return tempType[)
    #     }
    #     else:
    #         return None
    #     }
    # }
    
    # public MoveTarget getMoveTarget(String movetarg:
    #     Optional<MoveTarget> tempType= moveTargRepo.findByIdentifier(movetarg)
    #     if tempType.isPresent():
    #         return tempType[)
    #     }
    #     else:
    #         return None
    #     }
    # }
    
    def get_stat_by_name(self, name):

        return Stat.objects.get(identifier=name)
    
    # public Nature getNature(String name:
    #     Optional<Nature> tempNature = natureRepo.findByIdentifier(name)
    #     if tempNature.isPresent():
    #         return tempNature[)
    #     }
    #     else:
    #         return None
    #     }
    # }


    def get_nature_by_increase_and_decrease(self, increased, decreased):
        query1= list(Nature.objects.all())
        for nature in query1:
            if nature.decreased_stat.stat.identifier == decreased and nature.increased_stat.stat.identifier == increased:
                return nature
    
    # public LegacyMove getLegacyMove(String name, generation:
    #     List<LegacyMove> thing = legacyRepo.getMoveWithGen(name, generation)
    #     if thing.size() > 0:
    #         return thing[0]
    #     }
    #     else:
    #         return None
    #     }
    # }


        
    def poke_round(self, damage):
        return math.ceil(damage-0.5)
        
    def affected_by_sheer_force(self, move):
        sheer_force_ids = [3, 5, 6, 7, 21, 32, 37, 69, 70, 71, 72, 73, 74, 76, 77, 78, 93, 126, 139, 140, 141, 147, 151, 153, 159, 198, 201, 210, 254, 261, 263, 264, 268, 274, 275, 276, 296, 297, 330, 331, 332, 333, 334, 372, 375, 380, 393, 396, 397, 419, 425, 500]
        return (move.id in sheer_force_ids)    
    
    def affected_by_reckless(self, move):
        reckless_ids = [46, 49, 199, 254, 263, 270]
        return (move.id in reckless_ids)    

    
    def affected_by_mega_launcher(self, move):
        pulses = ["aura-sphere", "dark-pulse", "dragon-pulse", "heal-pulse", "origin-pulse", "terrain-pulse", "water-pulse"]
        return (move.identifier in pulses)
    
    
    def affected_by_iron_fist(self, m):
        punches = ["bullet-punch", "double-iron bash", "drain-punch", "dynamic-punch", "fire-punch", "focus-punch", "hammer-arm", "ice-punch", "mach-punch", "mega-punch", "meteor-mash", "plasma-fists", "power-up-punch", "shadow-punch", "surging-strikes", "thunder-punch", "wicked-blow"]
        return (m.identifier in punches) 


    def can_knock_off_item(self, item):
        items = ["metagrossite", "gengarite", "gardevoirite", "charizardite-x", "venusaurite", "blastoisinite", "mewtwonite-x", "mewtwonite-y", "blazikenite", "medichamite", "houndoominite", "aggronite", "banettite", "tyranitarite", "scizorite", "pinsirite", "aerodactylite", "lucarionite", "abomasite", "kangaskhanite", 
                "gyaradosite", "absolite", "charizardite-y", "alakazite", "heracronite", "mawilite", "manectite", "garchompite", "latiasite", "latiosite", "swampertite", "sceptilite", "sablenite", "altarianite", "galladite", "audinite", "sharpedonite", "slowbronite", "steelixite", "pidgeotite", "glalitite", "diancite", "camperuptite", "lopunnite", "salamencite", "beedrillite", "griseous-orb", 
                "normalium-z", "firium-z", "waterium-z", "electrium-z", "grassium-z", "icium-z", "fightinium-z", "poisonium-z", "groundium-z", "flyinium-z", "psychium-z", "buginium-z", "rockium-z", "ghostium-z", "dragonium-z", "darkinium-z", "steelium-z", "fairium-z", "pikanium-z", "decidium-z", "incinium-z", "primarium-z", "tapunium-z", "marshadium-z", "aloraichium-z", "snorlium-z", "eevium-z", "mewnium-z", 
                "pikashunium-z"]
        return (not item.identifier in items)


    def affected_by_strong_jaw(self, m):
        bites = ["bite", "crunch", "fire-fang", "fishious-rend", "ice-fang", "jaw-lock", "poison-fang", "psychic-fangs", "thunder-fang"]
        return (m.identifier in bites)


    def affected_by_tough_claws(self, m):
        physicalnoncontact = ["attack-order", "aura-wheel", "beat-up", "bone-rush", "bonemerang", "bulldoze", "bullet-seed", 
                "diamond-storm", "dragon-darts", "drum-beating", "earthquake", "explosion", "feint", "fissure", "fling", "freeze-shock", 
                "fusion-bolt", "glacial-lance", "grav-apple", "gunk-shot", "ice-shard", "icicle-crash", "icicle-spear", "lands-wrath", "leafage", 
                "metal-burst", "meteor-assault", "pay-day", "petal-blizzard", "pin-missile", "poison-sting", "poltergeist", "precipice-blades", 
                "present", "psycho-cut", "pyro-ball", "razor-leaf", "rock-blast", "rock-slide", "rock-throw", "rock-tomb", "rock-wrecker", "sacred-fire", 
                "sand-tomb", "scale-shot", "seed-bomb", "self-destruct", "shadow-bone", "sky-attack", "smack-down", "spirit-shackle", "stone-edge", 
                "thousand-arrows", "thousand-waves"]
        specialcontact = ["draining-kiss", "grass-knot", "infestation", "petal-dance"]
        if m.damage_class_id==2:
            return not (m.identifier in physicalnoncontact)
        elif m.damage_class_id==3:
            return (m.identifier in specialcontact)
        return False
    
    def ignores_abilities(self, atk_pokemon):
        if atk_pokemon.ability.identifier=="teravolt" or atk_pokemon.ability.identifier=="mold-breaker" or atk_pokemon.ability.identifier=="turboblaze":
            return True
        return False
    
    def is_pokemon_flying(self, pokemon, c):
        if c.gravity or c.smack_down:
            return False
        if pokemon.item and pokemon.item.identifier=="iron-ball":
            return False
        if pokemon.is_type("flying"):
            return True
        if pokemon.item and pokemon.item.identifier=="air-balloon":
            return True
        if pokemon.ability.identifier=="levitate":
            return True
        return False
    
    def convert_to_z(self, m): 
        bp = m.power
        if m.identifier=="v-create":
            return 220
        elif m.identifier=="thousand-arrows":
            return 180
        elif m.identifier=="hex":
            return 160
        elif m.identifier=="mega-drain":
            return 120
        elif m.identifier=="gear-grind":
            return 180
        elif m.identifier=="core-enforcer":
            return 140
        elif m.identifier=="weather-ball":
            return 160
        elif bp <= 55:
            return 100
        elif bp <= 65:
            return 120
        elif bp <= 75:
            return 140
        elif bp <= 85:
            return 160
        elif bp <= 95:
            return 175
        elif bp <= 100:
            return 180
        elif bp <=  110:
            return 185
        elif bp <= 125:
            return 190
        elif bp <= 130:
            return 195
        else:
            return 200
    
    


    def calculate_base_power(self, condition, atk_pokemon, def_pokemon):
        attacker_dmax = (condition.opp_dmax and condition.pokemon==atk_pokemon) or (condition.self_dmax and condition.pokemon==def_pokemon)
        defender_dmax = (condition.self_dmax and condition.pokemon==atk_pokemon) or (condition.opp_dmax and condition.pokemon==def_pokemon)

        multiplier = 4096
        m = condition.move

        #---------------------------------------------------------------------------------
        #-----------------------------BEGIN BASE POWER------------------------------------
        #---------------------------------------------------------------------------------
        basePower = m.power
        if attacker_dmax:
            basePower = m.get_max_move_power()
        
        
        #LOW KICK/GRASS KNOT
        if m.identifier=="grass-knot" or m.identifier=="low-kick":
            if defender_dmax and not  attacker_dmax:
                return 0
            if def_pokemon.weight < 100:
                m.power=20
            elif def_pokemon.weight < 250:
                m.power=40
            elif def_pokemon.weight < 500:
                m.power=60
            elif def_pokemon.weight < 1000:
                m.power=80
            elif def_pokemon.weight < 2000:
                m.power=100
            else:
                m.power=120        
        
        
        #HEAVY SLAM/HEAT CRASH
        if m.identifier=="heavy-slam" or m.identifier=="heat-crash":
            if defender_dmax and not  attacker_dmax:
                return 0
            if atk_pokemon.weight/def_pokemon.weight < 2:
                m.power=40
            elif atk_pokemon.weight/def_pokemon.weight < 3:
                m.power=60
            elif atk_pokemon.weight/def_pokemon.weight < 4:
                m.power=80
            elif atk_pokemon.weight/def_pokemon.weight < 5:
                m.power=100
            else:
                m.power=120

        
        
        #ACROBATICS
        if m.identifier=="acrobatics" and (atk_pokemon.item==None or atk_pokemon.item.identifier=="flying-gem"):
            basePower = 110
        
        
        #WAKE-UP-SLAP
        if def_pokemon.status=="Sleep" and m.identifier=="wake-up-slap":
            basePower = 140
        
        
        #SMELLING SALTS
        if def_pokemon.status=="Paralyze" and m.identifier=="smelling-salts":
            basePower = 140
        
        
        #WATER SHURIKEN
        if atk_pokemon.identifier=="ash-greninja" and m.identifier=="water-shuriken":
            basePower = 20
    
        
        #HEX
        if not def_pokemon.status=="None" and m.identifier=="hex":
            basePower = 130
        
        
        #WEATHER-BALL
        if not condition.weather=="None" and m.identifier=="weather-ball":
            basePower = 100
            if condition.weather=="Rain":
                m.attack_type=self.get_type("water")
            elif condition.weather=="Sun":
                m.attack_type=self.get_type("fire")
            elif condition.weather=="Sand":
                m.attack_type=self.get_type("rock")
            elif condition.weather=="Hail":
                m.attack_type=self.get_type("ice")
        
        
        #BOLT BEAK/FISHIOUS REND
        if m.identifier=="fishious-rend" or m.identifier=="bolt-beak":
            if def_pokemon==condition.pokemon and self.calculate_speed(def_pokemon, condition.opp_boost, condition.weather, condition.terrain, condition.foe_tw) < self.calculate_speed(atk_pokemon, condition.your_boost, condition.weather, condition.terrain, condition.your_tw):
                basePower=170
            elif atk_pokemon==condition.pokemon and self.calculate_speed(atk_pokemon, condition.opp_boost, condition.weather, condition.terrain, condition.foe_tw) > self.calculate_speed(def_pokemon, condition.your_boost, condition.weather, condition.terrain, condition.your_tw):
                basePower=170

        
        #----------------------------------------------------------------------
        #TODO: Assurance, Avalanche, Revenge, Pledges, Gust/Twister, Round, Pursuit, Stomping Tantrum
        #----------------------------------------------------------------------

        
        #BASE POWER LOGIC (IT'LL BE MESSY)
        if condition.aura_break:
            if m.is_type("fairy") and condition.fairy_aura or m.is_type("dark") and condition.dark_aura:
                multiplier = (multiplier*3072/4096)
            
        
        #----------------------------------------------------------------------
        #TODO: RIVALRY
        #----------------------------------------------------------------------

        
        #-IZE -ATE abilities
        if m.is_type("normal") and (atk_pokemon.ability.identifier=="galvanize" or atk_pokemon.ability.identifier=="aerilate" or 
                atk_pokemon.ability.identifier=="refrigerate" or atk_pokemon.ability.identifier=="pixilate"):
            if condition.generation == 6:
                multiplier = (multiplier*5325/4096)
            
            else:
                multiplier = (multiplier*4915/4096)
            
            if atk_pokemon.ability.identifier=="refrigerate":
                m.attack_type=self.get_type("ice")
            elif atk_pokemon.ability.identifier=="galvanize":
                m.attack_type=self.get_type("electric")
            elif atk_pokemon.ability.identifier=="pixilate":
                m.attack_type=self.get_type("fairy")
            elif atk_pokemon.ability.identifier=="aerilate":
                m.attack_type=self.get_type("flying")
            
        elif atk_pokemon.ability.identifier=="normalize":
            multiplier = (multiplier*4915/4096)
            m.attack_type=self.get_type("normal")
        
        
        #BATTERY
        if condition.battery and m.damage_class_id==3:
            multiplier = (multiplier* 5325/4096)
        
        
        #SAND FORCE
        if condition.weather=="Sand" and atk_pokemon.ability.identifier=="sand-force" and (m.get_attack_type().identifier=="rock" or m.get_attack_type().identifier=="steel" or m.get_attack_type().identifier=="ground"):
            multiplier = (multiplier* 5325/4096)
        
        
        #----------------------------------------------------------------------
        #TODO: Analytic
        #----------------------------------------------------------------------

        #IRON FIST
        if not condition.z and not ((condition.self_dmax and not atk_pokemon==condition.pokemon) or (condition.opp_dmax and atk_pokemon==condition.pokemon)):
            if atk_pokemon.ability.identifier=="iron-fist" and  self.affected_by_iron_fist(m):
                multiplier = (multiplier*4915/4096)    
        
        
        #RECKLESS
        if not condition.z and not ((condition.self_dmax and not atk_pokemon==condition.pokemon) or (condition.opp_dmax and atk_pokemon==condition.pokemon)):
            if atk_pokemon.ability.identifier=="reckless" and  self.affectedByReckless(m):
                multiplier = (multiplier*4915/4096)
        
        
        #SHEER FORCE
        if not condition.z and not ((condition.self_dmax and not atk_pokemon==condition.pokemon) or (condition.opp_dmax and atk_pokemon==condition.pokemon)):
            if atk_pokemon.ability.identifier=="sheer-force" and  self.affectedBySheerForce(m):
                multiplier = (multiplier*5325/4096)

        
        #TOUGH CLAWS
        if not condition.z and not ((condition.self_dmax and not atk_pokemon==condition.pokemon) or (condition.opp_dmax and atk_pokemon==condition.pokemon)):
            if atk_pokemon.ability.identifier=="tough-claws" and  self.affected_by_tough_claws(m):
                multiplier = (multiplier*5325/4096)
            
        
        #FAIRY/DARK AURA
        if (condition.dark_aura and m.get_attack_type().identifier=="dark") or (condition.fairy_aura and m.get_attack_type().identifier=="fairy"):
            multiplier = (multiplier*5448/4096)
        
        
        #TECHNICIAN
        if m.power*multiplier/4096 <= 60 and atk_pokemon.ability.identifier=="technician":
            multiplier = (multiplier*6144/4096)

        
        #FLARE BOOST
        if atk_pokemon.ability.identifier=="flare-boost" and m.damage_class_id==3 and atk_pokemon.status=="Burn":
            multiplier = (multiplier*6144/4096)
    
        
        #TOXIC BOOST
        if atk_pokemon.ability.identifier=="toxic-boost" and m.damage_class_id==2 and (atk_pokemon.status=="Toxic" or atk_pokemon.status=="Poison"):
            multiplier = (multiplier*6144/4096)

        
        #DRAGON'S MAW
        if atk_pokemon.ability.identifier=="dragons-maw" and m.get_attack_type().identifier=="dragon":
            multiplier = (multiplier*6144/4096)
        
        
        #TRANSISTOR
        if atk_pokemon.ability.identifier=="transistor" and m.get_attack_type().identifier=="electric":
            multiplier = (multiplier*6144/4096)
        
        
        #STRONG JAW
        if not condition.z and not ((condition.self_dmax and not atk_pokemon==condition.pokemon) or (condition.opp_dmax and atk_pokemon==condition.pokemon)):
            if atk_pokemon.ability.identifier=="strong-jaw" and  self.affected_by_strong_jaw(m):
                multiplier = (multiplier*6144/4096)

        
        
        #MEGA LAUNCHER
        if not condition.z and not ((condition.self_dmax and not atk_pokemon==condition.pokemon) or (condition.opp_dmax and atk_pokemon==condition.pokemon)):
            if atk_pokemon.ability.identifier=="mega-launcher" and self.affected_by_mega_launcher(m):
                multiplier = (multiplier*6144/4096)

        
        #HEATPROOF
        if def_pokemon.ability.identifier=="heatproof" and m.get_attack_type().identifier=="fire" and not self.ignores_abilities(atk_pokemon):
            multiplier = (multiplier*2048/4096)

        
        #DRY SKIN
        if def_pokemon.ability.identifier=="dry-skin" and m.get_attack_type().identifier=="fire":
            multiplier = (multiplier*5120/4096)


        #MUSCLE BAND/WISE GLASSES
        if (atk_pokemon.item and ((atk_pokemon.item.identifier=="wise-glasses" and m.damage_class_id==3) or (atk_pokemon.item.identifier=="muscle-band" and m.damage_class_id==2))):
            multiplier = (multiplier*4505/4096)
        
        
        #TYPE BOOSTING ITEM
        if not condition.item_consumed:
            if m.get_attack_type().identifier=="ground" and (atk_pokemon.item and (atk_pokemon.item.identifier=="soft-sand" or atk_pokemon.item.identifier=="earth-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="normal" and (atk_pokemon.item and (atk_pokemon.item.identifier=="silk-scarf" or atk_pokemon.item.identifier=="polkadot-bow" or atk_pokemon.item.identifier=="pink-bow")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="fire" and (atk_pokemon.item and (atk_pokemon.item.identifier=="charcoal" or atk_pokemon.item.identifier=="flame-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="fighting" and (atk_pokemon.item and (atk_pokemon.item.identifier=="black-belt" or atk_pokemon.item.identifier=="fist-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="ice" and (atk_pokemon.item and (atk_pokemon.item.identifier=="never-melt-ice" or atk_pokemon.item.identifier=="icicle-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="dragon" and (atk_pokemon.item and (atk_pokemon.item.identifier=="dragon-fang" or atk_pokemon.item.identifier=="draco-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="ghost" and (atk_pokemon.item and (atk_pokemon.item.identifier=="spell-tag" or atk_pokemon.item.identifier=="spooky-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="bug" and (atk_pokemon.item and (atk_pokemon.item.identifier=="silver-powder" or atk_pokemon.item.identifier=="insect-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="grass" and (atk_pokemon.item and (atk_pokemon.item.identifier=="miracle-seed" or atk_pokemon.item.identifier=="meadow-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="steel" and (atk_pokemon.item and (atk_pokemon.item.identifier=="metal-coat" or atk_pokemon.item.identifier=="iron-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="psychic" and (atk_pokemon.item and (atk_pokemon.item.identifier=="twisted-spoon" or atk_pokemon.item.identifier=="mind-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="flying" and (atk_pokemon.item and (atk_pokemon.item.identifier=="sharp-beak" or atk_pokemon.item.identifier=="sky-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="water" and (atk_pokemon.item and (atk_pokemon.item.identifier=="mystic-water" or atk_pokemon.item.identifier=="splash-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="poison" and (atk_pokemon.item and (atk_pokemon.item.identifier=="poison-barb" or atk_pokemon.item.identifier=="toxic-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="rock" and (atk_pokemon.item and (atk_pokemon.item.identifier=="hard-stone" or atk_pokemon.item.identifier=="stone-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="electric" and (atk_pokemon.item and (atk_pokemon.item.identifier=="magnet" or atk_pokemon.item.identifier=="zap-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="fairy" and (atk_pokemon.item and (atk_pokemon.item.identifier=="pixie-plate")):
                multiplier = (multiplier*4915/4096)
            elif m.get_attack_type().identifier=="dark" and (atk_pokemon.item and (atk_pokemon.item.identifier=="black-glasses" or atk_pokemon.item.identifier=="dread-plate")):
                multiplier = (multiplier*4915/4096)
            elif atk_pokemon.identifier=="dialga" and (m.get_attack_type().identifier=="steel" or m.get_attack_type().identifier=="dragon") and (atk_pokemon.item and atk_pokemon.item.identifier=="adamant-orb"):
                multiplier = (multiplier*4915/4096)
            elif atk_pokemon.identifier=="palkia" and (m.get_attack_type().identifier=="water" or m.get_attack_type().identifier=="dragon") and (atk_pokemon.item.identifier=="lustrous-orb"):
                multiplier = (multiplier*4915/4096)
            elif "giratina" in atk_pokemon.identifier and (m.get_attack_type().identifier=="ghost" or m.get_attack_type().identifier=="dragon") and (atk_pokemon.item.identifier=="griseous-orb"):
                multiplier = (multiplier*4915/4096)
            elif (atk_pokemon.identifier=="latios" or atk_pokemon.identifier=="latias") and (m.get_attack_type().identifier=="psychic" or m.get_attack_type().identifier=="dragon") and (atk_pokemon.item.identifier=="soul-dew"):
                multiplier = (multiplier*4915/4096)
            
            #GEMS
            elif condition.generation == 5:
                if m.get_attack_type().identifier=="dragon" and (atk_pokemon.item and atk_pokemon.item.identifier=="dragon-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True

                elif m.get_attack_type().identifier=="ground" and (atk_pokemon.item and atk_pokemon.item.identifier=="ground-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="fire" and (atk_pokemon.item and atk_pokemon.item.identifier=="fire-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="water" and (atk_pokemon.item and atk_pokemon.item.identifier=="water-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="electric" and (atk_pokemon.item and atk_pokemon.item.identifier=="electric-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="grass" and (atk_pokemon.item and atk_pokemon.item.identifier=="grass-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="ice" and (atk_pokemon.item and atk_pokemon.item.identifier=="ice-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="poison" and (atk_pokemon.item and atk_pokemon.item.identifier=="poison-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="normal" and (atk_pokemon.item and atk_pokemon.item.identifier=="normal-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="flying" and (atk_pokemon.item and atk_pokemon.item.identifier=="flying-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="psychic" and (atk_pokemon.item and atk_pokemon.item.identifier=="psychic-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="bug" and (atk_pokemon.item and atk_pokemon.item.identifier=="bug-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="rock" and (atk_pokemon.item and atk_pokemon.item.identifier=="rock-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="ghost" and (atk_pokemon.item and atk_pokemon.item.identifier=="ghost-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="dark" and (atk_pokemon.item and atk_pokemon.item.identifier=="dark-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
                elif m.get_attack_type().identifier=="steel" and (atk_pokemon.item and atk_pokemon.item.identifier=="steel-gem"):
                    multiplier = (multiplier*6144/4096)
                    condition.item_consumed=True
            elif m.get_attack_type().identifier=="normal" and (atk_pokemon.item and atk_pokemon.item.identifier=="normal-gem"):
                multiplier = (multiplier*5325/4096)
                condition.item_consumed=True

        #SOLAR BEAM/BLADE
        if (m.identifier=="solar-blade" or m.identifier=="solar-beam") and (condition.weather=="Rain" or condition.weather=="Sand" or condition.weather=="Hail" or condition.weather=="Heavy Rain"):
            multiplier = (multiplier*2048/4096)
        
        #KNOCK OFF
        if m.identifier=="knock-off" and (not condition.item_consumed and def_pokemon.item and self.can_knock_off_item(def_pokemon.item)):
            if not (("arceus" in def_pokemon.identifier or "silvally" in def_pokemon.identifier) and not def_pokemon.is_type("normal")):
                multiplier = (multiplier*6144/4096)
                condition.item_consumed=True

        
        #HELPING HAND
        if condition.helping_hand:
            multiplier = (multiplier*6144/4096)

        #CHARGE
        if condition.charge and m.get_attack_type().identifier=="electric":
            multiplier = (multiplier*8192/4096)        
        
        #BRINE
        if m.identifier=="brine" and condition.health < 50:
            multiplier = (multiplier*8192/4096)
        
        #FACADE
        if m.identifier=="facade" and atk_pokemon.status !="None":
            multiplier = (multiplier*8192/4096)
        
        #VENOSHOCK
        if m.identifier=="venoshock" and (atk_pokemon.status=="Poison") or atk_pokemon.status=="Toxic":
            multiplier = (multiplier*8192/4096)

        
        #----------------------------------------------------------------------
        #TODO: FUSION BOLT/FLARE
        #----------------------------------------------------------------------

        
        #TERRAINS
        if m.identifier=="terrain-pulse":
            if condition.terrain!="None":
                multiplier = (multiplier*8192/4096)
                if condition.terrain=="Grassy":
                    m.attack_type=self.get_type("grass")
                elif condition.terrain=="Misty":
                    m.attack_type=self.get_type("fairy")
                elif condition.terrain=="Electric":
                    m.attack_type=self.get_type("electric")
                elif condition.terrain=="psychic":
                    m.attack_type=self.get_type("psychic")
                
        if m.get_attack_type().identifier=="grass" and condition.terrain=="Grassy" and not self.is_pokemon_flying(atk_pokemon, condition):
            if condition.generation < 8:
                multiplier = (multiplier*6144/4096)
            else:
                multiplier = (multiplier*5325/4096)

        elif m.get_attack_type().identifier=="electric" and condition.terrain=="Electric" and not self.is_pokemon_flying(atk_pokemon, condition):
            if condition.generation < 8:
                multiplier = (multiplier*6144/4096)
            else:
                multiplier = (multiplier*5325/4096)
            if m.identifier=="rising-voltage":
                if not self.is_pokemon_flying(def_pokemon, condition):
                    multiplier = (multiplier*8192/4096)
        elif m.get_attack_type().identifier=="psychic" and condition.terrain=="Psychic" and self.is_pokemon_flying(atk_pokemon, condition):
            if condition.generation < 8:
                multiplier = (multiplier*6144/4096)

            else:
                multiplier = (multiplier*5325/4096)
            if m.identifier=="expanding-force":
                multiplier = (multiplier*6144/4096)
            
        elif (m.identifier=="earthquake" or m.identifier=="magnitude" or m.identifier=="bulldoze") and condition.terrain=="Grassy":
            multiplier = (multiplier*2048/4096)

        elif condition.terrain=="Misty" and m.get_attack_type().identifier=="dragon" and self.is_pokemon_flying(def_pokemon, condition):
            multiplier = (multiplier*2048/4096)

        if attacker_dmax:
            if m.get_attack_type().identifier=="fairy":
                condition.terrain="Misty"
            elif m.get_attack_type().identifier=="grass":
                condition.terrain="Grassy"
            if m.get_attack_type().identifier=="electric":
                condition.terrain="Electric"
            if m.get_attack_type().identifier=="psychic":
                condition.terrain="Psychic"
            
        
        #-----------------------------------------------------------
        #------------------TODO: MUD/WATER SPORTS-------------------
        #-----------------------------------------------------------
        #print(multiplier+" BP: "+basePower)
        basePower = self.poke_round(multiplier * basePower /  4096.0)
        #print(basePower)
        
        #------------------------------------------------------------------------------------
        #-----------------------------END BASE POWER------------------------------------------
        #------------------------------------------------------------------------------------
        return basePower




    def calculate_attack(self, condition, atk_pokemon, def_pokemon):
        m = condition.move
        basePower = m.power
        attack = 0
        multiplier = 4096
        attacker_dmax = (condition.opp_dmax and condition.pokemon==atk_pokemon) or (condition.self_dmax and condition.pokemon==def_pokemon)
        defender_dmax = (condition.self_dmax and condition.pokemon==atk_pokemon) or (condition.opp_dmax and condition.pokemon==def_pokemon)

        
        #------------------------------------------------------------------------------------
        #-----------------------------BEGIN ATTACK STATS-------------------------------------
        #------------------------------------------------------------------------------------
    
        
        if m.damage_class_id==2:
            attack = atk_pokemon.get_atk()
            defense = def_pokemon.get_def()
            if m.identifier=="body-press":
                attack = atk_pokemon.get_def()
            elif m.identifier=="foul-play":
                attack = def_pokemon.get_atk()
        
        if m.damage_class_id==3:
            attack = atk_pokemon.get_spa()
            defense = def_pokemon.get_spd()
            if m.identifier=="psyshock" or m.identifier=="psystrike" or m.identifier=="secret-sword":
                defense = def_pokemon.get_def()
            
        #UNAWARE, CRITS AND BOOSTS
        if def_pokemon.ability.identifier !="unaware" or (def_pokemon.ability.identifier=="unaware" and self.ignores_abilities(atk_pokemon)):
            if condition.critical:
                if atk_pokemon==condition.pokemon or (def_pokemon==condition.pokemon) and m.identifier=="foul-play":
                    attack = math.floor(attack *max(1, condition.opp_boost))
                else:
                    attack = math.floor(attack*max(1, condition.your_boost))
            else:
                if atk_pokemon==condition.pokemon or (def_pokemon==condition.pokemon) and m.identifier=="foul-play":
                    attack = math.floor(attack * condition.opp_boost)
                else:
                    attack = math.floor(attack* condition.your_boost)

        
        #HANDLE DROPS HERE
        change = 0
        if m.effect_id == 205:
            change = -2
        elif m.effect_id == 183:
            change = -1
        
        
        if atk_pokemon.ability.identifier=="contrary":
            change *= -1
        
        if not (atk_pokemon.item and atk_pokemon.item.identifier=="white-herb") and change < 0:
            if atk_pokemon==condition.pokemon:
                condition.changeOppBoost(change)
            
            else: 
                condition.changeYourBoost(change)
        return attack
            

    def get_attack_multiplier(self, condition, atk_pokemon, def_pokemon):

        m = condition.move
        attack_multiplier = 4096.0
        #HUSTLE
        if m.damage_class_id==2 and atk_pokemon.ability.identifier=="hustle":
            attack_multiplier = (attack_multiplier*6144/4096)
        
        
        #DEFEATIST/SLOW START
        if m.damage_class_id==2 and (atk_pokemon.ability.identifier=="slow-start" or (atk_pokemon.ability.identifier=="defeatist" and condition.health < 50)):
            attack_multiplier = (attack_multiplier*2048/4096)
        
        
        #FLOWER GIFT
        if condition.flower_gift and m.damage_class_id==2:
            attack_multiplier = (attack_multiplier*6144/4096)
        
        
        #GUTS
        if atk_pokemon.ability.identifier=="guts" and m.damage_class_id==2 and atk_pokemon.status != "Healthy":
            attack_multiplier = (attack_multiplier*6144/4096)
        
        
        #OVERGROW/BLAZE/TORRENT/SWARM
        if condition.health < 33.33 and ((atk_pokemon.ability.identifier=="overgrow" and m.get_attack_type().identifier=="grass") or (atk_pokemon.ability.identifier=="blaze" and m.get_attack_type().identifier=="fire") or (atk_pokemon.ability.identifier=="torrent" and m.get_attack_type().identifier=="water") or (atk_pokemon.ability.identifier=="swarm" and m.get_attack_type().identifier=="bug")):
            attack_multiplier = (attack_multiplier*6144/4096)
        
        
        #FLASH-FIRE
        if condition.flash_fire and m.get_attack_type().identifier=="fire":
            attack_multiplier = (attack_multiplier*6144/4096)
        
        
        #SOLAR-POWER
        if condition.weather=="Sun" and atk_pokemon.ability.identifier=="solar-power" and m.damage_class_id==3:
            attack_multiplier = (attack_multiplier*6144/4096)
        
        
        #----------------------------------------------------------------------
        #TODO: PLUS/MINUS
        #----------------------------------------------------------------------

        
        #STEELWORKER
        if atk_pokemon.ability.identifier=="steelworker" and m.get_attack_type().identifier=="steel":
            attack_multiplier = (attack_multiplier*6144/4096)
        
        #HUGE POWER/PURE POWER
        if atk_pokemon.ability.identifier=="huge-power" or atk_pokemon.ability.identifier=="pure-power"  and m.damage_class_id==2:
            attack_multiplier = (attack_multiplier*8192/4096)

        
        #WATER BUBBLE
        if atk_pokemon.ability.identifier=="water-bubble" and m.get_attack_type().identifier=="water":
            attack_multiplier = (attack_multiplier*8192/4096)
        
        
        #----------------------------------------------------------------------
        #TODO: STAKEOUT
        #----------------------------------------------------------------------

        #THICK FAT
        if def_pokemon.ability.identifier=="thick-fat" and (m.get_attack_type().identifier=="ice" or m.get_attack_type().identifier=="fire") and not self.ignores_abilities(atk_pokemon):
            attack_multiplier = (attack_multiplier*2048/4096)
    
        
        #WATER BUBBLE
        if def_pokemon.ability.identifier=="water-bubble" and m.get_attack_type().identifier=="fire" and not self.ignores_abilities(atk_pokemon):
            attack_multiplier = (attack_multiplier*2048/4096)
        
        
        #CHOICE BAND/SPECS
        if (atk_pokemon.item and (atk_pokemon.item.identifier=="choice-specs" and m.damage_class_id==3 or atk_pokemon.item.identifier=="choice-band" and m.damage_class_id==2)):
            attack_multiplier = (attack_multiplier*6144/4096)
        
        
        #ITEM-SPECIFIC
        if ("pikachu" in atk_pokemon.identifier and atk_pokemon.item and atk_pokemon.item.identifier=="light-ball") or (("marowak" in atk_pokemon.identifier or "cubone" in atk_pokemon.identifier) and (atk_pokemon.item and atk_pokemon.item.identifier=="thick-club" and m.damage_class_id == 2) or (atk_pokemon.identifier=="clamperl" and (atk_pokemon.item and atk_pokemon.item.identifier=="deep-sea-tooth" and m.damage_class_id == 3))):
            attack_multiplier = attack_multiplier*8192/4096
        
        return attack_multiplier
        


        attack = self.poke_round(attack * attack_multiplier/ 4096.0)
        
        
        #-------------------------------------------------------------------
        #-------------------------END ATTACK MULTIPLIER---------------------
        #-------------------------------------------------------------------

        #-------------------------------------------------------------------
        #-------------------------START DEFENSE MULTIPLIER------------------
        #-------------------------------------------------------------------        
        

    def calculate_defense(self, condition, atk_pokemon, def_pokemon):

        defense = 0
        m = condition.move
        if m.damage_class_id==2:
            defense = def_pokemon.get_def()
        
        if m.damage_class_id==3:
            defense = def_pokemon.get_spd()
            if m.identifier=="psyshock" or m.identifier=="psystrike" or m.identifier=="secret-sword":
                defense = def_pokemon.get_def()

        #UNAWARE
        #UNAWARE, CRITS AND BOOSTS
        if not atk_pokemon.ability.identifier=="unaware" or condition.move.identifier=="sacred-sword" or condition.move.identifier=="chip-away":
            if condition.critical:
                if def_pokemon==condition.pokemon:
                    defense=  math.floor(defense *min(1, condition.opp_boost))
                else:
                    defense =  math.floor(defense*min(1, condition.your_boost))
                
            else:
                if def_pokemon==condition.pokemon:
                    defense =  math.floor(defense* condition.opp_boost)
                else:
                    defense =  math.floor(defense* condition.your_boost)


        #SAND AND ROCK
        if def_pokemon.is_type("rock") and condition.weather=="Sand":
            defense = self.poke_round(defense * 6144/4096.0)

        return defense


    def get_defense_multiplier(self, condition, atk_pokemon, def_pokemon):
        defense_multiplier = 4096
        
        #FLOWER GIFT
        if condition.flower_gift and not self.is_move_physical(condition.move):
            defense_multiplier = defense_multiplier * 6144/4096
        
        
        #GRASS PELT
        if condition.terrain=="Grassy" and def_pokemon.ability.identifier=="grass-pelt" and self.is_move_physical(condition.move) and not self.ignores_abilities(atk_pokemon):
            defense_multiplier = defense_multiplier * 6144/4096
        
        
        #MARVEL SCALE
        if def_pokemon.ability.identifier=="marvel-scale" and self.is_move_physical(condition.move) and not def_pokemon.status=="Healthy" and not self.ignores_abilities(atk_pokemon):
            defense_multiplier = defense_multiplier * 6144/4096
        
        
        #FUR COAT
        if def_pokemon.ability.identifier=="fur-coat" and self.is_move_physical(condition.move) and not self.ignores_abilities(atk_pokemon):
            defense_multiplier = defense_multiplier * 8192/4096
        
        
        #---------------NEEDS WORK----------------------------
        #EVIOLITE 
        if def_pokemon.item and def_pokemon.item.identifier=="eviolite":
            defense_multiplier = defense_multiplier * 6144/4096
        
        
        #ASSAULT VEST
        if def_pokemon.item and def_pokemon.item.identifier=="assault-vest" and not self.is_move_physical(condition.move):
            defense_multiplier = defense_multiplier * 6144/4096
        
        
        #DEEP SEA SCALE
        if def_pokemon.item and def_pokemon.item.identifier=="deep-sea-scale" and not self.is_move_physical(condition.move) and def_pokemon.identifier=="clamperl":
            defense_multiplier = defense_multiplier * 8192/4096
        
        
        #METAL POWDER
        if def_pokemon.item and def_pokemon.item.identifier=="metal-powder" and self.is_move_physical(condition.move) and def_pokemon.identifier=="ditto":
            defense_multiplier = defense_multiplier * 8192/4096
        
        return defense_multiplier
        
        defense =  self.poke_round(defense * defense_multiplier/4096.0)
        
        #print("Defense/SpD: "+defense+" Multiplier: "+defense_multiplier)
        #-------------------------------------------------------------------
        #-------------------------END DEFENSE MULTIPLIER--------------------
        #-------------------------------------------------------------------
        
        if attacker_dmax and m.get_attack_type().identifier=="rock":
            condition.weather="Sand"
        
    def calculate_level_1(self, condition, atk_pokemon, def_pokemon):

        return math.floor(2*atk_pokemon.level/5+2)

        level2 =  math.floor(level1*basePower*attack/defense)
        print(f'{level1} BP: {basePower} DEFMULT: {defense_multiplier} Level 2: {level2} Def: {defense } Atk: {attack}')

        level3 =  math.floor(level2/50)
        #print(level3+2)

        return level3+2
    

    def calculate_final_damage(self, condition, pokemon, level1, base_power, attack, defense, final_modifier, type_modifier):
        # print(defense, attack)
        base_damage= (math.floor(math.floor(level1*base_power*attack/defense)/50)+2)
        # print("Line 928", base_damage, " BASE")
        m = condition.move
        if m.damage_class_id==1:
            return 0
        atk_pokemon=None
        def_pokemon=None
        if condition.cond=="Survive" or condition.cond=="Survive 2":
            def_pokemon = pokemon
            atk_pokemon = condition.pokemon
        else:
            def_pokemon = condition.pokemon
            atk_pokemon = pokemon


        # print(base_damage)
        
        #General modifiers
        
        if condition.is_doubles and (m.target_id!=10 or (m.identifier=="expanding-force" and condition.terrain=="Psychic")):
            base_damage = self.poke_round(base_damage*3072.0/4096)
            # print("Line 948", base_damage, "doubles")

        
        
        #----------------------------------------------------------------------
        #TODO: parental bond
        #----------------------------------------------------------------------


        #WEATHER BOOSTS/DROPS
        if condition.weather=="Sun":
            if m.is_type("fire"):
                base_damage = self.poke_round(base_damage*6144.0/4096)
            elif m.is_type("water"):
                base_damage = self.poke_round(base_damage*2048.0/4096)
        elif condition.weather=="Rain":
            if m.is_type("water"):
                base_damage = self.poke_round(base_damage*6144.0/4096)
            elif m.is_type("fire"):
                base_damage = self.poke_round(base_damage*2048.0/4096)
        # else:
            # print("Line 969", "no weather")
        
        #BATTLE ARMOR/SHELL ARMOR
        if condition.critical and not (def_pokemon.ability.identifier=="battle-armor" or def_pokemon.ability.identifier=="shell-armor") and not self.ignores_abilities(atk_pokemon):
            if condition.generation >= 6:
                base_damage = self.poke_round(base_damage*6144.0/4096)
            else:
                base_damage = self.poke_round(base_damage*8192.0/4096)
            print("Line 977: Critical")
        
        #RANDOM FACTOR.
        if condition.cond=="OHKO" or condition.cond=="2HKO":
            base_damage =  math.floor(base_damage*0.85)
        
        #STAB
        if atk_pokemon.is_type(m.get_attack_type().identifier):
            if atk_pokemon.ability.identifier=="adaptability":
                base_damage = self.poke_round(base_damage * 8192 / 4096.0)
            else:
                base_damage = self.poke_round(base_damage*6144/4096.0)
            # print("Line 988", base_damage, "STAB")


        if type_modifier > 1.1:
            base_damage = base_damage << 1
            if type_modifier > 3:
                base_damage = base_damage << 1
            # print("Line 995", base_damage, "effective")


        elif type_modifier < 0.9:
            base_damage = base_damage >> 1
            if type_modifier < 0.4:
                base_damage = base_damage >> 1
            # print("Line 1002", base_damage, "not effective")

        return base_damage*final_modifier/4096
    


    def check_berry_usage(self, def_pokemon, c, health):
        if not c.item_consumed and health > 0:
            if def_pokemon.item and def_pokemon.item.identifier=="sitrus-berry":
                if health/def_pokemon.get_HP() <= 0.5:
                    if def_pokemon.ability.identifier=="ripen":
                        health += max(1, math.floor(def_pokemon.get_HP()/2))
                    else:
                        health += max(1, math.floor(def_pokemon.get_HP()/4))
                        if def_pokemon.ability.identifier=="cheek-pouch":
                            health += max(1, math.floor(def_pokemon.get_HP()/3))
                    c.item_consumed=True
            elif def_pokemon.item and (def_pokemon.item.identifier=="wiki-berry" or def_pokemon.item.identifier=="aguav-berry" or def_pokemon.item.identifier=="iapapa-berry" or def_pokemon.item.identifier=="mago-berry" or def_pokemon.item.identifier=="figy-berry"):
                if c.generation == 8:
                    if health/def_pokemon.get_HP() <= 0.25 or (health/def_pokemon.get_HP() <= 0.5 and def_pokemon.ability.identifier=="gluttony"):
                        health += max(1, math.floor(def_pokemon.get_HP()/3))
                        if def_pokemon.ability.identifier=="cheek-pouch":
                            health += max(1, math.floor(def_pokemon.get_HP()/3))
                        elif def_pokemon.ability.identifier=="ripen":
                            health += max(1, math.floor(def_pokemon.get_HP()/3*2))
                        c.item_consumed=True
                elif c.generation == 7:
                    if health/def_pokemon.get_HP() <= 0.25 or (health/def_pokemon.get_HP() <= 0.5 and def_pokemon.ability.identifier=="gluttony"):
                        health += max(1, math.floor(def_pokemon.get_HP()/2))
                        if def_pokemon.ability.identifier=="cheek-pouch":
                            health += max(1, math.floor(def_pokemon.get_HP()/3))
                        c.item_consumed=True
                elif c.generation <= 6:
                    if health/def_pokemon.get_HP() <= 0.5:
                        health += max(1, math.floor(def_pokemon.get_HP()/8))
                        if def_pokemon.ability.identifier=="cheek-pouch":
                            health += max(1, math.floor(def_pokemon.get_HP()/3))
                        c.item_consumed=True
        return health

    
    def get_max_name(self, t):
        type_name= ["normal", "psychic", "ghost", "dark", "fairy", "steel", "fire", "water", "grass", "flying", "electric", "ground", "ice", "rock", "fighting", "bug", "poison", "dragon"]
        max_name = ["max-strike", "max-mindstorm", "max-phantasm", "max-darkness", "max-starfall", "max-steelspike", "max-flare", 
                "max-geyser", "max-overgrowth", "max-airstream", "max-lightning", "max-quake", "max-hailstorm", "max-rockfall", "max-knuckle", "max-ooze", "max-wyrmwind"]
        for i in range(len(type_name)):
            if type_name[i]==t.identifier:
                return max_name[i]
        return ""
    

    def get_z_name(self, t):
        type_name= ["normal", "psychic", "ghost", "dark", "fairy", "steel", "fire", "water", "grass", "flying", "electric", "ground", "ice", "rock", "fighting", "bug", "poison", "dragon"]
        z_name = ["breakneck-blitz", "shattered-psyche", "never-ending-nightmare", "black-hole-eclipse", "twinkle-tackle", "corkscrew-crash", "inferno-overdrive", 
                "hydro-vortex", "bloom-doom", "supersonic-skystrike", "gigavolt-havoc", "tectonic-rage", "subzero-slammer", "continental-crush", "all-out-pummeling", "acid-downpour", "devastating-drake"]
        for i in range(len(type_name)):
            if type_name[i]==t.identifier:
                return z_name[i]
        return ""
    

    def get_type_effectiveness(self, condition, def_pokemon):

        m = condition.move
        modifier = 1
        
        modifier = def_pokemon.get_effectiveness_from(m.get_attack_type())
        
        if condition.generation <= 5 and (def_pokemon.is_type("steel") and (m.get_attack_type().identifier=="ghost") or m.get_attack_type().identifier=="dark"):
            modifier /= 2.0

        
        #FREEZE DRY
        if m.identifier=="freeze-dry" and def_pokemon.is_type("water"):
            modifier = modifier * 4
        
        
        #FLYING TYPES, SMACK DOWN/GRAVITY/LEVITATE
        if (condition.gravity or condition.smack_down) and (def_pokemon.is_type("flying") or (def_pokemon.ability.identifier=="levitate" and not self.ignores_abilities(atk_pokemon)) and m.get_attack_type().identifier=="ground"):
            modifier = 1
            for t in def_pokemon.types:
                if not t.is_typeName("flying"):
                    modifier *= t.get_effectiveness_from(m.get_attack_type())/100.0

        
        #THOUSAND ARROWS
        elif (m.identifier=="thousand-arrows" or (def_pokemon.item and def_pokemon.item.identifier=="iron-ball")) and def_pokemon.is_type("flying"):
            modifier = 1.0
            if m.identifier=="thousand-arrows":
                condition.smack_down=True

        
        #LEVITATE
        elif def_pokemon.ability.identifier=="levitate" and m.get_attack_type().identifier=="ground" and not m.identifier=="thousand-arrows" and not self.ignores_abilities(atk_pokemon):
            modifier = 0
        
        return modifier


        
        #----------------------------------------------------------------------
        #TODO: Other interactions with typing.
        #----------------------------------------------------------------------

    
    def get_final_modifier(self, condition, atk_pokemon, def_pokemon, modifier):
        
        m = condition.move
        final_modifier = 4096
        
        if condition.screens:
            if condition.is_doubles:
                final_modifier = final_modifier*2732/4096
            else:
                final_modifier = final_modifier*2048/4096
            
        
        #NEUROFORCE
        if(atk_pokemon.ability.identifier=="neuroforce") and modifier > 1.1:
            final_modifier = final_modifier*5120/4096
        
        
        #SNIPER
        if(atk_pokemon.ability.identifier=="sniper") and condition.critical:
            final_modifier = final_modifier*6144/4096

        
        #TINTED LENS
        if (atk_pokemon.ability.identifier=="tinted-lens") and modifier < 0.9:
            final_modifier = final_modifier*8192/4096
        
        
        #MULTISCALE
        if (def_pokemon.ability.identifier=="multiscale" or def_pokemon.ability.identifier=="shadow-shield") and  (condition.health)==100 and not self.ignores_abilities(atk_pokemon):
            final_modifier = final_modifier * 2048/4096
        
        
        if (atk_pokemon.status=="Burn" and m.damage_class_id==2) and not m.identifier=="facade":
            if not atk_pokemon.ability.identifier=="guts":
                final_modifier = final_modifier * 2048/4096

        
        #FLUFFY (CONTACT)
        if self.affected_by_tough_claws(m) and def_pokemon.ability.identifier=="fluffy" and not self.ignores_abilities(atk_pokemon):
            final_modifier = final_modifier * 2048/4096


        
        #FRIEND GUARD
        if condition.friend_guard:
            final_modifier = final_modifier*3072/4096

        
        
        #SOLID ROCK
        if (def_pokemon.ability.identifier=="solid-rock" or def_pokemon.ability.identifier=="filter" or def_pokemon.ability.identifier=="prism-armor") and modifier > 1.1 and not self.ignores_abilities(atk_pokemon):
            final_modifier = final_modifier * 3072/4096

        
        #TODO: Metronome item
        
        #FLUFFY FIRE
        if (def_pokemon.ability.identifier=="fluffy" and m.get_attack_type().identifier=="fire") and not self.ignores_abilities(atk_pokemon):
            final_modifier = final_modifier * 8192/4096
        
        
        #EXPERT BELT
        if atk_pokemon.item and atk_pokemon.item.identifier=="expert-belt" and modifier > 1.1:
            final_modifier = final_modifier * 4915 / 4096
                
        
        #LIFE ORB
        if atk_pokemon.item and atk_pokemon.item.identifier=="life-orb":
            final_modifier = final_modifier * 5324/4096
        
        

        #resist berries
        if not condition.item_consumed:
            if m.get_attack_type().identifier=="fighting" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="chople-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="ice" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="yache-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="fire" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="occa-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="grass" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="rindo-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="electric" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="wacan-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="water" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="passho-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="steel" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="babiri-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="poison" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="kebia-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="ground" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="shuca-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="flying" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="coba-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="psychic" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="payapa-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="bug" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="tanga-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="rock" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="charti-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="ghost" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="kasib-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="dragon" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="haban-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="dark" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="colbur-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
            if m.get_attack_type().identifier=="normal" and def_pokemon.get_effectiveness_from(m.get_attack_type()) > 1.1 and def_pokemon.item and def_pokemon.item.identifier=="chilan-berry":
                final_modifier = final_modifier * 2048/4096
                condition.item_consumed=True
    
        return final_modifier
        
        #----------------------------------------------------------------------
        #TODO: double-damage situations, like Dig, Minimize and Dive
        #----------------------------------------------------------------------
        

        #Dmax Effects
        if attacker_dmax and condition.move.get_attack_type().identifier=="fire":
            condition.weather="Sun"
        elif attacker_dmax and condition.move.get_attack_type().identifier=="water":
            condition.weather="Rain"
        elif attacker_dmax and condition.move.get_attack_type().identifier=="ice":
            condition.weather="Hail"
        elif attacker_dmax and condition.move.get_attack_type().identifier=="ghost" and condition.move.damage_class_id==2:
            if condition.pokemon==atk_pokemon:
                condition.changeYourBoost(-1)
            else:
                condition.changeOppBoost(-1)
        elif attacker_dmax and condition.move.get_attack_type().identifier=="dark" and condition.move.damage_class_id==3:
            if condition.pokemon==atk_pokemon:
                condition.changeYourBoost(-1)
            else:
                condition.changeOppBoost(-1)
        elif attacker_dmax and condition.move.get_attack_type().identifier=="poison" and condition.move.damage_class_id==3: 
            if condition.pokemon==atk_pokemon:
                condition.changeOppBoost(1)
            else:
                condition.changeYourBoost(1)
        elif attacker_dmax and condition.move.get_attack_type().identifier=="fighting" and condition.move.damage_class_id==2:
            if condition.pokemon==atk_pokemon:
                condition.changeOppBoost(1)
            else:
                condition.changeYourBoost(1)
        return  (damage * final_modifier / 4096.0)
        

    
    def determine_order_of_stat(self, arr_to_insert_in, descriptor, conds, condList, condition_counter, orig_nature):
        stat_to_compare=0
        if not conds[0]:
            stat_to_compare = conds[1][descriptor]
        elif conds[1]:
            stat_to_compare = conds[0][descriptor]
        else:
            temp_stat0 = conds[0][descriptor]
            temp_stat1 = conds[1][descriptor]
            if temp_stat1 < temp_stat0:
                stat_to_compare = temp_stat1
            else:
                stat_to_compare = temp_stat0
        stor = {}
        stor["condition"] = condList[condition_counter]
        stor[descriptor] = stat_to_compare
        stor["with-orig-nature"] = conds[0]
        stor["allconds"] = conds
        self.place_into_array(arr_to_insert_in, stor, stat_to_compare, descriptor)

        
    def place_into_array(self, arr_to_insert_in, itemToPlace, valueToCompare, descriptor):
        pos = 0
        found = False
        while pos < len(arr_to_insert_in):
            if arr_to_insert_in[pos][descriptor] < valueToCompare:
                found = True
                arr_to_insert_in.insert(pos, itemToPlace)
                break
            pos+=1
        if not found:
            arr_to_insert_in.append(itemToPlace)

        
    def is_move_physical(self, m):
        if m.damage_class_id==2 or m.identifier=="psyshock" or m.identifier=="psystrike" or m.identifier=="secret-sword":
            return True
        return False
    
    
    def calculate_SR_damage(self, def_pokemon):
        rock = self.get_type("rock")
        modifier = def_pokemon.get_effectiveness_from(rock)
        modifier /= 8.0
        return math.floor(modifier*def_pokemon.get_HP())
        
    
    def is_move_multihit(self, m):
        moves = ["arm-thrust", "bone-rush", "bonemerang", "bullet-seed", "double-hit", "double-iron-bash", "double-kick", "dragon-darts", "dual-chop", "dual-wingbeat", 
                                    "fury-attack", "fury-swipes", "gear-grind", "icicle-spear", "pin-missile", "rock-blast", "scale-shot", "surging-strikes", "tail-slap", "triple-axel", "triple-kick", "water-shuriken"]
        return (m.identifier in moves)
    
        
    def calculate_speed(self, pokemon, boost, weather, terrain, tailwind):
        
        #TODO: boosts 
        
        base_speed = pokemon.get_speed()

        if pokemon.item and (pokemon.item.identifier=="iron-ball" or pokemon.item.identifier=="lax-incense"):
            base_speed =  (base_speed*2048/4096)
        elif pokemon.item and pokemon.item.identifier=="choice-scarf":
            base_speed =  (base_speed*6144/4096)
        if tailwind:
            base_speed = base_speed * 2
        if (weather=="Sun" and pokemon.ability.identifier=="chlorophyll") or (weather=="Rain" and pokemon.ability.identifier=="swift-swim") or (weather=="Sand" and pokemon.ability.identifier=="sand-rush") or (weather=="Hail" and pokemon.ability.identifier=="slush-rush") or (terrain=="Electric" and pokemon.ability.identifier=="surge-surfer"):
            base_speed = base_speed * 2
        return  math.floor(base_speed * boost)
    
    def heal_after_turn(self, def_pokemon, condition, current_hp):
        if not (def_pokemon.item and def_pokemon.item.identifier=="safety-goggles") or not def_pokemon.ability.identifier=="overcoat":
            if condition.weather=="Sand" and not (def_pokemon.ability.identifier=="sand-rush" or def_pokemon.ability.identifier=="sand-force" or def_pokemon.ability.identifier=="sand-veil"):
                if not (def_pokemon.is_type("rock") or def_pokemon.is_type("steel") or def_pokemon.is_type("ground")):
                    current_hp -= max(1, math.floor(def_pokemon.get_HP()/16))
            elif condition.weather=="Hail" and not (def_pokemon.ability.identifier=="slush-rush" or def_pokemon.ability.identifier=="snow-cloak"):
                if not (def_pokemon.is_type("ice")):
                    current_hp -= max(1, math.floor(def_pokemon.get_HP()/16))


        if def_pokemon.status=="Burn":
            if condition.generation < 7:
                if def_pokemon.ability.identifier=="heatproof":
                    current_hp -= max(1, math.floor(def_pokemon.get_HP()/16))
                else:
                    current_hp -= max(1, math.floor(def_pokemon.get_HP()/8))


            else:
                if def_pokemon.ability.identifier=="heatproof":
                    current_hp -= max(1, math.floor(def_pokemon.get_HP()/32))
                else:
                    current_hp -= max(1, math.floor(def_pokemon.get_HP()/16))



        elif def_pokemon.status=="Poison":
            if def_pokemon.ability.identifier=="poison-heal":
                current_hp += max(1, math.floor(def_pokemon.get_HP()/8))
            else:
                current_hp -= max(1, math.floor(def_pokemon.get_HP()/8))

        
        elif (def_pokemon.ability.identifier=="solar-power" or def_pokemon.ability.identifier=="dry-skin") and condition.weather=="Sun":
            current_hp -= max(1, math.floor(def_pokemon.get_HP()/8))
        
        
        elif def_pokemon.ability.identifier=="dry-skin" and condition.weather=="Rain":
            current_hp += max(1, math.floor(def_pokemon.get_HP()/8))
        
        
        elif def_pokemon.ability.identifier=="rain-dish" and condition.weather=="Rain":
            current_hp += max(1, math.floor(def_pokemon.get_HP()/16))
        
        
        if current_hp > 0:
        
            if condition.terrain=="Grassy":
                current_hp += max(1, math.floor(def_pokemon.get_HP()/16))
            
            if def_pokemon.item and def_pokemon.item.identifier=="leftovers":
                current_hp += max(1, math.floor(def_pokemon.get_HP()/16))
        
            elif def_pokemon.item and def_pokemon.item.identifier=="black-sludge":
                if def_pokemon.is_type("poison"):
                    current_hp += max(1, math.floor(def_pokemon.get_HP()/16))
                else:
                    current_hp -= max(1, math.floor(def_pokemon.get_HP()/16))
                
            elif def_pokemon.item and def_pokemon.item.identifier=="sticky-barb":
                current_hp -= max(1, math.floor(def_pokemon.get_HP()/16))
            
            current_hp = self.check_berry_usage(def_pokemon, condition, current_hp)
        return current_hp
        

    def calc_all_EVs(self, atks, defense, spas, spds, speed, orig, suggested, is_max_hp):
        total = 0
        results = [0,0,0,0,0,0,0]


        if len(atks) > 0:
            atk_map = atks[0]["with-orig-nature"]
            if not atk_map:
                atk_list = atks[0]["allconds"]
                atk_map = atk_list[1]
                if not atk_map:
                    atk_map = atk_list[0]
            atk = atk_map["attack"]
            total+=atk
            results[1] = atk
        else:
            results[1] = 0


        if len(spas) > 0:
            spa_map = spas[0]["with-orig-nature"]
            if not spa_map:
                spa_list =  spas[0]["allconds"]
                spa_map = spa_list[1]
                if not spa_map:
                    spa_map = spa_list[0]
            spa = spa_map["special-attack"]
            total+=spa
            results[3] = spa
        else:
            results[3] = 0
        
        
        if len(speed) > 0:
            speed_map = speed[0]["with-orig-nature"]
            if not speed_map:
                speed_list =  speed[0]["allconds"]
                speed_map = speed_list[1]
                if not speed_map:
                    speed_map = speed_list[0]
            speeeedd = speed_map["speed"]
            total+=speeeedd
            results[5] = speeeedd

        else:
            results[5] = 0

        
        if len(spds) > 0 and len(defense) > 0:
            spd_stack = spds[0]["with-orig-nature"]
            def_stack = defense[0]["with-orig-nature"]
            if not spd_stack:
                spd_list = spds[0]["allconds"]
                spd_stack = spd_list[1]
                if spd_stack == None:
                    spd_stack = spd_list[0]

            if def_stack == None:
                def_list = defense[0]["allconds"]
                def_stack = def_list[1]
                if def_stack == None:
                    def_stack = def_list[0]
        
            spd_hp=spd_stack[0]["hp"]
            def_hp=def_stack[0]["hp"]
            current_hp = max(spd_hp, def_hp)
            current_def = def_stack[0]["defense"]
            current_spd = spd_stack[0]["special-defense"]
            total_stat = current_hp+current_def+current_spd
            print(f"Line 1474 {current_hp} {current_spd} {current_def}")
            for i in range(len(spd_stack)):
                for j in range(len(def_stack)):
                    test_spd = spd_stack[i]["special-defense"]
                    test_hp = max(spd_stack[i]["hp"], def_stack[j]["hp"])
                    test_def = def_stack[j]["defense"]
                    print(f"Line 1480 Test: {test_hp} {test_spd} {test_def}")

                    if total_stat > test_def+test_hp+test_spd or (total_stat == test_def+test_hp+test_spd and current_hp < test_hp):
                        total_stat = test_def+test_hp+test_spd
                        current_hp = test_hp
                        current_spd = test_spd
                        current_def = test_def

            results[0] = current_hp
            results[2] = current_def
            results[4] = current_spd
            total += total_stat
            

        elif len(spds) > 0:
            spd_stack =  spds[0]["with-orig-nature"]
            if not spd_stack:
                spd_list =  spds[0]["allconds"]
                spd_stack = spd_list[1]
                if not spd_stack:
                    spd_stack = spd_list[0]

            
            current_hp = spd_stack[0]["hp"]
            current_spd = spd_stack[0]["special-defense"]
            total_stat = current_hp+current_spd

            for i in range(len(spd_stack)):
                test_spd = spd_stack[i]["special-defense"]
                test_hp = spd_stack[i]["hp"]
                if not is_max_hp:
                    if total_stat > test_hp+test_spd or (total_stat == test_hp+test_spd and current_hp < test_hp):
                        current_spd = test_spd
                        current_hp = test_hp
                        total_stat = test_hp+test_spd
                else:
                    if test_spd != current_spd:
                        break
                    else:
                        current_spd = test_spd
                        current_hp = test_hp


            results[0] = current_hp
            results[2] = 0
            results[4] = current_spd
            total+= total_stat

        
        elif len(defense) > 0:
            def_stack =  defense[0]["with-orig-nature"]
            if not def_stack:
                def_list =  defense[0]["allconds"]
                def_stack = def_list[1]
                if not def_stack:
                    def_stack = def_list[0]


            current_hp = def_stack[0]["hp"]
            current_def = def_stack[0]["defense"]
            total_stat = current_hp+current_def

            for i in range(len(def_stack)):
                test_def = def_stack[i]["defense"]
                test_hp = def_stack[i]["hp"]
                if not is_max_hp:
                    if total_stat > test_hp+test_def or (total_stat == test_hp+test_def and current_hp < test_hp):
                        current_def = test_def
                        current_hp = test_hp
                        total_stat = test_hp+test_def
                else:
                    if test_def != current_def:
                        break
                    else:
                        current_def = test_def
                        current_hp = test_hp

            results[0] = current_hp
            results[2] = current_def
            results[4] = 0
            total+= total_stat

        results[6] = total
        return results

    
    
    def summarize_condition(self, dPoke, c):
        summary = c.cond+" "
        if not c.raw_opp_boost=="0":
            summary = f'{summary}{c.raw_opp_boost} '

        if c.cond=="OHKO" or c.cond=="2HKO":
            summary = f'{summary}{c.pokemon.poke_stats[0].ev} HP '
            if self.is_move_physical(c.move):
                summary = f'{summary}{c.pokemon.poke_stats[2].ev}'
                if not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.increased_stat.stat.identifier=="defense":
                    summary = f'{summary}+ '
                elif not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.decreased_stat.stat.identifier=="defense":
                    summary = f'{summary}- '
                summary = f'{summary} Def '
            else:
                summary = f'{summary}{c.pokemon.poke_stats[4].ev}'
                if not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.increased_stat.stat.identifier=="special-defense":
                    summary = f'{summary}+ '
                elif not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.decreased_stat.stat.identifier=="special-defense":
                    summary = f'{summary}- '
                summary = f'{summary} SpD '

        elif c.cond=="Outspeed":
            summary = f'{summary}{c.pokemon.poke_stats[5].ev}'
            if not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.increased_stat.stat.identifier=="speed":
                summary +="+ "
            elif not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.decreased_stat.stat.identifier=="speed":
                summary +="- "

            summary = f'{summary} Speed '

        elif c.cond=="Survive" or c.cond=="Survive 2":
            if c.move.damage_class_id==2:
                summary = f'{summary}{c.pokemon.poke_stats[1].ev}'
                if not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.increased_stat.stat.identifier=="attack":
                    summary = f'{summary}+ '
                elif not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.decreased_stat.stat.identifier=="attack":
                    summary = f'{summary}- '
                summary = f'{summary} Atk '
            else:
                summary = f'{summary}{c.pokemon.poke_stats[3].ev}'
                if not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.increased_stat.stat.identifier=="special-attack":
                    summary = f'{summary}+ '
                elif not (c.pokemon.nature.increased_stat==c.pokemon.nature.decreased_stat) and c.pokemon.nature.decreased_stat.stat.identifier=="special-attack":
                    summary = f'{summary}- '
                summary = f'{summary} SpA '


        summary = f'{summary}{c.pokemon.ability.get_identifier_cleaned()}'

        if not (c.pokemon.item == None):
            summary = f'{summary} {c.pokemon.get_item_cleaned()} '
        
        summary = f'{summary}{c.pokemon.get_identifier_cleaned()}'
        
        if c.cond=="Outspeed":
            if c.your_tw:
                summary = f'{summary} in Tailwind'
            if c.foe_tw:
                summary = f'{summary} with opposing Tailwind'
        else:
            if c.cond=="OHKO" or c.cond=="2HKO":
                summary = f'{summary} with'
            if c.critical:
                summary = f'{summary} Crit '
            summary = f'{summary} {c.move.get_identifier_cleaned()}'
        if c.friend_guard:
            summary = f'{summary} with Friend Guard'
        if not c.terrain=="None":
            summary = f'{summary} in {c.terrain} Terrain'
        
        if not c.weather=="None":
            summary = f'{summary} in {c.weather}'
        if c.screens:
            summary = f'{summary} behind screens'
        if c.battery:
            summary = f'{summary} with Battery'
        if c.power_spot:
            summary = f'{summary} with Power Spot'
        return summary
    
    
    def calcDamageByMove(self, def_pokemon, c, dmg):
        damage = dmg
        if self.is_move_multihit(c.move):
            for hits in range(1, c.hits+1):
                if c.move.identifier=="triple-axel":
                    c.move.power=20*hits
                damage += self.calculate_damage(c, def_pokemon)
                if c.cond=="2HKO" or c.cond=="OHKO":
                    damage=self.check_berry_usage(c.pokemon, c, damage)
                else:
                    damage=self.check_berry_usage(def_pokemon, c, damage)
        else:
            damage += self.calculate_damage(c, def_pokemon)
        return damage
    
    
    def reset_condition(self, def_pokemon, c, orig_conds):
        for s in def_pokemon.poke_stats:
            s.ev=0

        c.item_consumed=False
        c.set_raw_boost(orig_conds["orig-boost"])
        c.set_opp_boost(orig_conds["opp-boost"])
        c.gravity= orig_conds["gravity"]
        c.smack_down =orig_conds["smack-down"]
        c.weather= orig_conds["weather"]
        c.terrain= orig_conds["terrain"]
    
    
    def calculate_EVs(self, def_pokemon, condition, is_max_hp):

        lists = []
        condition_list = []
        personality=""
        condition_ok = []
        for i in range(len(condition)):
            condition_ok.append(True)
        if not def_pokemon.nature:
            personality="undecided"
        else:
            personality = def_pokemon.nature.identifier
        nat = def_pokemon.nature
        
        for c in condition:
            orig_cond = {}
            orig_cond["orig-boost"] = c.raw_boost
            orig_cond["opp-boost"] = c.raw_opp_boost
            orig_cond["gravity"] = c.gravity
            orig_cond["smack-down"] = c.smack_down
            orig_cond["weather"] = c.weather
            orig_cond["terrain"] = c.terrain
            tObj = []
            natures = [None, None, None]
            c.summary =self.summarize_condition(def_pokemon, c)
            
            
            if not c.cond=="Outspeed":
                if c.z and c.generation == 7:
                    c.move.effectiveBP=(self.convert_to_z(c.move))


            #-----------------------------------------
            #----------OHKO/2HKO LOGIC----------------
            #-----------------------------------------
            if c.cond=="OHKO" or c.cond=="2HKO":


                if (personality=="undecided"):
                    if c.move.identifier=="body-press":
                        natures[1] = Nature.objects.get(identifier="relaxed")
                        natures[0] = Nature.objects.get(identifier="hardy")
                        natures[2] = Nature.objects.get(identifier="hasty")
                    
                    elif c.move.damage_class_id==2:
                        natures[1] = Nature.objects.get(identifier="adamant")
                        natures[0] = Nature.objects.get(identifier="hardy")
                        natures[2] = Nature.objects.get(identifier="modest")

                    else:
                        natures[1] = Nature.objects.get(identifier="modest")
                        natures[0] = Nature.objects.get(identifier="hardy")
                        natures[2] = Nature.objects.get(identifier="adamant")

                else:
                    if c.move.identifier=="body-press":
                        natures[0] = nat
                        if(nat.increased_stat==nat.decreased_stat):
                            natures[1] = Nature.objects.get(identifier="relaxed")
                            natures[2] = Nature.objects.get(identifier="hasty")
                        
                        elif nat.increased_stat.stat.identifier=="defense":
                            natures[1] = Nature.objects.get(identifier="hardy")
                            natures[2] = Nature.objects.get(identifier="hasty")
                        
                        elif nat.decreased_stat.stat.identifier=="defense":
                            natures[1] = Nature.objects.get(identifier="relaxed")
                            natures[2] = Nature.objects.get(identifier="hardy")
                        
                        else:
                            natures[1] = Nature.objects.get(identifier="relaxed")
                            natures[2] = Nature.objects.get(identifier="hasty")


                    else:
                        natures[0] = nat
                        if(nat.increased_stat==nat.decreased_stat):
                            natures[1] = Nature.objects.get(identifier="adamant")
                            natures[2] = Nature.objects.get(identifier="modest")
                        
                        elif c.move.damage_class_id==2:
                            
                            if nat.increased_stat.stat.identifier=="attack":
                                natures[1] = Nature.objects.get(identifier="hardy")
                                natures[2] = Nature.objects.get(identifier="modest")
                            
                            elif nat.decreased_stat.stat.identifier=="attack":
                                natures[1] = Nature.objects.get(identifier="adamant")
                                natures[2] = Nature.objects.get(identifier="hardy")
                            
                            else:
                                natures[1] = Nature.objects.get(identifier="adamant")
                                natures[2] = Nature.objects.get(identifier="modest")
                            

                        else:
                            if nat.increased_stat.stat.identifier=="special-attack":
                                natures[1] = Nature.objects.get(identifier="hardy")
                                natures[2] = Nature.objects.get(identifier="adamant")
                            
                            elif nat.decreased_stat.stat.identifier=="special-attack":
                                natures[1] = Nature.objects.get(identifier="modest")
                                natures[2] = Nature.objects.get(identifier="hardy")
                            
                            else:
                                natures[1] = Nature.objects.get(identifier="adamant")
                                natures[2] = Nature.objects.get(identifier="modest")

                base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                attack = self.calculate_attack(c, def_pokemon, c.pokemon)
                defense = self.calculate_defense(c, def_pokemon, c.pokemon)
                attack_modifier = self.get_attack_multiplier(c, def_pokemon, c.pokemon)
                defense_modifier = self.get_defense_multiplier(c, def_pokemon, c.pokemon)
                type_modifier = self.get_type_effectiveness(c, c.pokemon)
                final_modifier = self.get_final_modifier(c, def_pokemon, c.pokemon, type_modifier)
                level1 = self.calculate_level_1(c, def_pokemon, c.pokemon)

                sr_damage = 0
                if c.stealth_rock:
                    sr_damage = self.calculate_SR_damage(c.pokemon)
                
                type_modifier_2 = type_modifier 
                final_modifier_2 = final_modifier
                attack_modifier_2 = attack_modifier
                if c.cond == "2HKO" or c.hits > 1:
                    type_modifier_2 = self.get_type_effectiveness(c, c.pokemon)
                    final_modifier_2 = self.get_final_modifier(c, def_pokemon, c.pokemon, type_modifier_2)
                    attack_modifier_2 = self.get_attack_multiplier(c, def_pokemon, c.pokemon)
                hp_defender = c.pokemon.get_HP()*c.health/100
                for j in range(3):
                    n = natures[j]
                    def_pokemon.nature=n
                    found = False

                    for i in range(0, 252, 4):
                        self.reset_condition(def_pokemon, c, orig_cond)
                        if c.move.damage_class_id==2:
                            if c.move.identifier=="body-press":
                                def_pokemon.poke_stats[2].ev=i
                            else:
                                def_pokemon.poke_stats[1].ev=i
                        elif c.move.damage_class_id==3:
                            def_pokemon.poke_stats[3].ev=i
                        
                        dmg = sr_damage
                        print (f"Line 1824 BP:{base_power} DEF:{defense} DEFMOD:{defense_modifier} ATK:{attack} ATKMOD:{attack_modifier} FINMOD:{final_modifier} TYPEMOD: {type_modifier}")                                    
                        print (f"Line 1825 BP:{base_power} DEF:{defense} DEFMOD:{defense_modifier} ATK:{attack} ATKMOD:{attack_modifier_2} FINMOD:{final_modifier_2} TYPEMOD: {type_modifier}")                                    
                        if c.opp_dmax and c.generation == 8:
                            dmg *= 2
                        
                        for h in range(max(1, c.hits)):
                            attack = self.calculate_attack(c, def_pokemon, c.pokemon)
                            if h == 1:
                                dmg += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier/4096), self.poke_round(defense*defense_modifier/4096), final_modifier, type_modifier)
                            else:
                                if c.move.identifier == 'triple-axel':
                                    c.move.effectiveBP = 20 * h
                                    base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                dmg += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)
                            print("Line 1837", dmg, attack)

                            if max(1, c.hits) > 1:
                                dmg = self.check_berry_usage(c.pokemon, c, dmg)
                        print("Line 1841", dmg, i)
                        if c.cond=="2HKO":
                            if c.generation == 8 and c.opp_dmax:
                                dmg =  (hp_defender*2) - self.heal_after_turn(def_pokemon, c,  (hp_defender) - dmg)
                            else:
                                dmg =  (hp_defender) - self.heal_after_turn(def_pokemon, c,  (hp_defender) - dmg)
                            for h in range(max(1, c.hits)):
                                attack = self.calculate_attack(c, def_pokemon, c.pokemon)
                                if c.move.identifier == 'triple-axel':
                                    c.move.effectiveBP = 20 * h
                                    base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                dmg += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)
                            

 

                        #print("Damage: "+dmg+" Healed: "+ ( (hp_defender-dmg) - self.heal_after_turn(c.pokemon, c,  (hp_defender-dmg)))+" Total: "+( (hp_defender-dmg)- (self.heal_after_turn(def_pokemon, c,  (hp_defender-dmg))-dmg))) 
                        #print("SpA: "+i+" Nature: "+n.get_identifier_cleaned())
                        if dmg >= hp_defender or (c.opp_dmax and dmg >= hp_defender*2 and c.generation == 8):
                            x = {}

                            if c.move.identifier=="body-press":
                                x["defense"] = i
                            elif c.move.damage_class_id==2:
                                x["attack"]= i
                            
                            else:
                                x["special-attack"]= i
                            x["nature"] = n
                            tObj.append(x)
                            found=True
                            break

                    if not found:
                        tObj.append(None)

                condition_list.append(tObj)
                
            #-----------------------------------------
            #----------OUTSPEED LOGIC-----------------
            #-----------------------------------------
            elif c.cond=="Outspeed":
                if(personality=="undecided"):
                    natures[1] = Nature.objects.get(identifier="jolly")
                    natures[0] = Nature.objects.get(identifier="hardy")
                    natures[2] = Nature.objects.get(identifier="quiet")
                
                else:
                    natures[0] = nat
                    if(nat.increased_stat==nat.decreased_stat):
                        natures[1] = Nature.objects.get(identifier="jolly")
                        natures[2] = Nature.objects.get(identifier="quiet")
                    
                    elif nat.increased_stat.stat.identifier=="speed":
                        natures[1] = Nature.objects.get(identifier="hardy")
                        natures[2] = Nature.objects.get(identifier="quiet")
                    
                    elif nat.decreased_stat.stat.identifier=="speed":
                        natures[1] = Nature.objects.get(identifier="jolly")
                        natures[2] = Nature.objects.get(identifier="hardy")
                    
                    else:
                        natures[1] = Nature.objects.get(identifier="jolly")
                        natures[2] = Nature.objects.get(identifier="quiet")

                for j in range(3):
                    n = natures[j]
                    def_pokemon.nature=(n)
                    found = False
                    for i in range(0, 252, 4):
                        self.reset_condition(def_pokemon, c, orig_cond)
                        def_pokemon.poke_stats[5].ev=i
                        speedA = self.calculate_speed(def_pokemon, c.your_boost, c.weather, c.terrain, c.your_tw) 
                        speedB = self.calculate_speed(c.pokemon, c.opp_boost, c.weather, c.terrain, c.foe_tw)
                        print(f"Line 1914 {speedA} {speedB}")

                        if speedA> speedB:
                            x = {}
                            x["speed"] = i
                            x["nature"] = n
                            tObj.append(x)
                            found = True
                            break
                    if not found:
                        tObj.append(None)

                condition_list.append(tObj)

            #-----------------------------------------
            #----------SURVIVE LOGIC------------------
            #-----------------------------------------
            else:
                if(personality=="undecided"):
                    if self.is_move_physical(c.move):
                        natures[1] = Nature.objects.get(identifier="impish")
                        natures[0] = Nature.objects.get(identifier="hardy")
                        natures[2] = Nature.objects.get(identifier="mild")
                    
                    else:
                        natures[1] = Nature.objects.get(identifier="calm")
                        natures[0] = Nature.objects.get(identifier="hardy")
                        natures[2] = Nature.objects.get(identifier="naive")

                else:
                    if(nat.increased_stat==nat.decreased_stat):
                        natures[0] = nat
                        if self.is_move_physical(c.move):
                            natures[1] = Nature.objects.get(identifier="impish")
                            natures[2] = Nature.objects.get(identifier="mild")
                        
                        else:
                            natures[1] = Nature.objects.get(identifier="calm")
                            natures[2] = Nature.objects.get(identifier="naive")

                    elif self.is_move_physical(c.move):
                        natures[0] = nat
                        if nat.increased_stat.stat.identifier=="defense":
                            natures[1] = Nature.objects.get(identifier="hardy")
                            natures[2] = Nature.objects.get(identifier="mild")
                        
                        elif nat.decreased_stat.stat.identifier=="defense":
                            natures[1] = Nature.objects.get(identifier="impish")
                            natures[2] = Nature.objects.get(identifier="hardy")
                        
                        else:
                            natures[1] = Nature.objects.get(identifier="impish")
                            natures[2] = Nature.objects.get(identifier="mild")
                        
                    
                    else:
                        natures[0] = nat
                        if nat.increased_stat.stat.identifier=="special-defense":
                            natures[1] = Nature.objects.get(identifier="hardy")
                            natures[2] = Nature.objects.get(identifier="naive")
                        
                        elif nat.decreased_stat.stat.identifier=="special-defense":
                            natures[1] = Nature.objects.get(identifier="calm")
                            natures[2] = Nature.objects.get(identifier="hardy")
                        
                        else:
                            natures[1] = Nature.objects.get(identifier="calm")
                            natures[2] = Nature.objects.get(identifier="naive")

                base_power = self.calculate_base_power(c, c.pokemon, def_pokemon)
                attack = self.calculate_attack(c, c.pokemon, def_pokemon)
                defense = self.calculate_defense(c, c.pokemon, def_pokemon)
                attack_modifier = self.get_attack_multiplier(c, c.pokemon, def_pokemon)
                defense_modifier = self.get_defense_multiplier(c, c.pokemon, def_pokemon)
                type_modifier = self.get_type_effectiveness(c, def_pokemon)
                final_modifier = self.get_final_modifier(c, c.pokemon, def_pokemon, type_modifier)
                level1 = self.calculate_level_1(c, c.pokemon, def_pokemon)


                type_modifier_2 = type_modifier
                final_modifier_2 = final_modifier
                attack_modifier_2 = attack_modifier
                defense_modifier_2 = defense_modifier
                if c.cond == "Survive 2" or c.hits > 1:
                    type_modifier_2 = self.get_type_effectiveness(c, def_pokemon)
                    final_modifier_2 = self.get_final_modifier(c, c.pokemon, def_pokemon, type_modifier_2)
                    attack_modifier_2 = self.get_attack_multiplier(c, c.pokemon, def_pokemon)
                    defense_modifier_2 = self.get_defense_multiplier(c, c.pokemon, def_pokemon)
                for i in range(3):
                    storage = []
                    print("Line 2004", storage, i)
                    found = False
                    maxHP = -1
                    def_pokemon.nature=natures[i]
                    for hp in range(0, 252, 4):
                        print("Line 2009", hp)
                        self.reset_condition(def_pokemon, c, orig_cond)
                        def_pokemon.poke_stats[0].ev=hp
                        damage = 0
                        if c.stealth_rock:
                            damage = self.calculate_SR_damage(def_pokemon)
                        
                        if c.self_dmax and c.generation == 8:
                            damage *= 2
                        
                        defense = self.calculate_defense(c, c.pokemon, def_pokemon)
                        for h in range(max(1, c.hits)):
                            if h == 1:
                                damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier/4096), self.poke_round(defense*defense_modifier/4096), final_modifier, type_modifier)
                            else:
                                if c.move.identifier == 'triple-axel':
                                    c.move.effectiveBP = 20 * h
                                    base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)

                            if max(1, c.hits) > 1:
                                damage = self.check_berry_usage(c.pokemon, c, damage)
                        
                        hp_poke = def_pokemon.get_HP()*c.health/100
                        print(f"Line 2033  T1: {damage} HP: {hp} Def: {0} Nature: {natures[i].get_identifier_cleaned()}")
                        if c.cond=="Survive 2":
                            if c.self_dmax and c.generation == 8:
                                damage =  (hp_poke*2) - self.heal_after_turn(def_pokemon, c,  (hp_poke*2) - damage)
                                # print("Pre-T2: "+damage)                            
                            else:
                                damage =  (hp_poke) - self.heal_after_turn(def_pokemon, c,  (hp_poke) - damage)
                                # print("Pre-T2: "+damage)
                            
                            for h in range(max(1, c.hits)):
                                if c.move.identifier == 'triple-axel':
                                    c.move.effectiveBP = 20 * h
                                    base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)
                                if max(1, c.hits) > 1:
                                    damage = self.check_berry_usage(c.pokemon, c, damage)
                        
                            # print("T2: "+damage)

                        print (f"Line 2052 BP:{base_power} HP:{hp_poke} INIT DMG:{damage} DEF:{defense} DEFMOD:{defense_modifier} ATK:{attack} ATKMOD:{attack_modifier} FINMOD:{final_modifier}")                                    
                        #print("HP: "+ hp+" Def/SpD: 0 Nature: "+natures[i].get_identifier_cleaned())
                        #print(c.pokemon.get_identifier_cleaned()+": "+ damage)
                        if damage < hp_poke or (c.self_dmax and c.generation == 8 and damage < hp_poke *2 ):
                            found = True
                            maxHP = hp
                            sx = {}
                            sx["hp"] = hp
                            sx["nature"] = natures[i]
                            if self.is_move_physical(c.move):
                                sx["defense"] = 0
                            else:
                                sx["special-defense"] = 0
                            storage.append(sx)
                            # print(f"HP: {hp} Def/SpD: {def_pokemon.poke_stats[2].ev}/{def_pokemon.poke_stats[4].ev} Nature: {natures[i].get_identifier_cleaned()} HP%: {def_pokemon.get_HP()} {c.health}")
                            # print(f"HP: {hp} Def/SpD: 0 Nature: {natures[i].get_identifier_cleaned()} HP%: {def_pokemon.get_HP()} {c.health}")
                            # print(f"{c.pokemon.get_identifier_cleaned()}: {damage}")
                            break

                    if found:
                        lastDef = 0
                        for hp in range(maxHP-4, -4, -4):
                            for defev in range(lastDef, 256, 4):
                                self.reset_condition(def_pokemon, c, orig_cond)
                                def_pokemon.poke_stats[0].ev=hp
                                # print("Line 2077", hp)
                                if self.is_move_physical(c.move):
                                    def_pokemon.poke_stats[2].ev=defev
                                
                                else:
                                    def_pokemon.poke_stats[4].ev=defev
                                
                                damage = 0
                                if c.stealth_rock:
                                    damage = self.calculate_SR_damage(def_pokemon)
                                
                                if c.self_dmax and c.generation == 8:
                                    damage *= 2
                                
                                defense = self.calculate_defense(c, c.pokemon, def_pokemon)
                                for h in range(max(1, c.hits)):
                                    if h == 1:
                                        damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier/4096), self.poke_round(defense*defense_modifier/4096), final_modifier, type_modifier)
                                    else:
                                        if c.move.identifier == 'triple-axel':
                                            c.move.effectiveBP = 20 * h
                                            base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                        damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)

                                    if max(1, c.hits) > 1:
                                        damage = self.check_berry_usage(c.pokemon, c, damage)


                                # print(f"T1: {damage} HP: {hp} Def: {defense} Nature: {natures[i].get_identifier_cleaned()}")
                                hp_poke = def_pokemon.get_HP()*c.health/100
                                if c.cond=="Survive 2":
                                    if c.self_dmax and c.generation == 8:
                                        damage =  (hp_poke*2) - self.heal_after_turn(def_pokemon, c,  (hp_poke*2) - damage)
                                    
                                    else:
                                        print("Line 2112", damage, hp_poke)
                                        damage =  (hp_poke) - self.heal_after_turn(def_pokemon, c,  (hp_poke) - damage)
                                        print("Line 2114", damage, hp_poke)

                                    for h in range(max(1, c.hits)):
                                        if c.move.identifier == 'triple-axel':
                                            c.move.effectiveBP = 20 * h
                                            base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                        damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)
                                        if max(1, c.hits) > 1:
                                            damage = self.check_berry_usage(c.pokemon, c, damage)
                                    
                                    # print("T2: "+damage)
                                # print (f"Line 2125 BP:{base_power} HP:{hp_poke} INIT DMG:{damage} DEF:{defense} DEFMOD:{defense_modifier} ATK:{attack} ATKMOD:{attack_modifier} FINMOD:{final_modifier}")                                    

                                # print("HP: "+ hp+" Def/SpD: "+def+" Nature: "+natures[i].get_identifier_cleaned())
                                # print(c.pokemon.get_identifier_cleaned()+": "+ damage)
                                if damage < hp_poke:
                                    lastDef = defev
                                    sx = {}
                                    sx["hp"] = hp
                                    sx["nature"] = natures[i]
                                    if self.is_move_physical(c.move):
                                        sx["defense"] = defev
                                    else:
                                        sx["special-defense"] = defev
                                    
                                    storage.append(sx)
                                    # print(f"HP: {hp} Def/SpD: {defev} Nature: {natures[i].get_identifier_cleaned()}")
                                    # print(f"{c.pokemon.get_identifier_cleaned()}: {damage}")
                                    break

                    else:
                        lastHp = 252
                        print("Line 2146")

                        for defev in range(0, 256, 4):
                            self.reset_condition(def_pokemon, c, orig_cond)
                            def_pokemon.poke_stats[0].ev=lastHp
                            print("Line 2151", lastHp, def_pokemon.poke_stats[0].ev, def_pokemon.get_HP())
                            if self.is_move_physical(c.move):
                                def_pokemon.poke_stats[2].ev=defev        
                            else:
                                def_pokemon.poke_stats[4].ev=defev
                            defense = self.calculate_defense(c, c.pokemon, def_pokemon)
                            damage = 0
                            if c.stealth_rock:
                                damage = self.calculate_SR_damage(def_pokemon)

                            if c.self_dmax and c.generation == 8:
                                damage *= 2

                            hp_poke = def_pokemon.get_HP()*c.health/100

                            for h in range(max(1, c.hits)):
                                if h == 1:
                                    damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier/4096), self.poke_round(defense*defense_modifier/4096), final_modifier, type_modifier)
                                else:
                                    if c.move.identifier == 'triple-axel':
                                        c.move.effectiveBP = 20 * h
                                        base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                    damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)

                                if max(1, c.hits) > 1:
                                    damage = self.check_berry_usage(c.pokemon, c, damage)
                            # print(f"T1: {damage} HP: {hp} Def: {defev} Nature: {natures[i].get_identifier_cleaned()}")
                            if c.cond=="Survive 2":
                                if c.self_dmax and c.generation == 8:
                                    damage =  (hp_poke*2) - self.heal_after_turn(def_pokemon, c,  (hp_poke*2) - damage)
                                    # print(f"Pre-T2: {damage}")
                                
                                else:
                                    print("Line 2184", damage, hp_poke)
                                    damage =  (hp_poke) - self.heal_after_turn(def_pokemon, c,  (hp_poke) - damage)
                                    print("Line 2186", damage, hp_poke)

                                    for h in range(max(1, c.hits)):
                                        if c.move.identifier == 'triple-axel':
                                            c.move.effectiveBP = 20 * h
                                            base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                        damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)
                                        if max(1, c.hits) > 1:
                                            damage = self.check_berry_usage(c.pokemon, c, damage)
                            print (f"Line 2195 BP:{base_power} HP:{hp_poke} INIT DMG:{damage} DEF:{defense} DEFMOD:{defense_modifier} ATK:{attack} ATKMOD:{attack_modifier} FINMOD:{final_modifier}")                                    
                            print("Line 2196", defev, lastHp, damage, hp_poke)

                            # print("HP: "+ hp+" Def/SpD: "+def+" Nature: "+natures[i].get_identifier_cleaned())
                            # print(c.pokemon.get_identifier_cleaned()+": "+ damage)
                            if damage < hp_poke:
                                for hp in range(lastHp, -4, -4):
                                    def_pokemon.poke_stats[0].ev=hp
                                    hp_poke = def_pokemon.get_HP()*c.health/100


                                    if c.cond== "Survive 2":
                                        self.reset_condition(def_pokemon, c, orig_cond)
                                        def_pokemon.poke_stats[0].ev=hp
                                        if self.is_move_physical(c.move):
                                            def_pokemon.poke_stats[2].ev=defev        
                                        else:
                                            def_pokemon.poke_stats[4].ev=defev
                                        defense = self.calculate_defense(c, c.pokemon, def_pokemon)
                                        damage = 0
                                        if c.stealth_rock:
                                            damage = self.calculate_SR_damage(def_pokemon)
                                        if c.self_dmax and c.generation == 8:
                                            damage *= 2

                                        for k in range(2):
                                            for h in range(max(1, c.hits)):
                                                if h == 1:
                                                    damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier/4096), self.poke_round(defense*defense_modifier/4096), final_modifier, type_modifier)
                                                else:
                                                    if c.move.identifier == 'triple-axel':
                                                        c.move.effectiveBP = 20 * h
                                                        base_power = self.calculate_base_power(c,def_pokemon, c.pokemon)
                                                    damage += self.calculate_final_damage(c, def_pokemon, level1, base_power, self.poke_round(attack*attack_modifier_2/4096), self.poke_round(defense*defense_modifier/4096), final_modifier_2, type_modifier_2)

                                                if max(1, c.hits) > 1:
                                                    damage = self.check_berry_usage(c.pokemon, c, damage)
                                            if k == 1:
                                                damage =  (hp_poke) - self.heal_after_turn(def_pokemon, c,  (hp_poke) - damage)

                                    print("Line 2237", damage, hp_poke, lastHp)
                                    if damage >= hp_poke:
                                        print("Line 2239", hp)
                                        if hp != 252:
                                            sx = {}
                                            sx["hp"] = hp+4
                                            sx["nature"] = natures[i]
                                            if self.is_move_physical(c.move):
                                                sx["defense"] = defev
                                            else:
                                                sx["special-defense"] = defev
                                            
                                            print(f"Line 2249 HP: {hp} Def/SpD: {defev} Nature: {natures[i].get_identifier_cleaned()}")
                                            print(f"Line 2250 {c.pokemon.get_identifier_cleaned()}: {damage}")
                                            storage.append(sx)
                                            lastHp = hp                         
                                            break
                                #End hp for loop
                            #End def for loop
                    print(storage)
                    if len(storage) == 0:
                        tObj.append(None)
                    else:
                        tObj.append(storage)
                    #End else for found hp.
                #End nature for loop
                condition_list.append(tObj)
            #End else for defense condition
        #End for loop for all conditions
        
        #FROM HERE: LOOP THROUGH AND FIGURE OUT APPROPRIATE LOCATION/STACK/ARRAY.
        
        suggestions = []
        condition_counter = 0
        boostOn = ""
        boosted = [False, False, False, False, False]
        boost = []
        conditionPossible = []
        hinder = []
        attacks = []
        defense = []
        spas = []
        spds = []
        speed = []
        for conds in condition_list:
            suggestion= {}

            if not conds[0] and not conds[1] and not conds[2]:
                condition_ok[condition_counter] = False

                suggestion["suggestion"] ="Not possible, consider changing items, or adding boosts"
                suggestion["possible"] = False
                conditionPossible.append(suggestion)
                boost.append(False)
                hinder.append(False)
            
            elif (not conds[0] and not conds[1]) or (not conds[1] and not conds[2]) or (not conds[0] and not conds[2]):
                suggestion["possible"] = True
                boost.append(True)
                hinder.append(False)
                conditionPossible.append(suggestion)
                if(condition[condition_counter].cond=="Outspeed") or condition[condition_counter].cond=="Underspeed":
                    boosted[4] = True
                
                elif condition[condition_counter].cond=="OHKO" or condition[condition_counter].cond=="2HKO" :
                    if condition[condition_counter].move.damage_class_id==3:
                        boosted[2] = True
                    elif condition[condition_counter].move.damage_class_id==2:
                        boosted[0] = True
                    else:
                        condition_ok[condition_counter] = False

                else:
                    if self.is_move_physical(condition[condition_counter].move):
                        boosted[1] = True
                    elif condition[condition_counter].move.damage_class_id==3:
                        boosted[3] = True
                    else:
                        condition_ok[condition_counter] = True


            elif (not conds[0] or not conds[1] or not conds[2]):
                suggestion["possible"] = True
                boost.append(False)
                hinder.append(False)
                conditionPossible.append(suggestion)

            else:
                suggestion["possible"] = True
                boost.append(False)
                hinder.append(True)
                conditionPossible.append(suggestion)
            if conditionPossible[condition_counter]["possible"]:

                if(condition[condition_counter].cond=="Outspeed") or condition[condition_counter].cond=="Underspeed":            
                    self.determine_order_of_stat(speed, "speed", conds, condition, condition_counter, personality)

                elif(condition[condition_counter].cond=="OHKO") or condition[condition_counter].cond=="2HKO":
                    if self.is_move_physical(condition[condition_counter].move):
                        self.determine_order_of_stat(attacks, "attack", conds, condition, condition_counter, personality)
                    else:
                        self.determine_order_of_stat(spas, "special-attack", conds, condition, condition_counter, personality)

                else:
                    stat_to_comp=""
                    arr_to_insert_in=None
                    if self.is_move_physical(condition[condition_counter].move):
                        stat_to_comp = "defense"
                        arr_to_insert_in = defense

                    else:
                        stat_to_comp = "special-defense"
                        arr_to_insert_in = spds

                    # print(f"{conds[0]} {conds[1]} {conds[2]}")
                    stat_to_compare = None
                    if not conds[0]:
                        print(conds[1], conds[0], conds[2])
                        ss = conds[1]
                        print(ss)

                        stat_to_compare = ss[0]["hp"] + ss[0][stat_to_comp]
                    elif not conds[1]:
                        ss = conds[0]
                        stat_to_compare = ss[0]["hp"] + ss[0][stat_to_comp]
                    else:
                        ss = conds[0]
                        sx = conds[1]

                        temp_stat0 = ss[0]["hp"] + ss[0][stat_to_comp]
                        temp_stat1 = sx[0]["hp"] + sx[0][stat_to_comp]
                        if temp_stat1 < temp_stat0:
                            stat_to_compare = temp_stat1
                        else:
                            stat_to_compare = temp_stat0


                    stor = {}
                    stor["condition"] = condition[condition_counter]
                    stor[stat_to_comp] = stat_to_compare
                    if conds[0]:
                        stor["with-orig-nature"] = conds[0] 
                    else:
                        stor["with-orig-nature"] = None
                    stor["allconds"] = conds
                    self.place_into_array(arr_to_insert_in, stor, stat_to_compare, stat_to_comp)

            
            condition_counter += 1
        #CREATED STACK OF POTENTIAL CANDIDATES
        
        
        #NOW FIGURE OUT IF THERE ARE ANY ISSUES (INCOMPATIBLE NATURES), IF SO WE REMOVE.
        count_boosts = sum([1 for b in boosted if b])
            
        
        stat_stack =[]
        stat_stack.append(attacks)
        stat_stack.append(defense)
        stat_stack.append(spas)
        stat_stack.append(spds)
        stat_stack.append(speed)
        nature_if_null=None
        if count_boosts > 1:
            original_boosted_stat = def_pokemon.nature
            stat_label = ["attack", "defense", "special-attack", "special-defense", "speed"]

            stat_boosted = None
            if original_boosted_stat and original_boosted_stat.decreased_stat !=original_boosted_stat.increased_stat:
                stat_boosted = original_boosted_stat.increased_stat.stat.identifier

            for i in range(5):
                if stat_label[i] != stat_boosted and boosted[i]:
                    sstack = stat_stack[i]
                    if stat_label[i]=="defense" or stat_label[i]=="special-defense":
                        all_conds = sstack[0]["allconds"]

                        while (len(all_conds[0]) == 0 or len(all_conds[1]) == 0):
                            condition_ok[condition.index(sstack[0]["condition"])] = False
                            sstack.pop(0)
                            all_conds = sstack[0]["allconds"]


                    else:
                        all_conds = sstack[0]["allconds"]
                        while not all_conds[0] or not all_conds[1]:
                            condition_ok[condition.index(sstack[0]["condition"])] = False
                            sstack.pop(0)
                            all_conds = sstack[0]["allconds"]


        if count_boosts >= 1:
            stat_label = ["attack", "defense", "special-attack", "special-defense", "speed"]
            lowered_stat = None
            boosted_stat=None
            candidate=None
            for i in range(len(boosted)):
                if boosted[i]:
                    boosted_stat = self.get_stat_by_name(stat_label[i])
                elif len(stat_stack[i]) == 0:
                    lowered_stat = self.get_stat_by_name(stat_label[i])
                elif len(stat_stack[i]) == 1:
                    candidate = self.get_stat_by_name(stat_label[i])

            if not lowered_stat:
                lowered_stat = candidate
            nature_if_null = self.get_nature_by_increase_and_decrease(boosted_stat, lowered_stat)
        else:
            nature_if_null = Nature.objects.get(identifier="hardy")
        
        #FOLLOW BY PICKING EVS, MINIMIZE, AND SEE IF IT IS OVER 508. IF SO REMOVE THE ONE WITH MOST EVS.
        res = []
        while True:            
            res = self.calc_all_EVs(attacks, defense, spas, spds, speed, nat, nature_if_null, is_max_hp)
            print(res)
            if res[6] > 508:
                highest = 0
                highestidx = 0
                if res[1] > highest:
                    highest = res[1]
                    highestidx = 1
                if res[3] > highest:
                    highest = res[3]
                    highestidx = 3
                if res[5] > highest:
                    highest = res[5]
                    highestidx = 5
                if res[2]+res[0] > highest*2:
                    highest = res[2]
                    highestidx = 2
                if res[0]+res[4]> highest*2:
                    highest=res[4]
                    highestidx=4
                if highestidx == 1: 
                    condition_ok[condition.index(attacks[0]["condition"])] = False
                    attacks.pop(0)
                    break
                elif highestidx == 2:
                    condition_ok[condition.index(defense[0]["condition"])] = False
                    defense.pop(0)
                    break
                elif highestidx == 3:
                    condition_ok[condition.index(spas[0]["condition"])] = False
                    spas.pop(0)
                    break
                elif highestidx == 4:
                    condition_ok[condition.index(spds[0]["condition"])] = False
                    spds.pop(0)
                    break
                elif highestidx == 5: 
                    condition_ok[condition.index(speed[0]["condition"])] = False
                    speed.pop(0)
                    break
            if res[6] <= 508:
                break
        res[6] = 508-res[6]
        #OPTIMIZE IF POSSIBLE
        def_pokemon.nature=nat
        stat_to_hinder = None
        stat_to_test = [self.get_stat_by_name("attack"), self.get_stat_by_name("defense"), self.get_stat_by_name("special-attack"), self.get_stat_by_name("special-defense"), self.get_stat_by_name("speed")]
        hinderArray = [0, 0, 0, 0, 0, 0]
        if def_pokemon.nature and def_pokemon.nature.decreased_stat.stat.identifier=="speed":
            stat_to_hinder = self.get_stat_by_name("speed")
        elif def_pokemon.nature and (def_pokemon.nature.decreased_stat.stat.identifier=="special-attack" or def_pokemon.nature.decreased_stat.stat.identifier=="attack"):
            stat_to_hinder = self.get_stat_by_name(def_pokemon.nature.decreased_stat.stat.identifier)
        elif len(attacks) == 0:
            stat_to_hinder =self.get_stat_by_name("attack")
        elif len(spas) == 0:
            stat_to_hinder = self.get_stat_by_name("special-attack")       
        else:
            test_hinder = self.get_stat_by_name("attack")
            lowest_diff = 508
            for i in range(5):
                if len(stat_stack[i]) > 0:
                    list_of_natures = stat_stack[i][0]["allconds"]
                    stat_something = list_of_natures[2]
                    if stat_something:
                        if i% 2 == 1:
                            stat_map_list =  stat_something
                            #if isHPEnabled) > logic later
                            
                            for x in range(len(stat_map_list)):
                                statL = ("defense" if i == 1 else "special-defense")
                                
                                if stat_map_list[x]["hp"] + stat_map_list[x][statL] - (res[0] + res[i+1]) < lowest_diff:
                                    lowest_diff = (res[0] + res[i+1])
                                    test_hinder = stat_to_test[i]
                                    hinderArray[0] = stat_map_list[x]["hp"] - res[0]
                                    for z in range(i):
                                        hinderArray[z] = 0
                                    hinderArray[i+1] = stat_map_list[x][statL] - res[i+1]

                        else:
                            stat_map = stat_something
                            if abs(stat_map[stat_to_test[i].stat_info.identifier] - res[i+1]) < lowest_diff:
                                test_hinder = stat_to_test[i]
                                lowest_diff  = abs(stat_map[stat_to_test[i].stat_info.identifier] - res[i+1])
                                for z in range(i):
                                    hinderArray[z] = 0
                                hinderArray[i+1] = stat_map[stat_to_test[i].stat_info.identifier] - res[i+1]
                else:
                    test_hinder = stat_to_test[i]
                    break
            stat_to_hinder = test_hinder

        
        stat_to_boost = self.get_stat_by_name("attack")
        highest_diff = 0
        boostArray = [0, 0, 0, 0, 0, 0]
        for i in range(5):
            if len(stat_stack[i]) > 0:
                list_of_natures = stat_stack[i][0]["allconds"]
                if not list_of_natures[1] or not list_of_natures[0]:
                    stat_to_boost = stat_to_test[i]
                    break
                
                if i% 2 == 1:
                    stat_map_list = [] 
                    if not def_pokemon.nature or (def_pokemon.nature.decreased_stat==def_pokemon.nature.increased_stat) or not def_pokemon.nature.increased_stat==stat_to_test[i]:
                        stat_map_list =  list_of_natures[1]
                    else:
                        stat_map_list =  list_of_natures[0]
                    

                    
                    for x in range(len(stat_map_list)):
                        statL = ("defense" if i == 1 else "special-defense")
                        
                        if not is_max_hp:
                            if stat_map_list[x]["hp"] + stat_map_list[x][statL] - (res[0] + res[i+1]) > highest_diff:
                                highest_diff = stat_map_list[x]["hp"] + stat_map_list[x][statL] - (res[0] + res[i+1])
                                stat_to_boost = stat_to_test[i]
                                boostArray[0] = stat_map_list[x]["hp"] - res[0]
                                for z in range(i):
                                    boostArray[z] = 0
                                boostArray[i+1] = stat_map_list[x][statL] - res[1]

                        else:
                            if stat_map_list[x]["hp"] + stat_map_list[x][statL] - (res[0] + res[i+1]) > highest_diff:
                                highest_diff = stat_map_list[x]["hp"] + stat_map_list[x][statL] - (res[0] + res[i+1])
                                stat_to_boost = stat_to_test[i]
                                boostArray[0] = stat_map_list[x]["hp"] - res[0]
                                for z in range(i):
                                    boostArray[z] = 0
                                boostArray[i+1] = stat_map_list[x][statL] - res[1]

 
                else:
                    stat_map_list =[] 
                    if not def_pokemon.nature or (def_pokemon.nature.decreased_stat==def_pokemon.nature.increased_stat) or not def_pokemon.nature.increased_stat==stat_to_test[i]:
                        stat_map_list = list_of_natures[1]
                    else:
                        stat_map_list = list_of_natures[0]


                    if abs(stat_map_list[stat_to_test[i].identifier] - res[i+1] ) > highest_diff:
                        stat_to_boost = stat_to_test[i]
                        highest_diff  = abs(stat_map_list[stat_to_test[i].identifier] - res[i+1])
                        for z in range(i):
                            boostArray[z] = 0
                        boostArray[i+1] = abs(stat_map_list[stat_to_test[i].identifier] - res[i+1])

        
        #TODO: We found Stats to increase and lower, as well as difference in stats. Now we need to implement the difference function.
        suggested_nature = self.get_nature_by_increase_and_decrease(stat_to_hinder, stat_to_boost)
        #print(suggested_nature.identifier)
        suggestedRes = []
        suggestedTotal = 0
        for i in range(6):
            suggestedRes.append(res[i] + hinderArray[i] - boostArray[i])
            suggestedTotal+= suggestedRes[i]
        suggestedRes.append(508-suggestedTotal)
        
        goodCond = []
        badCond = []
        for i in range(len(condition)):
            if condition_ok[i]:
                goodCond.append(condition[i])
            else:
                badCond.append(condition[i])

        
        
        result_map = {}
        result_map["resultEVarr"]= res
        result_map["calculatedNature"] = nature_if_null
        result_map["suggestedEVarr"] = suggestedRes
        result_map["suggested_nature"] = suggested_nature
        result_map["goodCond"] = goodCond
        result_map["badCond"] = badCond
        return result_map
