/// @description Insert description here
// You can write your code in this editor
//Desativa os objetos na cena
if ( (obj_tempo.status_tempo == "Dia") || (resposta == "Sim") ){	
	instance_deactivate_object(no_acao_nao);
	instance_activate_object(no_acao_sim);
	/*
	no_acao_nao.visible = false;
	no_acao_sim.visible = true;*/
}
else
	if (resposta == "Não"){
		instance_deactivate_object(no_acao_sim);
		instance_activate_object(no_acao_nao);
		/*no_acao_sim.visible = false;
		no_acao_nao.visible = true;*/
	}
	
//resposta = ""	

