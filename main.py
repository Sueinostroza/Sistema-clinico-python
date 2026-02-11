""" Proyecto de modulo: Sistema de gestión de pacientes de una clínica
Autor:Susan Inostroza A.

Descripción:
El programa permite el registro de nuevos pacientes en una clínica, almacenando su nombre y previsión de salud. Permite visualizar, buscar y eliminar pacientes, además de calcular el valor de una atención médica según el tipo de consulta y previsión de salud del paciente. """

from sistema_clinico.menu import mostrar_menu
from sistema_clinico import gestion_pacientes

def main():
    while True:
        mostrar_menu()
        total=gestion_pacientes.contar_pacientes(
            gestion_pacientes.pacientes
        )
        print(f"\n Pacientes registrados actualmente: {total}")
       
        opcion=input("Ingrese una opción: ")
        if opcion=="1":
            gestion_pacientes.registrar_paciente()
        elif opcion=="2":
            gestion_pacientes.mostrar_pacientes()
        elif opcion=="3":
            gestion_pacientes.buscar_paciente_nombre()
        elif opcion=="4":
            gestion_pacientes.buscar_paciente_id()
        elif opcion=="5":
            gestion_pacientes.valor_a_pagar()
        elif opcion=="6":
            gestion_pacientes.eliminar_usuario_id()
        elif opcion=="7":
            print("Saliendo del sistema..")
            break
        else:
            print("🔺 La opción ingresada no es válida")

if __name__ =="__main__":
    main()

