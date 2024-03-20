import readchar

print("Presiona una tecla (para salir presiona la tecla ↑):")

while True:
    caracter = readchar.readkey()
    if caracter == readchar.key.UP:
        break
    else:
        print(f"Has presionado: {caracter}")

print("Has salido del programa.")
