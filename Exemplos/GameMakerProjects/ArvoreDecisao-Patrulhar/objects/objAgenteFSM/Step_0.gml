/// @description Insert description here
// You can write your code in this editor
switch(estado){	
	case ESTADOS.PATRULHAR:		
		
		//Calcular a distância entre o Agente e o Jogador
		var dist = point_distance(x, y, obj_ponto.x, obj_ponto.y);
		
		//Chegou perto do jogador, muda de estado
		if dist < 128{			
			estado = ESTADOS.FUGIR;
			//Define a velocidade do objeto
			//speed = 0;						
			direction = (180 - direction);						
		}
		else{				
			ia_patrulhar();
		}
		
		estado_str = "patrulhando";
		
	break;	
	case ESTADOS.FUGIR:
		estado_str = "fugindo";
		var dist = point_distance(x, y, obj_ponto.x, obj_ponto.y);		 
		
		if (dist > 360){			
			estado = ESTADOS.PATRULHAR;	
			destinox   = random_range(64, room_width-64);
			destinoy   = random_range(64, room_height-64);
		}
		
	break;
}





