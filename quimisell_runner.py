#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
QUIMISELL - LANZADOR INTERACTIVO DE MÉTODOS NUMÉRICOS
================================================================================
Este script proporciona un menú interactivo en consola para explorar y ejecutar
fácilmente cualquiera de los 60 métodos numéricos del curso sin necesidad de
escribir rutas manuales en la terminal.

Uso:
    python quimisell_runner.py
================================================================================
"""

import os
import sys
import subprocess

MODULOS = [
    {
        "dir": "01_introduccion_y_errores",
        "titulo": "Módulo 1: Introducción, Conversión de Bases y Teoría de Errores",
        "descripcion": "Representación de datos, punto flotante, errores y series de Taylor/Maclaurin."
    },
    {
        "dir": "02_interpolacion_y_regresion",
        "titulo": "Módulo 2: Interpolación Polinomial y Modelos de Regresión",
        "descripcion": "Newton, Lagrange, Neville, vecino cercano y regresiones multivariables."
    },
    {
        "dir": "03_raices_de_ecuaciones",
        "titulo": "Módulo 3: Raíces de Ecuaciones No Lineales (1D)",
        "descripcion": "Métodos cerrados y abiertos: Bisección, Regla Falsa, Newton-Raphson, Müller, Fractales."
    },
    {
        "dir": "04_sistemas_ecuaciones_lineales",
        "titulo": "Módulo 4: Sistemas de Ecuaciones Lineales y Matrices",
        "descripcion": "Gauss, Gauss-Jordan, LU, Cramer, Jacobi, Gauss-Seidel, SOR y balances de materia."
    },
    {
        "dir": "05_sistemas_no_lineales_y_calculo",
        "titulo": "Módulo 5: Sistemas No Lineales, Diferenciación e Integración",
        "descripcion": "Newton multivariable con Jacobiano, derivadas, Riemann, Simpson, Romberg y Gauss."
    },
    {
        "dir": "06_ecuaciones_diferenciales",
        "titulo": "Módulo 6: Ecuaciones Diferenciales Ordinarias (EDOs) y Parciales (EDPs)",
        "descripcion": "Euler modificado en CSTRs, RK4, diferencias finitas, Laplace 2D y Crank-Nicolson."
    }
]

BANNER = r"""
================================================================================
  ██████╗ ██╗   ██╗██╗███╗   ███╗██╗███████╗███████╗██╗     ██╗     
 ██╔═══██╗██║   ██║██║████╗ ████║██║██╔════╝██╔════╝██║     ██║     
 ██║   ██║██║   ██║██║██╔████╔██║██║███████╗█████╗  ██║     ██║     
 ██║▄▄ ██║██║   ██║██║██║╚██╔╝██║██║╚════██║██╔══╝  ██║     ██║     
 ╚██████╔╝╚██████╔╝██║██║ ╚═╝ ██║██║███████║███████╗███████╗███████╗
  ╚══▀▀═╝  ╚═════╝ ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚══════╝
     --- MÉTODOS NUMÉRICOS APLICADOS A LA CIENCIA E INGENIERÍA ---
================================================================================
"""

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def obtener_scripts_del_modulo(ruta_modulo):
    if not os.path.isdir(ruta_modulo):
        return []
    archivos = [f for f in sorted(os.listdir(ruta_modulo)) if f.endswith(".py") and not f.startswith("__")]
    return archivos

def menu_principal(base_dir):
    while True:
        limpiar_pantalla()
        print(BANNER)
        print(" Selecciona un módulo para explorar sus métodos:\n")
        
        for idx, mod in enumerate(MODULOS, start=1):
            print(f"  [{idx}] {mod['titulo']}")
            print(f"      -> {mod['descripcion']}\n")
        
        print("  [0] Salir")
        print("--------------------------------------------------------------------------------")
        
        opcion = input(" Ingrese una opción [0-6]: ").strip()
        
        if opcion == "0":
            print("\n ¡Gracias por utilizar QuimiSell Métodos Numéricos! Hasta pronto.\n")
            break
        
        if opcion.isdigit() and 1 <= int(opcion) <= len(MODULOS):
            idx_mod = int(opcion) - 1
            menu_modulo(base_dir, MODULOS[idx_mod])
        else:
            input("\n Opción inválida. Presione Enter para reintentar...")

def menu_modulo(base_dir, info_modulo):
    ruta_modulo = os.path.join(base_dir, info_modulo["dir"])
    scripts = obtener_scripts_del_modulo(ruta_modulo)
    
    while True:
        limpiar_pantalla()
        print(BANNER)
        print(f" >> {info_modulo['titulo']}")
        print(f" Carpeta: {info_modulo['dir']}/\n")
        
        if not scripts:
            print("  No se encontraron scripts .py en esta carpeta.")
            input("\n Presione Enter para regresar...")
            return

        for idx, script in enumerate(scripts, start=1):
            nombre_limpio = script.replace(".py", "").replace("_", " ").title()
            print(f"  [{idx:02d}] {script}")
        
        print("\n  [00] Regresar al menú principal")
        print("--------------------------------------------------------------------------------")
        
        opcion = input(f" Ingrese el número del script a ejecutar [1-{len(scripts)}]: ").strip()
        
        if opcion in ("0", "00"):
            break
        
        if opcion.isdigit() and 1 <= int(opcion) <= len(scripts):
            script_seleccionado = scripts[int(opcion) - 1]
            ruta_script = os.path.join(ruta_modulo, script_seleccionado)
            
            print(f"\n" + "="*80)
            print(f" EJECUTANDO: {script_seleccionado}")
            print("="*80 + "\n")
            
            try:
                # Ejecutar script con el intérprete de Python actual
                subprocess.run([sys.executable, ruta_script], check=False)
            except Exception as e:
                print(f"\n Error al ejecutar el script: {e}")
            
            print("\n" + "="*80)
            input(" Ejecución terminada. Presione Enter para continuar...")
        else:
            input("\n Opción inválida. Presione Enter para reintentar...")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        menu_principal(base_dir)
    except KeyboardInterrupt:
        print("\n\n Programa interrumpido por el usuario. Saliendo...\n")

if __name__ == "__main__":
    main()
