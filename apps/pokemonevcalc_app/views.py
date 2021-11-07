from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from apps.pokemonevcalc_app.models import Move, Items, Pokemon, Condition
from apps.pokemonevcalc_app.models import Ability, Nature
from .services import APIService
from .serializers import MoveSerializer, PokemonSerializer, ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, filters

api_serv = APIService()
# Create your views here.
def index(request):
	response = "Hello owo"
	boosts = ["+6", "+5", "+4", "+3", "+2", "+1", "0", "-1", "-2", "-3", "-4", "-5", "-6"]
	conditions_def = ["Outspeed", "Survive", "Survive 2", "OHKO", "2HKO"]
	weathers = ["None", "Rain", "Sun", "Sand", "Hail"]
	terrains = ["None", "Misty", "Grassy", "Electric", "Psychic"]
	status = ["Healthy", "Burn", "Paralyze", "Freeze", "Poison", "Toxic"]




def get_calculation(request):
	boosts = ["+6", "+5", "+4", "+3", "+2", "+1", "0", "-1", "-2", "-3", "-4", "-5", "-6"]
	conditions_def = ["Outspeed", "Survive", "Survive 2", "OHKO", "2HKO"]
	weathers = ["None", "Rain", "Sun", "Sand", "Hail"]
	terrains = ["None", "Misty", "Grassy", "Electric", "Psychic"]
	status = ["Healthy", "Burn", "Paralyze", "Freeze", "Poison", "Toxic"]
	
	def get_object_requested(obj, identifier):
		try:
			req = obj.objects.get(identifier=identifier)
			return req
		except Exception :
			return None
	context = {'errors': None, 'defPokemon': None, 'weathers': weathers, 'terrains': terrains, 'boosts': boosts, 'statuses': status, 'conditions': conditions_def, 'natures': Nature.objects.all()}

	def add_dash_and_lower(text):
		return text.replace(" ", "-").lower()
	condlist = []
	if request.method=='GET':
		return render(request, "calculator.html", context)

	elif request.method=='POST':
		args = request.POST
		valid = True
		generation = int(args['generation'])
		
		defending_pokemon = get_object_requested(Pokemon, add_dash_and_lower(args["calcpokemon"]))
		if not defending_pokemon:
			valid = False
			context["defPokemonError"] = True
		else:
			context["defPokemon"] = defending_pokemon
			defending_pokemon.level = int(args["level"])
			defending_pokemon.ability = get_object_requested(Ability, add_dash_and_lower(args["ability"]))
			defending_pokemon.item = get_object_requested(Items, add_dash_and_lower(args["item"]))
			defending_pokemon.status= args["status"]
			if args["nature-pokemon"] == "undecided":
				defending_pokemon.nature = None
			else:
				defending_pokemon.nature = get_object_requested(Nature, args["nature-pokemon"])
			defending_pokemon.poke_stats = list(defending_pokemon.stats.all().order_by('id'))
			
		# 	if (defending_pokemon.getLegacyTypes().size() > 0) {
		# 		for (LegacyType lt: defending_pokemon.getLegacyTypes()) {
		# 			if (lt.getGenerationId() <= generation){
		# 				defending_pokemon.getOldTypes().add(apiServ.getType(lt.getTypeId()))
		# 			}
		# 		}
		# 	}
		# }
		counter = 1
		conditions = []
		while f'pokemon-{counter}' in args:
			condition = Condition()
			condition.cond = args[f"condition-{counter}"]
			cond_pokemon = get_object_requested(Pokemon,add_dash_and_lower(args[f"pokemon-{counter}"]))
			cond_pokemon.poke_stats = list(cond_pokemon.stats.all().order_by('id'))
			print(cond_pokemon.poke_stats)
			if not cond_pokemon:
				valid = False
				context[f"condPokemon{counter}Error"] = True
			else:
				cond_pokemon.ability = get_object_requested(Ability, add_dash_and_lower(args[f"ability-{counter}"]))
				cond_pokemon.item = get_object_requested(Items, add_dash_and_lower(args[f"item-{counter}"]))
				cond_pokemon.level = int(args[f"level-{counter}"])
				cond_pokemon.status = args[f"status-{counter}"]
				cond_pokemon.poke_stats[0].iv = int(args[f"hp-iv-{counter}"])
				cond_pokemon.poke_stats[0].ev = int(args[f"hp-{counter}"])
				cond_pokemon.nature = get_object_requested(Nature, args[f"nature-{counter}"])
				cond_pokemon.poke_stats[5].iv=int(args[f"speed-iv-{counter}"])
				cond_pokemon.poke_stats[5].ev = int(args[f"speed-{counter}"])			
				# if (cond_pokemon.getLegacyTypes().size() > 0) {
				# 	for (LegacyType lt: cond_pokemon.getLegacyTypes()) {
				# 		if (lt.getGenerationId() <= Integer.parseInt(args["generation"))){
				# 			cond_pokemon.getOldTypes().add(apiServ.getType(lt.getTypeId()))
				# 		}
				# 	}
				# }
				move = get_object_requested(Move, add_dash_and_lower(args[f"move-{counter}"]))
				if not move:
					if condition.cond != "Outspeed" and condition.cond == "Underspeed":
						context[f"move{counter}Error"] = True
						valid = False					
				else:
					if move.damage_class_id == 2:
						cond_pokemon.poke_stats[1].iv = int(args[f"atk-iv-{counter}"])
						cond_pokemon.poke_stats[1].ev = int(args[f"atk-{counter}"])			
						cond_pokemon.poke_stats[2].iv = int(args[f"def-iv-{counter}"])
						cond_pokemon.poke_stats[2].ev = int(args[f"def-{counter}"])
					else:
						evatk = int(args[f"atk-{counter}"])
						cond_pokemon.poke_stats[3].iv=int(args[f"atk-iv-{counter}"])
						cond_pokemon.poke_stats[3].ev=evatk
						print(evatk, cond_pokemon.poke_stats[3].ev)
						cond_pokemon.poke_stats[4].iv=int(args[f"def-iv-{counter}"])
						cond_pokemon.poke_stats[4].ev=int(args[f"def-{counter}"])
						print(cond_pokemon.poke_stats)

					condition.move=move

					# if (apiServ.getLegacyMove(move.getIdentifier(), generation) != null) {
					# 	move.setEffectiveBP(apiServ.getLegacyMove(move.getIdentifier(), generation).getPower())
					# }

			
			condition.is_doubles = args["single-double"]=="double"
			condition.pokemon = cond_pokemon
			condition.generation=generation
			condition.set_opp_boost(args[f"boost-opp-{counter}"])
			condition.set_raw_boost(args[f"boost-you-{counter}"])
			condition.weather=args[f"weather-{counter}"]
			condition.terrain=args[f"terrain-{counter}"]
			if args[f"hits-{counter}"].isnumeric():
				condition.hits=int(args[f"hits-{counter}"])
			else:
				condition.hits = 1

			if f"z-{counter}" in args:
				condition.z = True
			if f"dynamax-self-{counter}" in args:
				condition.self_dmax = True
			if f"dynamax-opp-{counter}" in args:
				condition.opp_dmax=True
			if f"screen-{counter}" in args:
				condition.screens = True
			if f"your-tailwind-{counter}" in args:
				condition.your_tw = True
			if f"foe-tailwind-{counter}" in args:
				condition.foe_tw = True			
			if f"hh-{counter}" in args:
				condition.helping_hand=True		
			if f"flower-gift-{counter}" in args:
				condition.flower_gift = True
			if f"power-spot-{counter}" in args:
				condition.power_spot = True		
			if f"battery-{counter}" in args:
				condition.battery=True
			if f"stealth-rock-{counter}" in args:
				condition.stealth_rock = True
			if f"gravity-{counter}" in args:
				condition.gravity=True
			if f"smack-down-{counter}" in args:
				condition.smack_down = True
			if f"crit-{counter}" in args:
				condition.critical = True

			condition.health = float(args[f"hp-percentage-{counter}"])
			counter+=1
			conditions.append(condition)
		
		if not valid:
			context["allConditions"]= conditions
			context["errors"]= True
			context["boosts"]= boosts
			context["conditions"] = conditions_def
			context["weathers"]=weathers
			context["terrains"]= terrains
			context["natures"]= [nature.identifier for nature in Nature.objects.all()]
			context["statuses"]= status
			return render(request, "calculatorerrors.html", context)
		
		
		result = api_serv.calculate_EVs(defending_pokemon, conditions, "max-hp" in args)
		stat_list_x = []
		labels = ["HP", "Attack", "Defense", "Spec. Attack", "Spec. Defense", "Speed", "EVs Remaining"]
		abbrev = ["HP", "Atk", "Def", "SpA", "SpD", "Spe", "Total"]

		for i in range(7):
			tempX = []
			tempArr = result["resultEVarr"]
			tempX.append(tempArr[i])
			tempX.append(labels[i])
			tempX.append(abbrev[i])
			stat_list_x.append(tempX)
		
		goodCond = []
		badCond = []
		
		context["resultOn"]= True
		context["calcedstat"]=stat_list_x
		context["conditions"]= conditions
		context["pokemon"]= defending_pokemon
		if not defending_pokemon.nature:
			defending_pokemon.nature = result["calculatedNature"]
		
		if not result["suggestedEVarr"]:
			context["suggestionEV"] = result["suggestedEVarr"]
			context["suggestedNature"] = result["suggestedNature"]
		
		context["goodCondition"] = result["goodCond"]
		context["badCondition"]= result["badCond"]
		

		
		return render(request, "calculationresult.html", context)





class MoveView(generics.ListAPIView):
	serializer_class = MoveSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['^identifier']
	queryset=Move.objects.all()

	# def get(self, request):
	# 	return self.retrieve(request)


class PokemonView(generics.ListAPIView):
	serializer_class = PokemonSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['^identifier']
	queryset=Pokemon.objects.all()


class ItemView(generics.ListAPIView):
	serializer_class = ItemSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['^identifier']
	queryset = Items.objects.all()


