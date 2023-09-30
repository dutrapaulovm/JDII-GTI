//Criando os nós de ação
no_acao_atravessar = new NoAcaoAtravessar();
no_acao_atravessar.texto = "Atravessar Floresta com segurança!";

no_acao_naoatravessar = new NoAcaoNaoAtravessar();
no_acao_naoatravessar.texto = "Fica com medo e não consegue atravessar!";

//Criando os nós de decisão
no_raiz = new NoDecisaoFloresta()
no_raiz.pergunta = "Você chegou na floresta. Usar lanterna?";
//Associando os nós filhos a raiz
no_raiz.no_sim = no_acao_atravessar;
no_raiz.no_nao = no_acao_naoatravessar;

acao_executada = false;