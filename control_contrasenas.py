#! /usr/bin/env python3

#context manager
with open("contrasenas.txt", "r") as archivo_contrasenas:
    contrasena = archivo_contrasenas.read()
    print(contrasena)

#TODO: función que compare las contraseñas

def compara_contraseñas(contraseña_introducida, contraseña_correcta):
    return True if contraseña_introducida == contraseña_correcta else False

#TODO: función main que controle el flujo del programa

def main():
    print("Bienvenido a mi programa")
    print()
    print("Introduzca la contraseña")
    contraseña_usuario = input()
    print()
    
    if compara_contraseñas(contraseña_usuario, contrasena):
        print("Bienvenidx!!")
    else:
        print("MAAAAAAAAAL")
