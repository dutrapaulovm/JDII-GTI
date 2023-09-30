// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function NoBase() constructor{
	
	tomar_decisao = function(){
	}	
}
//Nó utilizado para tomar a decisão lógica
function NoDecisao() : NoBase() constructor{
	
	//Definindo os nós filhos 
	no_sim = noone;
	no_nao = noone;
	
	avaliar = function(){
		return false;	
	}
	
	tomar_decisao = function(){
		if avaliar(){
			return no_sim;
		}
		else{
			return no_nao;
		}
	}
}


function NoAcao() : NoBase() constructor{
	
	tomar_decisao = function(){
		
	}
	
}

