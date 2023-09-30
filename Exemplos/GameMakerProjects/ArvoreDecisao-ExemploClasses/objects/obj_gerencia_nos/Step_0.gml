/*
Atualizamos o nó raiz para que possamos
utilizar o próximo nó avaliado durante a 
decisão
*/
if (is_instanceof(no_raiz, NoDecisao)){
	no_raiz = no_raiz.tomar_decisao();
}

if (is_instanceof(no_raiz, NoAcao)){
	no_raiz.tomar_decisao();
}








