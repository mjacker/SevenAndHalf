from random import random
from cards import cards
from player import player
from resourses import recibir_nombre, recibir_eleccion_num
import random
from banca import checkWinner
import menu as mn 



def playSAH():
    # iniciando constructores
    deck = cards()

    jugadores = [] 

    # Asking how many players will play
    mn.cantidadJugadores()
    N = recibir_eleccion_num(2, 4)
    print("N-jugadores: ", N)
    # N = 2
    for i in range(0, N):
        exec("player{0} = player('{1}')".format(i, recibir_nombre(i + 1)))
        exec(f"jugadores.append(player{i})")

    z = 0  
    while z<300: # for the moment checking only thrree rounds
        for i in range(0, N):
            print("juega: ", jugadores[i].player_name)
            if i < N - 1:
                jugadores[i].jugadorTurn(deck)
            elif i == N - 1:
                jugadores[i].bancaTurn(deck) #original

        print(
            """
+ ---------------------------------------------------- +
+ -------------- Resultados de la mesa --------------- +""")
        for i in range(0, N-1):
            if jugadores[i].player_score <= jugadores[-1].player_score and jugadores[i].player_score != 0.0 and jugadores[-1].player_score != 0.0:
                print(f"\n##{jugadores[i].player_name}## perdió contra ##{jugadores[-1].player_name}## siendo la Banca.")
                jugadores[i].player_coins -= 10
                jugadores[-1].player_coins += 10
                print(f"Pierde 10 monedas y se queda con {jugadores[i].player_coins}.")
            elif jugadores[i].player_score > jugadores[-1].player_score:
                print(f"\n##{jugadores[i].player_name}## le ganó a ##{jugadores[-1].player_name}## siendo la Banca.")
                jugadores[i].player_coins += 20
                jugadores[-1].player_coins -= 20
                print(f"\Gana 20 monedas y se queda con {jugadores[i].player_coins} monedas.")

        print("TEMP")
        for x in jugadores:
            print(x.getData())
        print("TEMP")

        # reset score for next round.
        for i in  jugadores:
            i.setScore(0.0)

        print("TERMINA PRIMERA RONDA")
        z += 1 
        input("press any key to continue next round...")