# This is an auto-generated Django model module.
# You'll have to do the following manually to clean self up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import math


class Ability(models.Model):
	id = models.IntegerField(primary_key=True)
	identifier = models.TextField(blank=True, null=True)
	generation_id = models.IntegerField(blank=True, null=True)
	is_main_series = models.IntegerField(blank=True, null=True)
	name = models.CharField(max_length=255, blank=True, null=True)

	def get_identifier_cleaned(self):
		clean_identifier = self.identifier.replace("-", " ")
		clean_identifier = clean_identifier[0].upper() + clean_identifier[1:]
		for i in range(len(clean_identifier)):
			if clean_identifier[i] == " ":
				clean_identifier = f'{clean_identifier[:i+1]}{clean_identifier[i+1].upper()}{clean_identifier[i+2:]}'
		return clean_identifier

	class Meta:
		managed = False
		db_table = 'abilities'


class Berries(models.Model):
	id = models.IntegerField(primary_key=True)
	item_id = models.IntegerField(blank=True, null=True)
	firmness_id = models.IntegerField(blank=True, null=True)
	natural_gift_power = models.IntegerField(blank=True, null=True)
	natural_gift_type_id = models.IntegerField(blank=True, null=True)
	size = models.IntegerField(blank=True, null=True)
	max_harvest = models.IntegerField(blank=True, null=True)
	growth_time = models.IntegerField(blank=True, null=True)
	soil_dryness = models.IntegerField(blank=True, null=True)
	smoothness = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'berries'


class Items(models.Model):
	id = models.IntegerField(primary_key=True)
	identifier = models.TextField(blank=True, null=True)
	category_id = models.IntegerField(blank=True, null=True)
	cost = models.IntegerField(blank=True, null=True)
	fling_power = models.TextField(blank=True, null=True)
	fling_effect_id = models.TextField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'items'


class MoveDamageClasses(models.Model):
	id = models.IntegerField(primary_key=True)
	identifier = models.TextField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'move_damage_classes'


class MovePastGeneration(models.Model):
	id_x = models.IntegerField()
	identifier = models.CharField(max_length=255, blank=True, null=True)
	generation_id = models.IntegerField(blank=True, null=True)
	type_id = models.IntegerField(blank=True, null=True)
	power = models.IntegerField(blank=True, null=True)
	pp = models.IntegerField(blank=True, null=True)
	accuracy = models.IntegerField(blank=True, null=True)
	priority = models.IntegerField(blank=True, null=True)
	target_id = models.IntegerField(blank=True, null=True)
	damage_class_id = models.IntegerField(blank=True, null=True)
	effect_id = models.IntegerField(blank=True, null=True)
	effect_chance = models.IntegerField(blank=True, null=True)
	contest_type_id = models.IntegerField(blank=True, null=True)
	super_contest_effect_id = models.IntegerField(blank=True, null=True)
	generation = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'move_past_generation'


class MoveTargets(models.Model):
	id = models.IntegerField(primary_key=True)
	identifier = models.TextField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'move_targets'


class Move(models.Model):
	id = models.IntegerField(primary_key=True)
	identifier = models.CharField(max_length=255, blank=True, null=True)
	generation_id = models.IntegerField(blank=True, null=True)
	type = models.ForeignKey('Type', models.DO_NOTHING, blank=True, null=True)
	power = models.IntegerField(blank=True, null=True)
	pp = models.IntegerField(blank=True, null=True)
	accuracy = models.IntegerField(blank=True, null=True)
	priority = models.IntegerField(blank=True, null=True)
	target_id = models.IntegerField(blank=True, null=True)
	damage_class_id = models.IntegerField(blank=True, null=True)
	effect_id = models.IntegerField(blank=True, null=True)
	effect_chance = models.IntegerField(blank=True, null=True)
	contest_type_id = models.IntegerField(blank=True, null=True)
	contest_effect_id = models.IntegerField(blank=True, null=True)
	super_contest_effect_id = models.IntegerField(blank=True, null=True)
	max_move_power = models.IntegerField(blank=True, null=True)

	def __init__(self, *args, **kwargs):
		super(Move, self).__init__(*args, **kwargs)
		self.effectiveBP = 0
		self.attack_type = None


	dtype = models.CharField(max_length=31)

	def __str__(self) -> str:
		return self.identifier

	def getPower(self):
		if self.effectiveBP > 0:
			return self.effectiveBP
		else:
			return self.power


	def get_attack_type(self):
		if self.attack_type:
			return self.attack_type
		else:
			return self.type

	def get_identifier_cleaned(self):
		temp_identifier = self.identifier.replace('-', ' ')
		temp_identifier = f'{temp_identifier[0].upper()}{temp_identifier[1:]}'
		for i in range(len(temp_identifier)):
			if temp_identifier[i] == ' ':
				temp_identifier = f'{temp_identifier[:i+1]}{temp_identifier[i+1].upper()}{temp_identifier[i+2:]}'
		return temp_identifier

	class Meta:
		managed = False
		db_table = 'moves'

	def is_type(self, type):
		if self.type.identifier == type:
			return True
		return False


class Nature(models.Model):
	id = models.IntegerField(primary_key=True)
	identifier = models.TextField(blank=True, null=True)
	decreased_stat = models.ForeignKey('PokemonStats', models.DO_NOTHING, blank=True, null=True, related_name='decreasing_nature')
	increased_stat = models.ForeignKey('PokemonStats', models.DO_NOTHING, blank=True, null=True, related_name='increasing_nature')
	hates_flavor_id = models.IntegerField(blank=True, null=True)
	likes_flavor_id = models.IntegerField(blank=True, null=True)
	game_index = models.IntegerField(blank=True, null=True)
	identifer = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self) -> str:
		return self.identifier

	class Meta:
		managed = False
		db_table = 'natures'

	def get_identifier_cleaned(self):
		clean_identifier = self.identifier.replace("-", " ")
		clean_identifier = clean_identifier[0].upper() + clean_identifier[1:]
		for i in range(len(clean_identifier)):
			if clean_identifier[i] == " ":
				clean_identifier = f'{clean_identifier[:i+1]}{clean_identifier[i+1].upper()}{clean_identifier[i+2:]}'
		return clean_identifier


class Pokemon(models.Model):
	id = models.IntegerField(primary_key=True)
	identifier = models.CharField(max_length=255, blank=True, null=True)
	species_id = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	weight = models.IntegerField(blank=True, null=True)
	base_experience = models.IntegerField(blank=True, null=True)
	orderx = models.IntegerField(blank=True, null=True)
	is_default = models.IntegerField(blank=True, null=True)
	abilities = models.ManyToManyField(Ability, through='PokemonAbilities')
	types = models.ManyToManyField('Type', through='PokemonType')


	def __init__(self, *args, **kwargs):
		super(Pokemon, self).__init__(*args, **kwargs)
		self.ability = None
		self.item = None
		self.nature = None



	def __str__(self) -> str:
		return self.identifier

	def get_identifier_no_space(self):
		if "tapu" in self.identifier:
			return self.identifier.replace("-", "").replace(" ", "")
		elif self.identifier == "type-null" or self.identifier == "mr-rime" or self.identifier == "mime-jr":
			return self.identifier.replace("-", "")
		elif self.identifier == "type-null" or self.identifier == "mr-rime" or self.identifier == "mime-jr":
			return self.identifier.replace("-", "")
		elif "mr-mime" in self.identifier:
			return self.identifier.replace("mr-mime", "mrmime")
		elif "mega-x" in self.identifier:
			return self.identifier.replace("mega-x", "megax")
		
		elif "mega-y" in self.identifier:
			return self.identifier.replace("mega-y", "megay")
		
		elif "rapid-strike" in self.identifier:
			return self.identifier.replace("rapid-strike", "rapidstrike")
		
		elif "single-strike" in self.identifier:
			return self.identifier.replace("-single-strike", "")
		
		elif "-incarnate" in self.identifier:
			return self.identifier.replace("-incarnate", "")
		else:
			return self.identifier

	def get_identifier_cleaned(self):
		clean_identifier = self.identifier.replace("-", " ")
		clean_identifier = f'{clean_identifier[0].upper()}{clean_identifier[1:]}'
		for i in range(len(clean_identifier)):
			if clean_identifier[i] == " ":
				clean_identifier = f'{clean_identifier[:i+1]}{clean_identifier[i+1].upper()}{clean_identifier[i+2:]}'
		return clean_identifier

	def get_item_cleaned(self):
		if self.item:
			temp_identifier = self.item.identifier.replace('-', ' ')
			temp_identifier = f'{temp_identifier[0].upper()}{temp_identifier[1:]}'
			for i in range(len(temp_identifier)):
				if temp_identifier[i] == ' ':
					temp_identifier = f'{temp_identifier[:i+1]}{temp_identifier[i+1].upper()}{temp_identifier[i+2:]}'
			return temp_identifier
		else:
			return None

	def get_HP(self):
		if self.stats:
			stt = self.poke_stats[0]
			return math.floor((2*stt.base_stat+stt.iv+math.floor(stt.ev/4))*self.level/100)+self.level+10

	def get_stat(self, stt): 
		# print(f"base stats: {stt.base_stat}, iv: {stt.iv}, ev: {stt.ev}")
		base= math.floor((2*stt.base_stat+stt.iv+math.floor(stt.ev/4))*self.level/100)+5
		if self.nature and self.nature.decreased_stat.stat.identifier != self.nature.increased_stat.stat.identifier and self.nature.increased_stat.stat.identifier == stt.stat.identifier:
			return math.floor(base*1.1)
		elif self.nature and self.nature.decreased_stat.stat.identifier != self.nature.increased_stat.stat.identifier and self.nature.decreased_stat.stat.identifier == stt.stat.identifier:
			return math.floor(base*0.9)
		else:
			return base

	def get_atk(self):
		if self.poke_stats:
			stt = self.poke_stats[1]
			return self.get_stat(stt)


	def get_spa(self):
		if self.stats:
			stt = self.poke_stats[3]
			return self.get_stat(stt)

	def get_def(self):
		if self.stats:
			stt = self.poke_stats[2]
			return self.get_stat(stt)


	def get_spd(self):
		if self.stats:
			stt = self.poke_stats[4]
			return self.get_stat(stt)


	def get_speed(self):
		if self.stats:
			stt = self.poke_stats[5]
			return self.get_stat(stt)

	def is_type(self, type):
		for t in self.types.all():
			if t.identifier == type:
				return True
		return False

	def get_effectiveness_from(self, t):
		init = 1
		# if (this.oldTypes != null && this.oldTypes.size() > 0) {
		# 	for (Type x: this.oldTypes) {
		# 		if (x.getEffectivenessFrom(t) == 200) {
		# 			init *= 2;
		# 		}
		# 		else if (x.getEffectivenessFrom(t) == 50) {
		# 			init *= 0.5;
		# 		}
		# 		else if (x.getEffectivenessFrom(t) == 0) {
		# 			init = 0;
		# 		}
		# 	}
		# }
		# else {
		for x in self.types.all():
			if x.get_effectiveness_from(t) == 200:
				init *= 2
			elif x.get_effectiveness_from(t) == 50:
				init *= 0.5
			elif x.get_effectiveness_from(t) == 0:
				init = 0
		return init

	class Meta:
		managed = False
		db_table = 'pokemon'

	


class PokemonAbilities(models.Model):
	pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, blank=True, null=True)
	ability = models.ForeignKey(Ability, models.DO_NOTHING, blank=True, null=True)
	is_hidden = models.IntegerField(blank=True, null=True)
	slot = models.IntegerField(blank=True, null=True)
	
	def __str__(self) -> str:
		return self.identifier
	
	class Meta:
		managed = False
		db_table = 'pokemon_abilities'


class PokemonStats(models.Model):
	pokemon = models.ForeignKey('Pokemon', models.DO_NOTHING, blank=True, null=True, related_name="stats")
	stat = models.ForeignKey('Stat', models.DO_NOTHING, blank=True, null=True, related_name="stat_info")
	base_stat = models.IntegerField(blank=True, null=True)
	effort = models.IntegerField(blank=True, null=True)
	def __init__(self, *args, **kwargs):
		super(PokemonStats, self).__init__(*args, **kwargs)
		self.iv = 31
		self.ev = 0


	class Meta:
		managed = False
		db_table = 'pokemon_stats'


class PokemonType(models.Model):
	pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, blank=True, null=True)
	type = models.ForeignKey('Type', models.DO_NOTHING, blank=True, null=True)
	slot = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'pokemon_types'


class PokemonTypePast(models.Model):
	pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, blank=True, null=True)
	generation_id = models.IntegerField(blank=True, null=True)
	type = models.ForeignKey('Type', models.DO_NOTHING, blank=True, null=True)
	slot = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'pokemon_types_past'


class Stat(models.Model):
	id = models.IntegerField(primary_key=True)
	damage_class_id = models.TextField(blank=True, null=True)
	identifier = models.TextField(blank=True, null=True)
	is_battle_only = models.IntegerField(blank=True, null=True)
	game_index = models.IntegerField(blank=True, null=True)

	def __str__(self) -> str:
		return self.identifier

	class Meta:
		managed = False
		db_table = 'stats'


class TypeEfficacy(models.Model):
	damage_type = models.ForeignKey('Type', models.DO_NOTHING, blank=True, null=True, related_name='type_effectiveness_to')
	target_type = models.ForeignKey('Type', models.DO_NOTHING, blank=True, null=True, related_name='type_effectiveness_from')
	damage_factor = models.IntegerField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'type_efficacy'


class Type(models.Model):
	id = models.IntegerField(primary_key=True)
	identifier = models.TextField(blank=True, null=True)
	generation_id = models.IntegerField(blank=True, null=True)
	damage_class_id = models.IntegerField(blank=True, null=True)
	
	def __str__(self) -> str:
		return self.identifier

	class Meta:
		managed = False
		db_table = 'types'

	def get_effectiveness_to(self, t):
		for type in self.type_effectiveness_to.all():
			if type.target_type.identifier == t.identifier:
				return type.damage_factor
		return 100
	
	def get_effectiveness_from(self, t):
		for type in self.type_effectiveness_from.all():
			if type.damage_type.identifier == t.identifier:
				return type.damage_factor
		return 100


class Condition():
	def __init__(self):
		self.cond=""
		self.pokemon=None
		self.terrain=""
		self.weather=""
		self.move=None
		self.generation=8
		self.hits=1
		self.screens=False
		self.opp_boost=0
		self.your_boost=0
		self.raw_boost=0
		self.raw_opp_boost=0
		self.summary=""
		self.is_doubles=False
		self.helping_hand=False
		self.friend_guard=False
		self.rivalry=False
		self.fairy_aura=False
		self.dark_aura=False
		self.aura_break=False
		self.neutralizing_gas=False
		self.is_critical=False
		self.health=100
		self.battery=False
		self.flower_gift=False
		self.power_spot=False
		self.your_tw=False
		self.foe_tw=False
		self.charge=False
		self.gravity=False
		self.flash_fire=False
		self.z=False
		self.self_dmax=False
		self.opp_dmax=False
		self.item_consumed=False
		self.smack_down=False
		self.stealth_rock=False
		self.max_hp = False
		self.critical = False

	def set_raw_boost(self, your_boost):
		self.raw_boost = your_boost	
		if your_boost=="0":
			self.your_boost =  1.0	
		
		elif your_boost=="+1":
			self.your_boost =  1.5	
		
		elif your_boost=="+2":
			self.your_boost =  2.0	
		
		elif your_boost=="+3":
			self.your_boost =  2.5	
		
		elif your_boost=="+4":
			self.your_boost =  3.0	
		
		elif your_boost=="+5":
			self.your_boost =  3.5	
		
		elif your_boost=="+6":
			self.your_boost =  4.0	
		
		elif your_boost=="-1":
			self.your_boost =  2.0/3.0	
		
		elif your_boost=="-2":
			self.your_boost =  2.0/4.0	
		
		elif your_boost=="-3":
			self.your_boost = 2.0/5.0 	
		
		elif your_boost=="-4":
			self.your_boost =  2.0/6.0	
		
		elif your_boost=="-5":
			self.your_boost =  2.0/7.0	
		
		else:
			self.your_boost =  0.25	
		
	def set_opp_boost(self, opp_boost):
		self.raw_opp_boost = opp_boost

		if opp_boost=="0":
			self.opp_boost =  1.0
		elif opp_boost=="+1":
			self.opp_boost =  1.5
		elif opp_boost=="+2":
			self.opp_boost =  2.0
		elif opp_boost=="+3":
			self.opp_boost =  2.5
		elif opp_boost=="+4":
			self.opp_boost =  3.0
		elif opp_boost=="+5":
			self.opp_boost =  3.5
		elif opp_boost=="+6":
			self.opp_boost =  4.0
		elif opp_boost=="-1":
			self.opp_boost =  2.0/3.0
		elif opp_boost=="-2":
			self.opp_boost =  2.0/4.0
		elif opp_boost=="-3":
			self.opp_boost = 2.0/5.0 
		elif opp_boost=="-4":
			self.opp_boost =  2.0/6.0
		elif opp_boost=="-5":
			self.opp_boost =  2.0/7.0
		else:
			self.opp_boost =  0.25