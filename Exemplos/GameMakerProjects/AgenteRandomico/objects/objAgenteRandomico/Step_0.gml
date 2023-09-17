/// @description Insert description here
// You can write your code in this editor

var dist = point_distance(x, y, destinox, destinoy);

if dist >= 10
	move_towards_point(destinox, destinoy, velocidade)
else{
	destinox   = random_range(64, room_width-64);
	destinoy   = random_range(64, room_height-64);
}


