def convertir_mapa_a_matriz(laberinto):
    return [list(fila) for fila in laberinto.split("\n")]

def mostrar_mapa(mapa):
    print('\n'.join(''.join(fila) for fila in mapa))

def main_loop(mapa, inicio, final):
    px, py = inicio
    fx, fy = final
    while (px, py) != (fx, fy):
        mapa[px][py] = 'P'
        mostrar_mapa(mapa)
        movimiento = input("Movimiento (w/a/s/d): ")
        dx, dy = 0, 0
        if movimiento == 'w':
            dx = -1
        elif movimiento == 's':
            dx = 1
        elif movimiento == 'a':
            dy = -1
        elif movimiento == 'd':
            dy = 1
        if (0 <= px + dx < len(mapa)) and (0 <= py + dy < len(mapa[0])) and mapa[px + dx][py + dy] != '#':
            mapa[px][py] = '.'
            px += dx
            py += dy

laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""
mapa = convertir_mapa_a_matriz(laberinto)
inicio = (0, 0)
final = (len(mapa)-1, len(mapa[0])-1)
main_loop(mapa, inicio, final)
