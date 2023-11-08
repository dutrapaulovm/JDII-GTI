// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information

function ia_inverter_dir(){
	
	direction = 180 - direction; 
	//speed *= 1.05	
}

function ia_patrulhar(){
	var dist = point_distance(x, y, destinox, destinoy);

	if dist >= 10
		move_towards_point(destinox, destinoy, velocidade)
	else{
		randomize()
		destinox   = random_range(64, room_width-64);
		destinoy   = random_range(64, room_height-64);		
	}
}