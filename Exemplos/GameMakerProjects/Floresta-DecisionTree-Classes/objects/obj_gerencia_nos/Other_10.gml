/// @description Insert description here
// You can write your code in this editor
no_acao_atravessar = new NoAcaoFloresta();
no_acao_atravessar.texto = "Atravessar Floresta com segurança!";

no_acao_nao_atravessar = new NoAcaoFloresta();
no_acao_nao_atravessar.texto = "Fica com medo e não consegue atravessar!";

no_raiz  = new NoDecisaoFloresta();
no_raiz.pergunta   = "Você chegou na floresta. Usar lanterna?";
no_raiz.no_sim  = no_acao_atravessar;
no_raiz.no_nao = no_acao_nao_atravessar;

resposta  = ""
reiniciar = false;

instance_activate_object(obj_botao);