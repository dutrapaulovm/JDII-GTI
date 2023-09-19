/// @description Insert description here
// You can write your code in this editor
draw_self();

var old_color = draw_get_color();

draw_set_color(c_black);
draw_set_font(fnt_botao);
draw_set_halign(fa_center);
draw_text(x, y, texto);

draw_set_color(old_color);





