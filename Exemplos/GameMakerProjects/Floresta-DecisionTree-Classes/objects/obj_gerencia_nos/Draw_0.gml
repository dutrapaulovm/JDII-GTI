/// @description Insert description here
// You can write your code in this editor
draw_set_font(fnt_texto);
draw_set_halign(fa_center);

if (is_instanceof(no_raiz, NoDecisaoFloresta)){
	draw_text(room_width / 2, (room_height / 2)-64, no_raiz.pergunta);	
}
else
	if (is_instanceof(no_raiz, NoAcaoFloresta)){
		if (no_raiz.escrever_texto){
			draw_text(room_width / 2, (room_height / 2)-32, "Reposta: " + resposta);
			draw_text(room_width / 2, room_height / 2, no_raiz.texto);
		}
	}