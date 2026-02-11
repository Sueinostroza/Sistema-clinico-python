""" Módulo de gestión de pacientes para un sistema clínico.
    Contiene las funciones de registro, visualización, búsqueda, calculo de valores y eliminación de pacientes."""
#Lista que almacena los pacientes
pacientes=[]
#Diccionario para relacionar el código de previsión médica con el nombre correspondiente
prevision_medica={
            1:"Fonasa",
            2:"Isapre",
            3:"Particular"
}
#Set para evitar el registro de pacientes con nombres duplicados
nombres_registrados=set()

def contar_pacientes(lista):
    """Función recursiva que cuenta la cantidad de pacientes registrados en la clínica"""
    if not lista:
        return 0
    return 1 + contar_pacientes(lista[1:])

def registrar_paciente():
    """Función que permite registrar nuevos pacientes en el sistema.
    Valida que el nombre no esté duplicado y asigna un ID único a cada paciente registrado""" 
    print("---Registrar paciente----")
    nombre_paciente=input("Ingrese el nombre completo del paciente: ").strip().upper()
    if nombre_paciente in nombres_registrados:
        print("⚠️ Ya existe un paciente con ese nombre")
        return
    while True:
        try:
            print("Seleccione la previsión médica")
            prevision=int(input('''
                    1.-Fonasa
                    2.-Isapre
                    3.-Particular
                    Ingrese una opcion:  '''))
            if prevision not in prevision_medica:
                print("Opción inválida")
                continue
            break
        except ValueError:
            print("🔺 Ingrese una opción válida")

    nuevo_id=len(pacientes)+1
    paciente={
    "id":nuevo_id,
    "nombre":nombre_paciente,
    "prevision":prevision
        }
    pacientes.append(paciente)
    nombres_registrados.add(nombre_paciente)
    print(f"El paciente {nombre_paciente} fue registrado correctamente ✅")

def mostrar_pacientes():
    """Función que permite mostrar todos los pacientes registrados en el sistema"""
    print("### Mostrar pacientes ###")
    if len(pacientes)==0:
        print("🔺 No hay pacientes registrados")
        return
    for paciente in pacientes:
        print(f"ID:{paciente['id']} Paciente: {paciente['nombre']} Previsión médica: {prevision_medica[paciente['prevision']]}")

def buscar_paciente_nombre():
    """Función que permite buscar pacientes por nombre en caso de no conocer el ID """
    if len(pacientes)==0:
        print("🔺 No hay pacientes registrados")
        return None
    print("### Buscar paciente por nombre ###")
    buscar_nombre=input("Ingrese el nombre del paciente a buscar: ").strip().upper()
    encontrado=False
    for paciente in pacientes:
        if paciente['nombre'].strip().upper()==buscar_nombre:
            print("Resultado de la búsqueda: ")
            print(f"ID: {paciente['id']} Paciente: {paciente['nombre']} Previsión médica: {prevision_medica[paciente['prevision']]}")
            encontrado=True
            break
    if not encontrado:
        print("❌ No se encontró ningún paciente con ese nombre")

def buscar_paciente_id():
    """Función que permite buscar pacientes por su ID. Se utiliza este método para evitar confusiones en caso de pacientes con nombres similares"""
    if len(pacientes)==0:
        print("🔺 No hay pacientes registrados")
        return None
    print("### Buscar paciente por ID ###")
    while True:
        try:
            paciente_id=int(input("Ingrese el ID del paciente: "))
            break
        except ValueError:
            print("🔺 Ingrese un número válido")
    for paciente in pacientes:
        if paciente['id']==paciente_id:
            print("Resultado de la búsqueda: ")
            print(f"ID: {paciente['id']} Paciente: {paciente['nombre']} Previsión médica: {prevision_medica[paciente['prevision']]}")
            return paciente
    print("❌ No se encontró un paciente con ese ID")
    return None

def valor_a_pagar():
    """Función que calcula el valor total a pagar por una consulta médica.
    El cálculo depende del tipo de consulta seleccionada y de la previsión médica del paciente, aplicando el descuento correspondiente"""
    if len(pacientes)==0:
        print("🔺 No hay pacientes registrados")
        return
    paciente=buscar_paciente_id()
    if paciente is None:
        return
    valor_consulta={
        1:21000,
        2:30000
    }
    tabla_descuento={
        "Fonasa":0.7,
        "Isapre":0.9,
        "Particular":0.0
    }
    tipos_consulta=(
        "1.-Consulta general",
        "2.-Consulta especialidad"
    )
    print("### Valor consulta médica ###")
    while True:
        try:
            for tipo in tipos_consulta:
                print(tipo)
            consulta=int(input("Ingrese una opción numérica: "))
            if consulta not in valor_consulta:
                print("🔺 Ingrese una opción válida 1 o 2")
                continue
            break
        except ValueError:
            print("🔺 Ingrese un número válido: ")
    #Obtiene la previsión del paciente según el código registrado
    prevision=prevision_medica[paciente['prevision']]
    valor_base=valor_consulta[consulta]
    descuento=tabla_descuento[prevision]

    valor_final=int(valor_base*(1-descuento))

    print(f'''
          Paciente: {paciente['nombre']}
          Previsión: {prevision}
          Valor a pagar: ${valor_final}
          ''')

def eliminar_usuario_id():
    """Función de permite eliminar un paciente del sistema mediante su ID.
    Se definió asi para evitar cometer errores de eliminación en caso de pacientes con nombres similares"""
    if len(pacientes)==0:
        print("🔺 No hay pacientes registrados")
        return None
    print("### Eliminar paciente por ID ###")
    encontrado=False
    while True:
        try:
            eliminar_paciente=int(input("Ingrese ID del paciente a eliminar: "))
            break
        except ValueError:
            print("🔺 Favor ingrese solo números")
            
    for paciente in pacientes:
        if paciente['id']==eliminar_paciente:
            encontrado=True
            print(f"Se ha encontrado al paciente nombre: {paciente['nombre']} y su Previsión médica: {prevision_medica[paciente['prevision']]}")
            while True:
                decision=input(f"¿Esta seguro de eliminar al paciente:si/no: ").upper()    
                if decision=="SI":
                    pacientes.remove(paciente)
                    nombres_registrados.remove(paciente['nombre'])
                    print("Paciente eliminado correctamente ✅ ")
                    break
                elif decision=="NO":
                    print("El paciente no fue eliminado")
                    break
                else:
                    print("🔺 Opción inválida, ingrese SI o NO")
            break
    if not encontrado:
        print("❌ No se encontró el paciente con ese n° de ID")


        




    





