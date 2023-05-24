import re

def menu() -> int:
    """Imprime el menu y pide una opcion 

    Returns:
        int: opcion del menu elegida
    """    
    print("""
    ╔════════════════════════════════════════════════════════╗
    ║       ADMINISTRACION INSUMOS TIENDA DE MASCOTAS        ║ 
    ╠════╦═══════════════════════════════════════════════════╣
    ║  1 ║ Cargar datos desde archivo csv                    ║
    ║  2 ║ Listar cantidad por marca                         ║
    ║  3 ║ Listar insumos por marca                          ║
    ║  4 ║ Buscar insumo por caracteristica                  ║       
    ║  5 ║ Listar insumos ordenados por marca                ║   
    ║  6 ║ Realizar compras                                  ║
    ║  7 ║ Guardar en formato JSON                           ║
    ║  8 ║ Leer desde formato JSON                           ║
    ║  9 ║ Actualizar precios                                ║
    ║ 10 ║ Salir                                             ║
    ╚════╩═══════════════════════════════════════════════════╝""")
    
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
        except ValueError:
            print("Solo pueden ingresarse opciones numericas entre 1-10")
            continue
        
        if opcion > 0 and opcion <= 10:
            return opcion
        else:
            print(f"La opcion numero {opcion} no existe.")

def cargar_datos_csv(lista: list, archivo: str) -> None:
    """Carga los datos de un archivo csv a una lista de diccionarios

    Args:
        lista (list): lista vacia que se desea cargar con los datos del archivo
        archivo (str): csv con los datos necesarios 
    """    
    with open(archivo, "r", encoding= "UTF-8") as file:
        keys = re.findall(r'\w+', file.readline().strip("\n"))
        for linea in file:
            item = {}
            linea = linea.strip("\n").split(",")
            for i in range(len(keys)):
                item[keys[i]] = linea[i]
            lista.append(item)

def mostrar_insumo(insumo: dict) -> None:
    """Muestra un insumo de tipo diccionario en forma de fila

    Args:
        insumo (dict): elemento que se va a mostrar
    """    
    print(f"║{insumo['ID']:^4s}║{insumo['NOMBRE']:^35s}║{insumo['MARCA']:^25s}║{insumo['PRECIO']:^10s}║{insumo['CARACTERISTICAS']:^90s}║")

def mostrar_catalogo(catalogo: list) -> None:
    """Muestra una lista en formato de lista

    Args:
        catalogo (list): lista de diccionarios que se va a mostrar con encabezados
    """    
    print("╔════╦═══════════════════════════════════╦═════════════════════════╦══════════╦══════════════════════════════════════════════════════════════════════════════════════════╗")
    print("║ ID ║               NOMBRE              ║          MARCA          ║  PRECIO  ║                                     CARACTERISTICAS                                      ║")
    print("║════║═══════════════════════════════════║═════════════════════════║══════════║══════════════════════════════════════════════════════════════════════════════════════════║")
    for insumo in catalogo:
        mostrar_insumo(insumo)
        print("║════║═══════════════════════════════════║═════════════════════════║══════════║══════════════════════════════════════════════════════════════════════════════════════════║")

def extraer_valores_por_clave(lista: list, clave: str, sin_repe = False) -> list:
    """Reduce una lista de diccionarios a una lista simple mediante una clave

    Args:
        lista (list): lista de diccionarios 
        clave (str): clave del diccionario de la cual se extraen los valores
        sin_repe (bool, optional): True -> devuelve una lista sin repetidos | Defaults False -> devuelve una lista con repetidos.

    Returns:
        list: lista de los valores que extraemos de la lista de diccionarios mediante una clave
    """    
    lista_reducida = list(map(lambda item: item[clave], lista))
    if sin_repe:
        lista_reducida = list(set(lista_reducida))
        
    return lista_reducida

def contador_cantidades(lista_principal: list, clave: str, lista_comparacion: list) -> dict:
    """Cuenta la cantidad de elementos que tienen el mismo valor en una clave en especifico

    Args:
        lista_principal (list): lista de diccionarios
        clave (str): clave del diccionarios con la que vamos a acceder a los valores
        lista_comparacion (list): lista de valores que vamos a comparar

    Returns:
        dict: diccionario de contadores resultantes de la comparacion
    """    
    contadores = {}
    for item in lista_comparacion:
        contadores[item] = 0
        
    for elemento in lista_principal:
        for item in lista_comparacion:
            if elemento[clave] == item:
                contadores[item] += 1
                
    return contadores

def mostrar_diccionario(dict: dict, titulo: str) -> None:
    """Muestra las claves y valores de un diccionario con un titulo a eleccion

    Args:
        dict (dict): diccionario que se desea mostrar
        titulo (str): titulo del listado que se va a imprimir
    """    
    claves = dict.keys()
    print(f"    {titulo}")
    print("-----------------------------------------")
    for clave in claves:
        print(f"| {clave}: {dict[clave]}")

def listar_catalogo_por(catalogo: list, clave: str, lista_tipo: list) -> None:
    """Lista un catalogo filtrando algun elemento del mismo 

    Args:
        catalogo (list): catalogo que se va a mostrar
        clave (str): elemento del catalogo por el que vamos a filtrar
        lista_tipo (list): lista de elementos para comparar con el catalogo y poder mostrarlo filtrado 
    """    
    for item in lista_tipo:
        print(f"{item:^165s}")
        print("╔════╦══════════════════════════════╦═════════════════════════╦══════════╦══════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║ ID ║            NOMBRE            ║          MARCA          ║  PRECIO  ║                                     CARACTERISTICAS                                      ║")
        print("║════║══════════════════════════════║═════════════════════════║══════════║══════════════════════════════════════════════════════════════════════════════════════════║")

        for insumo in catalogo:
            if insumo[clave] == item:
                mostrar_insumo(insumo)
        print("╚════╩══════════════════════════════╩═════════════════════════╩══════════╩══════════════════════════════════════════════════════════════════════════════════════════╝\n")

def buscar_por_caracteristica(catalogo: list) -> list:
    """Muestra el catalogo original y permite al usuario ingresar 
    una caracteristica, luego muestra todos los insumos que tengan esa 
    caracteristica

    Args:
        catalogo (list): lista con los insumos

    Returns:
        list: lista filtrada con los insumos que tengan la caracteristica ingresada
    """    
    mostrar_catalogo(catalogo)
    caracteristica = input("\nIngrese la caracteristica que desea buscar en los insumos:")
    patron = re.compile(f"(^|~){caracteristica}(~|$)")
    
    lista_insumos_con_caracteristica = []
    
    for insumo in catalogo:
        if patron.search(insumo["CARACTERISTICAS"]):
            lista_insumos_con_caracteristica.append(insumo)
        
    return lista_insumos_con_caracteristica

def catalogo_con_primer_caracteristica(catalogo: list) -> list:
    """A partir del catalogo original devuelve una lista casi igual pero con una sola caracteristica de cada insumo

    Args:
        catalogo (list): lista original con las caracteristicas correspondientes por insumo

    Returns:
        list: catalogo con 1 sola caracteristica por insumo
    """    
    catalogo_aux = []
    for insumo in catalogo:
        catalogo_aux.append(insumo.copy())
    
    patron = re.compile("^[\w ]+")
    for insumo in catalogo_aux:
        caracteristica1 = patron.search(insumo["CARACTERISTICAS"])
        caracteristica1 = re.sub("~", "", caracteristica1.group())
        insumo["CARACTERISTICAS"] = caracteristica1

    return catalogo_aux

def ordenar_catalogo_criterio_y_precio(catalogo: list, criterio_uno: str, precio: str) -> None:
    """Ordena ascendentemente un catalogo por un primer criterio y en caso de igualdad, ordena descendentemente por precio

    Args:
        catalogo (list): catalogo que vamos a ordenar
        criterio_uno (str): campo por el cual vamos a ordenar ascendentemente
        precio (str): en caso de igualdad, este campo precio ordena descendentemente
    """    
    for i in range(len(catalogo) - 1):
        for j in range(i + 1, len(catalogo)):
            if catalogo[i][criterio_uno] > catalogo[j][criterio_uno] or (catalogo[i][criterio_uno] == catalogo[j][criterio_uno] and float(re.sub("\\$", "", catalogo[i][precio])) < float(re.sub("\\$", "", catalogo[j][precio]))):
                aux = catalogo[i]
                catalogo[i] = catalogo[j]
                catalogo[j] = aux