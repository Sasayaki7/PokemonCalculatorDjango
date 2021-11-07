/**
 * 
 */
 

const formRow = document.getElementById('condition-1').cloneNode(true)
const conditions = document.querySelector('.conditions')


function changeStringNumber(str, index){
	if (str != null){
		return str.replace(/\d+/, index);
	}
	else{
		return ""
	}	
}

function changeName(element, index){
	if(element.nodeName == 'LABEL'){
		element.setAttribute("for",changeStringNumber(element.getAttribute("for"),  index));
	}
	else if (element.nodeName == 'INPUT' || element.nodeName == 'SELECT'){
		element.setAttribute("name",changeStringNumber(element.getAttribute("name"), index));
		if (element.type =='radio' || element.type == 'checkbox'){
			element.setAttribute("id", changeStringNumber(element.getAttribute("id"), index))
		}
		
	}
	else if (element.nodeName == 'DIV'){
		element.setAttribute("id",changeStringNumber(element.getAttribute("id"), index));
	}

}


function changeAllNodes(element, index){
	if (element.hasChildNodes()){
		element.childNodes.forEach(e =>{
			changeAllNodes(e, index)
		})
	}
	changeName(element, index)
	return element
}

function cleanseText(text){
	return text.replace(/ /g, "-").toLowerCase();
}


function isMultiHitMove(move){
	let moves = ["Arm Thrust", "Bone Rush", "Bonemerang", "Bullet Seed", "Double Hit", "Double Iron Bash", "Double Kick", "Dragon Darts", "Dual Chop", "Dual Wingbeat", 
	"Fury Attack", "Fury Swipes", "Gear Grind", "Icicle Spear", "Pin Missile", "Rock Blast", "Scale Shot", "Surging Strikes", "Tail Slap", "Triple Axel", "Triple Kick", "Water Shuriken"];
	return moves.includes(move)
}

function removeDash(s){
	let arrS = s.split("-")
	arrS = arrS.map(w => w.charAt(0).toUpperCase() + w.slice(1))
	return arrS.join(" ")
}

function clearAutoCompleteList(div){
	while (div.firstChild){
		div.removeChild(div.firstChild);
	}
}

function clearAutoCompleteFromNode(div){
	clearAutoCompleteList(div.parentNode.querySelector('.item-autocomplete'));
}

function createListOfAutoComplete(list, div){
	let html = "";
	let counter = 0;
	clearAutoCompleteList(div)
	for (let item of list){
		let newToggle = document.createElement("div");
		newToggle.setAttribute("class", "autocomplete-item")
		newToggle.innerHTML = item.identifier;
		newToggle.classList.add("autocomplete-selector")

		newToggle.addEventListener("click", function(e){
			let elem = div.parentNode.querySelector("input") 
			elem.value = removeDash(item.identifier)
			if (elem.name.includes("move")){
				let movename = removeDash(item.identifier)
				if (isMultiHitMove(movename)){
					div.parentNode.parentNode.querySelector(".input-row").classList.remove('invisible')
				}
				else{
					div.parentNode.parentNode.querySelector(".input-row").classList.add('invisible')
					div.parentNode.parentNode.querySelector(".input-row input").value = 1
				}
			}
			if (elem.name.includes("calcpokemon")){
				getImageForPokemon(elem);
			}
			else if (elem.name.includes("pokemon")){
				changeOppPokemon(elem);
			}
			else if (elem.name == "item"){
				changeItemForPokemon(elem)
			}
			else if (elem.name.includes("item")){
				changeItemForOppPokemon(elem)
			}
			clearAutoCompleteList(div)
		})
		div.appendChild(newToggle);
		counter ++;
		if (counter > 5){
			break;
		}
	}
}


function getMovesStartingWith(s, node){
	fetch(`/api/moves?startWith=${s}`)
		.then(resp => resp.json())
		.then(resp => {
			createListOfAutoComplete(resp, node.parentNode.querySelector('.item-autocomplete'))
		})
}


function getPokemonStartingWith(s, node){
	fetch(`/api/pokemon?startWith=${s}`)
		.then(resp => resp.json())
		.then(resp => {
			createListOfAutoComplete(resp, node.parentNode.querySelector('.item-autocomplete'))
		})
}



function getItemsStartingWith(s, node){
	fetch(`/api/items?startWith=${s}`)
		.then(resp => resp.json())
		.then(resp => {
			createListOfAutoComplete(resp, node.parentNode.querySelector('.item-autocomplete'))
		})
}


function autoComplete(node){
	let str = node.value
	if (node.name.includes("pokemon")){
		getPokemonStartingWith(str, node);
	}
	else if (node.name.includes("move")){
		getMovesStartingWith(str, node);
	}
	else if (node.name.includes("item")){
		getItemsStartingWith(str, node)
	}
}

function changeTypes(node, list){
	while (node.firstChild){
		node.removeChild(node.firstChild);
	}
	for (let type of list){
		let image = document.createElement("img");
		image.setAttribute("src", `https://www.serebii.net/pokedex-bw/type/${type.type.name}.gif`)
		node.appendChild(image);
	}

}

function cleanForImage(str){
		if (str.indexOf("tapu") != -1) {
			return str.replace("-", "");
		}
		else if (str =="type-null"||str=="mr-rime"||str=="mime-jr") {
			return str.replace("-", "");
		}
		else if (str.indexOf("mr-mime") != -1) {
			return str.replace("mr-mime", "mrmime");
		}
		else if (str.indexOf("mega-x") != -1) {
			return str.replace("mega-x", "megax");
		}
		else if (str.indexOf("mega-y") != -1) {
			return str.replace("mega-y", "megay");
		}
		else if (str.indexOf("rapid-strike") != -1) {
			return str.replace("rapid-strike", "rapidstrike");
		}
		else if (str.indexOf("single-strike") != -1) {
			return str.replace("-single-strike", "");
		}
		else if (str.indexOf("-incarnate") != -1){
			return str.replace("-incarnate", "");	
		}
		else {
			return str.replace(/ /g, "-");
		}
}

function getImageForPokemon(e){
	let imageCleanseText = cleanForImage(cleanseText(e.value).toLowerCase())

	let cleansedText = cleanseText(e.value)
	console.log(cleansedText);
	fetch(`https://pokeapi.co/api/v2/pokemon/${cleansedText}`)
		.then(resp => resp.json())
		.then(resp => {document.getElementById("pokemon-pic").src=`https://play.pokemonshowdown.com/sprites/xyani/${imageCleanseText}.gif`
			let html = "";
			for(let abil in resp.abilities){
				html += `<option ${abil==0?'selected' : ''} value=${resp.abilities[abil].ability.name}>${removeDash(resp.abilities[abil].ability.name)}</option>`
			}
			changeTypes(e.parentNode.parentNode.parentNode.querySelector('.type-pokemon'), resp.types);
			e.parentNode.parentNode.parentNode.querySelector(".your-ability").innerHTML=html
		})
		.catch()
}

function changeOppPokemon(e){
	let imageCleanseText = cleanForImage(cleanseText(e.value).toLowerCase())
	console.log(e.value)
	let cleansedText = cleanseText(e.value)
	console.log(cleansedText);
	fetch(`https://pokeapi.co/api/v2/pokemon/${cleansedText}`)
		.then(resp => resp.json())
		.then(resp => {
			e.parentNode.parentNode.parentNode.querySelector(".opp-pokemon").src=`https://play.pokemonshowdown.com/sprites/xyani/${imageCleanseText}.gif`
			let html = "";
			for(let abil in resp.abilities){
				html += `<option ${abil==0?'selected' : ''} value=${resp.abilities[abil].ability.name}>${removeDash(resp.abilities[abil].ability.name)}</option>`
			}
			changeTypes(e.parentNode.parentNode.parentNode.querySelector('.type-pokemon'), resp.types);
			e.parentNode.parentNode.parentNode.parentNode.querySelector(".opp-ability").innerHTML=html
		})
		.catch()
}

function changeItemForPokemon(e){
	let cleansedText = cleanseText(e.value)
	document.getElementById("item-pic").src=`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/${cleansedText}.png`
}

function changeItemForOppPokemon(e){
	let cleansedText = cleanseText(e.value)
	e.parentNode.parentNode.parentNode.parentNode.querySelector(".opp-item").src=`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/${cleansedText}.png`
}

function addRow(){
	let cloneRow = formRow.cloneNode(true);
	cloneRow = changeAllNodes(cloneRow, conditions.children.length)
	conditions.appendChild(cloneRow);
	conditions.appendChild(document.getElementById('add-button'));
	if (conditions.childNodes.length>=10){
		document.getElementById('add-button').classList.add('invisible');
	}
}

function changeCondition(e){
	let condition = e.parentNode.parentNode;
	let condimg = e.parentNode.querySelector('.cond-show')

	let attackShow = condition.querySelector('.offev')
	let speedShow = condition.querySelector('.speedev')
	let defShow = condition.querySelector('.defev')
	speedShow.classList.add('invisible')
	defShow.classList.add('invisible')
	attackShow.classList.add('invisible')
	if (e.value=='Outspeed' || e.value=='Underspeed'){
		speedShow.classList.remove('invisible')
		condimg.src = "/static/assets/outspeed.png"
	}
	else if (e.value=='Survive' || e.value == 'Survive 2'){
		attackShow.classList.remove('invisible')
		condimg.src = "/static/assets/blue-arrow.png"

	}
	else{
		defShow.classList.remove('invisible')
		condimg.src = "/static/assets/orange-arrow.png"
	}
}

function deleteRow(e){
	let condition = e.parentNode
	if (conditions.childNodes.length<=2){
		return;
	}
	let startIndex = parseInt(condition.id.match(/\d+/)[0])+1;
	condition.remove();
	for (let index = startIndex; index < conditions.childNodes.length; index++){
		let nextElem = document.querySelector(`#condition-${index}`)
		if (nextElem){
			changeAllNodes(nextElem, index-1)
		}
		else{
			return
		}
	}
	document.getElementById('add-button').classList.remove('invisible')
}

function expandRow(e){
	return;
}

console.log('loaded')