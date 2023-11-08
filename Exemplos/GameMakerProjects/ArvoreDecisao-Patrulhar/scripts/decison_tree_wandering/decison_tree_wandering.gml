
/*Nó de teste que verifica se o agente está longe do 
jogador ou algum objeto.
Estamos considerando o objeto (obj_ponto) para
verificar se o agente(objAgenteTree) está longe dele.
*/
function NoEstaLonge() : NoDecisao() constructor{
	
	m_agente = noone;
	
	avaliar = function(){
		var _dist = 0;
		with(m_agente){
			_dist = point_distance(x, y, obj_ponto.x, obj_ponto.y);		
			if (_dist > 360){
				//Para permitir inverter
				//a direção novamente.
				if (esta_invertido){
					esta_invertido = false;
					destinox   = random_range(64, room_width-64);
					destinoy   = random_range(64, room_height-64);				
				}
			}			
		}
		return (_dist > 360);
	}	
}

/*Nó de teste que verifica se o agente está perto do 
jogador ou algum objeto.
Estamos considerando o objeto (obj_ponto) para
verificar se o agente(objAgenteTree) está perto dele.
*/
function NoEstaPerto() : NoDecisao() constructor{
	
	m_agente = noone;
	
	avaliar = function(){
		var _dist = 0;
		with(m_agente){
			_dist = point_distance(x, y, obj_ponto.x, obj_ponto.y);		
		}
		return (_dist < 128);
	}	
}

function NoNaoEstaInvertido() : NoDecisao() constructor {
	
	m_agente = noone;
	
	avaliar = function(){
		var _res = false;		
		with(m_agente){
			_res = esta_invertido;
		}		
		return _res;
	}		
	
}


function NoAcaoInterverDir() : NoAcao() constructor{
	
	m_agente = noone;
	
	tomar_decisao = function(){
		
		with(m_agente){
			/*Inverte a direção somente
			se o objeto ainda não está invertido
			a sua direção de movimento.
			*/
			if (!esta_invertido){
				esta_invertido = true;
				ia_inverter_dir();
			}
			//Calculando a distância entre objetos
			/*var _dist = point_distance(x, y, obj_ponto.x, obj_ponto.y);
			if (_dist > 360){
				//Para permitir inverter
				//a direção novamente.
				esta_invertido = false;
			}*/
			
		}
		return m_agente.no_raiz;
	}
	
}



function NoAcaoPatrulhar() : NoAcao() constructor{
	
	m_agente = noone;
	
	tomar_decisao = function(){
		with(m_agente){				
			ia_patrulhar();
		}
		return m_agente.no_raiz;
	}
	
}
