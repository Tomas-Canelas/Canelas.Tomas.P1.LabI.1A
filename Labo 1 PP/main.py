from funciones import *
import os

while True:
    os.system("cls")                        #Limpio pantalla
    
    #Logica del menu
    match menu():
        case 1:                             #Carga en lista de archivo csv 
            catalogo = []
            cargar_datos_csv(catalogo, "C:\\Users\\TOM\\Desktop\\Python C1\\Labo 1 PP\\insumos.csv")
        case 2:                             #Listar cantidad por marca
            contador_marcas = contador_cantidades(catalogo, "MARCA", extraer_valores_por_clave(catalogo, "MARCA", True))
            mostrar_diccionario(contador_marcas, "CANTIDAD POR MARCA")
        case 3:                             #Listar insumos por marca
            listar_catalogo_por(catalogo, "MARCA", extraer_valores_por_clave(catalogo, "MARCA", True))
        case 4:                             #Buscar insumo por caracteristica
            mostrar_catalogo(buscar_por_caracteristica(catalogo))
        case 5:                             #Listar insumos ordenados
            catalogo_una_caracteristica = catalogo_con_primer_caracteristica(catalogo)
            ordenar_catalogo_criterio_y_precio(catalogo_una_caracteristica, "MARCA", "PRECIO")
            mostrar_catalogo(catalogo_una_caracteristica)
        case 6:                             #Realizar compras
            marca = "Pedigree"
            aux = list(filter(lambda insumo: insumo["MARCA"] == marca, catalogo))
            print(aux)
        case 7:                             #Guardar en formato JSON 
            pass
        case 8:                             #Leer desde formato JSON
            pass
        case 9:                             #Actualizar precios
            pass
        case 10:                             #Salir
            salir = input("Confirma la salida? s/n: ")
            if salir == "s":
                break
    
    #pauso la terminal
    os.system("pause")

