from MapaGame import *

if __name__ == "__main__":

    mapa = np.array([ [-9,-9,-9,-9,-9,-9,-9,-9],
                      [-9, 0, 0, 0, 0, 0, 0,-9],
                      [-9, 0, 0, 0, 0, 0, 0,-9],
                      [-9, 0, 0,-9, 0,-9, 0,-9],
                      [-9, 0, 0,-9, 0, 0, 0,-9],
                      [-9,-9, 0,-9, 0, 0, 0,-9],
                      [-9, 0, 6,-9, 0, 0, 3,-9],
                      [-9,-9,-9,-9,-9,-9,-9,-9] ])

    mapa = np.array([  [-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9],
                       [-9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,-9],
                       [-9, 0, 0, 0, 0,-9, 0, 0, 0, 0, 0,-9],
                       [-9, 0, 0,-9, 0,-9, 0, 0, 0, 0, 0,-9],
                       [-9, 0, 0,-9, 0,-9, 0,-9,-9,-9, 0,-9],
                       [-9,-9, 0,-9, 0,-9, 0,-9,-9, 0, 0,-9],
                       [-9, 0, 6,-9, 0, 0, 0, 0, 0, 0, 3,-9],
                       [-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9,-9] ])   

    mapa = np.array([  [0,0,0,0,0,0,0,0,0,0],
                       [0,1,0,1,1,1,1,1,1,1],
                       [0,0,0,1,0,1,0,1,0,1],
                       [0,1,1,1,1,1,0,1,1,1],
                       [0,1,0,1,0,0,0,1,0,1],
                       [0,1,1,1,1,1,1,1,1,1],
                       [0,1,0,1,0,1,0,1,0,1],
                       [0,1,0,1,1,1,1,1,0,1]])

    rows, cols = mapa.shape
    print(mapa.shape)    
    mapaGame = MapaGame(rows=rows, cols=cols, border=False)
    mapaGame.create_map(mapa)
    mapaGame.origem      = (6,2)   #Posição de origem
    mapaGame.destino     = (6,10)  #Posição de destino      
    mapaGame.tick_agent  = 0.1     #Indica o tempo de espera do agente para executar o próximo movimento
    mapaGame.show_matriz = True    #Exibe os valores da matriz no cenário 

    while(True):        

        if not mapaGame.reached:
            mapaGame.verifica_caminho(mapaGame.origem, mapaGame.destino)   
        
        mapaGame.update()
        mapaGame.render()