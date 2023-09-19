// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function NoAcaoFloresta() : NoAcao() constructor{
	
	texto = "";
	escrever_texto = false;
	
	tomar_decisao = function(){
		escrever_texto = true;
		//obj_gerencia_nos.alarm[0] = 10;		
		with(obj_gerencia_nos){
			if (reiniciar == false){
				reiniciar = true;
				alarm[0] = 60;			
			}
		}
	}

}

function NoDecisaoFloresta() : NoDecisao() constructor{
	
	pergunta = "";
	
	testar_valor = function(){		
		if (obj_gerencia_nos.resposta != ""){
			return ( (obj_tempo.status_tempo == "Dia") || (obj_gerencia_nos.resposta == "Sim") );
		}
		
		return false;
	}
	
	tomar_decisao = function(){
		
		if (testar_valor()){
			no_sim.tomar_decisao();
			return no_sim;
		}
		else{
			if (obj_gerencia_nos.resposta == "Não"){
				no_nao.tomar_decisao();
				return no_nao;
			}
		}
		return self;
	}
	
}
