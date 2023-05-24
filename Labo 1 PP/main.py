from funciones import *
import os

flag_descarga_archivo_csv = False
flag_carga_archivo_json = False

while True:
    os.system("cls")                        #Limpio pantalla
    
    #Logica del menu
    match menu():
        case 1:                             #Carga en lista de archivo csv 
            catalogo = []
            descargar_de_csv(catalogo, "C:\\Users\\TOM\\Desktop\\Python C1\\Labo 1 PP\\insumos.csv")
            flag_descarga_archivo_csv = True
        case 2:                             #Listar cantidad por marca
            if flag_descarga_archivo_csv:
                contador_marcas = contador_cantidades(catalogo, "MARCA", extraer_valores_por_clave(catalogo, "MARCA", True))
                mostrar_diccionario(contador_marcas, "CANTIDAD POR MARCA")
            else:
                print("Primero se debe cargar el archivo csv en la lista, ingrese a la opcion 1")    
        case 3:                             #Listar insumos por marca
            if flag_descarga_archivo_csv:
                listar_catalogo_por(catalogo, "MARCA", extraer_valores_por_clave(catalogo, "MARCA", True))
            else:
                print("Primero se debe cargar el archivo csv en la lista, ingrese a la opcion 1")
        case 4:                             #Buscar insumo por caracteristica
            if flag_descarga_archivo_csv:
                mostrar_catalogo(buscar_por_caracteristica(catalogo))
            else:
                print("Primero se debe cargar el archivo csv en la lista, ingrese a la opcion 1")
        case 5:                             #Listar insumos ordenados
            if flag_descarga_archivo_csv:
                catalogo_una_caracteristica = catalogo_con_primer_caracteristica(catalogo)
                ordenar_catalogo_criterio_y_precio(catalogo_una_caracteristica, "MARCA", "PRECIO")
                mostrar_catalogo(catalogo_una_caracteristica)
            else:
                print("Primero se debe cargar el archivo csv en la lista, ingrese a la opcion 1")
        case 6:                             #Realizar compras
            if flag_descarga_archivo_csv:
                total = realizar_compras(catalogo)
                print(f"El total de la compra es: ${total}")
            else:
                print("Primero se debe cargar el archivo csv en la lista, ingrese a la opcion 1")
        case 7:                             #Guardar en formato JSON 
            if flag_descarga_archivo_csv:
                catalogo_alimentos = catalogo_solo_alimentos(catalogo)
                cargar_a_json(catalogo_alimentos, "Labo 1 PP\\catalogo_alimentos.json")
                flag_carga_archivo_json = True
            else:
                print("Primero se debe cargar el archivo csv en la lista, ingrese a la opcion 1")
        case 8:                             #Leer desde formato JSON
            if flag_carga_archivo_json:
                lista_json = descargar_de_json("Labo 1 PP\\catalogo_alimentos.json")
                mostrar_catalogo(lista_json)
            else:
                print("Primero se debe cargar el archivo json con el catalogo, ingrese a la opcion 7")
        case 9:                             #Actualizar precios
            if flag_descarga_archivo_csv:
                catalogo_precios_nuevos = aumento_precios(catalogo)
                cargar_a_csv(catalogo_precios_nuevos, "Labo 1 PP\\insumos.csv")
                flag_descarga_archivo_csv = False
            else:
                print("Primero se debe cargar el archivo csv en la lista, ingrese a la opcion 1")   
        case 10:                            #Salir
            salir = input("Confirma la salida? s/n: ")
            if salir == "s":
                break
    
    #pauso la terminal
    os.system("pause")

