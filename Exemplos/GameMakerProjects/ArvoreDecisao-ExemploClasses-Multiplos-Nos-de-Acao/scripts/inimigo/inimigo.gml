function Inimigo() constructor{
	
	nome  = "";
	forca = 100;
	inteligencia = 2;
	
	atacar = function(){
		
	}
	
	mover = function(_x, _y){
		x += _x
		y += _y
	}
	
}

function Troll() : Inimigo() constructor{
	
	mover = function(_x, _y){
		//Lógica do Troll
	}
}



