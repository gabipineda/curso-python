import os
import keyboard

def borrar_e_imprimir(num):
    os.system('cls' if os.name=='nt' else 'clear')
    print(num)

def main():
    num = 0
    while num <= 50:
        if keyboard.is_pressed('n'):  # si se presiona la tecla 'n'
            num += 1
            borrar_e_imprimir(num)

main()
