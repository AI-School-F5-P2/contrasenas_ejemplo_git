#! /usr/bin/env python3

#context manager
with open("contrasenas.txt", "r") as archivo_contrasenas:
    contrasena = archivo_contrasenas.read()
    print(contrasena)

#TODO: función que compare las contraseñas

#TODO: función main que controle el flujo del programa