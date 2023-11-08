/// @description Insert description here
// You can write your code in this editor

/*A função draw_self() desenha o sprite do objeto
na tela. Devemos chamar essa função sempre que for
preciso utilizar o evento Draw e o possua algum
sprite associado.
*/
draw_self();
var dist = point_distance(x, y, obj_ponto.x, obj_ponto.y);

draw_text(x, y, estado_str);
draw_text(x, y+16, string(direction));
draw_text(x, y+32, string(destinox) + "," + string(destinoy) );
draw_text(x, y+48, string(dist))






