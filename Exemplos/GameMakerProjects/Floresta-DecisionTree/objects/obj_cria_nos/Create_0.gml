/// @description Insert description here
// You can write your code in this editor
no_acao_atravessar = instance_create_layer(x, y, "Instances", obj_no_acao);
no_acao_atravessar.texto = "Atravessar Floresta com segurança!";

no_acao_nao_atravessar = instance_create_layer(x, y, "Instances", obj_no_acao);
no_acao_nao_atravessar.texto = "Fica com medo e não consegue atravessar!";

no_raiz = instance_create_layer(x,y,"Instances", obj_no_decisao);
no_raiz.pergunta = "Você chegou na floresta. Usar lanterna?";

no_raiz.no_acao_sim = no_acao_atravessar
no_raiz.no_acao_nao = no_acao_nao_atravessar
instance_deactivate_object(obj_no_acao);

/*
no_acao_atravessar.visible	   = false;
no_acao_nao_atravessar.visible = false;*/



