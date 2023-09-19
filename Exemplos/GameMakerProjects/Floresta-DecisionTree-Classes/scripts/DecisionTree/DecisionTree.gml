// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function NoBaseDecisao() constructor{
	
	tomar_decisao = function(){
		return NoBaseDecisao()
	}
	
}

function NoAcao() : NoBaseDecisao() constructor{	
	tomar_decisao = function(){
		return NoBaseDecisao()
	}	
}

function NoDecisao() : NoBaseDecisao() constructor{
	
	no_sim = new NoBaseDecisao(); 
	no_nao = new NoBaseDecisao();	
	
	testar_valor = function(){
		return false;	
	}
	
	tomar_decisao = function(){
		return NoDecisao();
	}
	
}
