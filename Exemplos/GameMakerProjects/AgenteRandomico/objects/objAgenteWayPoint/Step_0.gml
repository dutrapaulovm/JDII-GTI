/// @description Insert description here
// You can write your code in this editor
//Pegando a lista criada no objeto
var lista = objControlador.lista;

if (keyboard_check_pressed(vk_space)){
	velocidade = 5;
	index      = 0;	
	var ponto  = ds_list_find_value(lista, index);
	destinox = ponto.x;
	destinoy = ponto.y; 
}



//Recuperando o total de elementos na lista
var total = ds_list_size(lista);

//Movimenta somente se tiver elementos na lista
if (total > 0){
	var dist = point_distance(x, y, destinox, destinoy);

	if dist >= 10
		move_towards_point(destinox, destinoy, velocidade)
	else{
		/*Atualiza o índice para buscar o 
		próximo ponto
		*/
		index++;
		
		
		//A função clamp é utiliza para colocar
		//o limite entre dois valores dada um valor
		index = clamp(index, 0, total-1);
		
		ponto = ds_list_find_value(lista, index);		
		
		destinox   = ponto.x;
		destinoy   = ponto.y;
		
		
	}
}


