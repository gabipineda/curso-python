import os
import msvcrt

def imprimir_numero(n):
    os.system('cls' if os.name=='nt' else 'clear')
    print(n)

def main():
    n = 0
    while n < 50:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'n':
                n += 1
                imprimir_numero(n)

if __name__ == "__main__":
    main()