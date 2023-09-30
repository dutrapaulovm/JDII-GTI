/// @description Insert description here
/*A função draw_self é utilizada para desenhar
o sprite novamente.
*/
draw_self();
//Escrevendo o texto em cima do sprite
//Pegando a cor atual
var _old_color = draw_get_color();
//Definindo uma nova cor
draw_set_color(c_black);
//Alinhando e escrevendo o texto
draw_set_halign(fa_center);
draw_text(x, y, rotulo);
//Definindo a cor antiga novamente
draw_set_color(_old_color);







