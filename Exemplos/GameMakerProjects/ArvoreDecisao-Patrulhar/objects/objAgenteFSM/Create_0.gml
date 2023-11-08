/// @description Insert description here
// You can write your code in this editor
randomize()
velocidade = 2;
destinox   = random_range(64, room_width-64);
destinoy   = random_range(64, room_height-64);

/*Utilizando enumerações para
definir os estados do agente.*/
enum ESTADOS{
	PATRULHAR = 1,
	FUGIR     = 2
}

//Define o estado inicial do agente
estado     = ESTADOS.PATRULHAR;
estado_str = "patrulhando";

