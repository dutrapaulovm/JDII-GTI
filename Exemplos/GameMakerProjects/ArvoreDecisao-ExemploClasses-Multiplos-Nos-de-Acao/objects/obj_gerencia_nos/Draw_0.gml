//Alterando o alinhamento do texto
draw_set_halign(fa_center);
draw_text(96, 96, string((delta_time / 10000)));
if is_instanceof(no_raiz, NoDecisao){
	draw_text(room_width / 2, room_height / 2, no_raiz.pergunta);
}
else
	if is_instanceof(no_raiz, NoAcao){
		draw_text(room_width / 2, room_height / 2, no_raiz.texto);	
	}











