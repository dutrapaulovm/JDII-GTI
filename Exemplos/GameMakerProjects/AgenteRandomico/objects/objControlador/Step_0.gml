/// @description Insert description here
// You can write your code in this editor

if mouse_check_button_pressed(mb_left){
	var inst = instance_create_layer(mouse_x, mouse_y, "Base", obj_ponto);
	ds_list_add(lista, inst);
}
num_pontos = instance_number(obj_ponto);


