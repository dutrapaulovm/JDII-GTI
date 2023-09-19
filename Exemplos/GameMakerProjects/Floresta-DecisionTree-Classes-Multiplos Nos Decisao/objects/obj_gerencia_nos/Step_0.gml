/// @description Insert description here
// You can write your code in this editor
if (is_instanceof(no_raiz, NoDecisaoFloresta)){
	no_raiz = no_raiz.tomar_decisao();
}

/*Caso a decisão chegue no último nó, neste caso, o no
de ação é necessário verificar se o nó retornado é do tipo
ação para ser executado logo em seguida.
*/
if (is_instanceof(no_raiz, NoAcaoFloresta)){
	no_raiz.tomar_decisao();
}