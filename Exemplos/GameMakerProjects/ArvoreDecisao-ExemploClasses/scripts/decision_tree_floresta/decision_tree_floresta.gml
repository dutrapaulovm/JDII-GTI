function NoDecisaoFloresta() : NoDecisao() constructor{
	
	pergunta = "";
	
	//Avalia a condição para o nó
	avaliar = function(){		
		return (obj_tempo.estado_tempo == "dia" ||
		obj_resposta.resposta == "Sim");
	}
	
	tomar_decisao = function(){
		if (obj_resposta.resposta != ""){
			if (avaliar()){
				return no_sim;
			}			
			return no_nao;			
		}
		//Retorna o próprio nó
		return self;
	}
}

function NoAcaoFloresta() : NoAcao() constructor{
		
	texto = ""	
	
	tomar_decisao = function(){
				
	}
	
}

function NoAcaoAtravessar() : NoAcaoFloresta() constructor{	
	tomar_decisao = function(){
		//room_next(room);
		//room_goto(rm_floresta);		
		with(obj_gerencia_nos){
			if !acao_executada{
				alarm[0] = 120;
				acao_executada = true;
			}
		}
		//obj_gerencia_nos.alarm[0] = 120;
	}	
}

function NoAcaoNaoAtravessar() : NoAcaoFloresta() constructor{
	
	tomar_decisao = function(){
		//Reinicia a cena atual
		with(obj_gerencia_nos){
			if !acao_executada{
				alarm[1] = 120;
				acao_executada = true;
			}
		}		
	}
}

