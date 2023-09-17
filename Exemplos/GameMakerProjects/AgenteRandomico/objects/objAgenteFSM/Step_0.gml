/// @description Insert description here
// You can write your code in this editor
switch(estado){	
	case ESTADOS.PATRULHAR:		
		estado_str = "patrulhando";
		//Calcular a distância entre o Agente e o Jogador
		var _dist = point_distance(x, y, obj_ponto.x, obj_ponto.y);
		
		//Chegou perto do jogador, muda de estado
		if _dist < 128{			
			estado = ESTADOS.FUGIR;
			//Define a velocidade do objeto
			//speed = 0;							
			//Alterando a direção do objeto
			direction = direction + 180
		}
		else{				
			ia_patrulhar();
		}
		
	break;	
	case ESTADOS.FUGIR:
		
		estado_str = "fugindo";
		
		_dist = point_distance(x, y, obj_ponto.x, obj_ponto.y);		 
		
		if (_dist > 360){			
			estado = ESTADOS.PATRULHAR;	
			destinox   = random_range(64, room_width-64);
			destinoy   = random_range(64, room_height-64);
		}
		
	break;
}