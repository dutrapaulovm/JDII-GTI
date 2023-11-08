/// @description Insert description here
// You can write your code in this editor
randomize()
//Controla a velocidade do objeto
velocidade	   = 2;
//Define se o objeto esta invertido
//ver script ia_agente
esta_invertido = false;

//Gera uma posição inicial alvo para o objeto
destinox   = random_range(64, room_width-64);
destinoy   = random_range(64, room_height-64);

//Criando o no de ação patrulhar
no_acao_patrulhar = new NoAcaoPatrulhar(); 
no_acao_patrulhar.m_agente = self;

//Criando o nó de ação inverter direção
no_acao_inverter = new NoAcaoInterverDir();
no_acao_inverter.m_agente = self;

no_esta_invertido = new NoNaoEstaInvertido();
no_esta_invertido.no_sim = no_acao_patrulhar


//Criando o nó de decisão EstaPerto
no_esta_perto = new NoEstaPerto();
no_esta_perto.m_agente = self;
no_esta_perto.no_sim = no_acao_inverter;
no_esta_perto.no_nao = no_esta_invertido;

//Criando o Nó Raiz
no_raiz = new NoEstaLonge();
//Referenciando o objeto atual que esta sendo
//criado na cena
no_raiz.m_agente  = self; 

//Vinculando os nós(Ação ou Decisão) a raiz
no_raiz.no_sim = no_acao_patrulhar
//Vinculando o nó de decisão
no_raiz.no_nao = no_esta_perto;

//Inicialmente definimos o no raiz como atual
no_atual = no_raiz

//A condição do no não está invertido quando
//é falso deve retornar para a raiz
no_esta_invertido.no_nao = no_raiz

