import re
import json
from functools import reduce

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
    ║ 10 ║ Agregar nuevo producto                            ║
    ║ 11 ║ Guardar datos actualizados en archivo             ║
    ║ 12 ║ Salir                                             ║
    ╚════╩═══════════════════════════════════════════════════╝""")
    
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
        except ValueError:
            print("Solo pueden ingresarse opciones numericas entre 1-10")
            continue
        
        if opcion > 0 and opcion <= 12:
            return opcion
        else:
            print(f"La opcion numero {opcion} no existe.")

def descargar_de_csv(lista: list, archivo: str) -> None:
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
        print("╔════╦═══════════════════════════════════╦═════════════════════════╦══════════╦══════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║ ID ║               NOMBRE              ║          MARCA          ║  PRECIO  ║                                     CARACTERISTICAS                                      ║")
        print("║════║═══════════════════════════════════║═════════════════════════║══════════║══════════════════════════════════════════════════════════════════════════════════════════║")

        for insumo in catalogo:
            if insumo[clave] == item:
                mostrar_insumo(insumo)
        print("╚════╩═══════════════════════════════════╩═════════════════════════╩══════════╩══════════════════════════════════════════════════════════════════════════════════════════╝\n")

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

def filtar_por_marca(catalogo: list) -> list:
    """Pide por cosola que se ingrese una marca y luego filtra una lista con los productos de esa marca

    Args:
        catalogo (list): catalogo en el cual se van a buscar los productos de esa marca

    Returns:
        list: devuelve una lista con todos los productos de la marca ingresada
    """    
    mostrar_catalogo(catalogo)
    marca = input("\nIngrese la marca de la cual desea ver que productos hay disponibles: ")
    insumos_marca_elegida = list(filter(lambda insumo: insumo["MARCA"] == marca, catalogo))
    return insumos_marca_elegida

def realizar_compras(catalogo: list) -> float:
    """Permite al usuario realizar compras hasta que lo desee, carga en un archivo txt la factura

    Args:
        catalogo (list): catalogo del cual se van a realizar las compras

    Returns:
        float: precio final total de la compra
    """    
    with open("Labo 1 PP\\factura.txt", "w") as file:
        file.write("| Cantidad |                    Descripcion                   |     Precio     |          Subtotal         |\n")
    
    subtotales = []
    while True:
        insumos_marca_elegida = filtar_por_marca(catalogo)
        mostrar_catalogo(insumos_marca_elegida)
        
        #Validaciones
        while True:
            try:
                id = int(input("Ingrese el id del producto que desea: "))
            except ValueError:
                print("Solo se pueden ingresar id entre 1-50")
                continue
            break
        
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad que desea: "))
            except ValueError:
                print("Solo se pueden ingresar numeros")
                continue
            break
        
        for insumo in catalogo:
            if id == int(insumo["ID"]):
                producto = {}
                producto["INSUMO"] = insumo["NOMBRE"]
                producto["MARCA"] = insumo["MARCA"]
                producto["PRECIO"] = re.sub("\\$", "", insumo["PRECIO"])
                producto["CANTIDAD"] = cantidad
                subtotales.append(producto['CANTIDAD'] * float(producto['PRECIO']))
                
                with open("Labo 1 PP\\factura.txt", "a") as file:
                    file.write("|----------|--------------------------------------------------|----------------|---------------------------|\n")
                    file.write(f"|{str(producto['CANTIDAD']):^10s}| {producto['INSUMO']:29s}{producto['MARCA']:20s}|{producto['PRECIO']:^16s}|{str(subtotales[-1]):^27s}|\n")
        
        seguir = input("Desea seguir comprando? s/n: ")
        if seguir == "n":
            break
    
    # Para validar que subtotales no este vacia
    try:
        total = reduce(lambda ant, act: ant + act, subtotales)
    except UnboundLocalError:
        total = 0
    
    with open("Labo 1 PP\\factura.txt", "a") as file:
        file.write(f"\nEl total de la compra es de: ${total}")
    return total

def catalogo_solo_alimentos(catalogo: list) -> list:
    """Filtra el catalogo original y devuelve uno solo de los productos que contengan la palabra 'Alimento' en el nombre

    Args:
        catalogo (list): catalogo original

    Returns:
        list: catalogo solo de alimentos
    """    
    patron = re.compile("Alimento")
    return list(filter(lambda insumo: patron.search(insumo["NOMBRE"]), catalogo))

def cargar_a_json(lista_dicts: list, archivo: str) -> None:
    """Crea y escribe un archivo json con una lista de diccionarios que le pasamos

    Args:
        lista_dicts (list): lista de diccionarios que queremos cargar como archivo json
        archivo (str): nombre que recibira el archivo json
    """    
    with open(archivo, "w") as file:
        json.dump(lista_dicts, file, indent=2)

def descargar_de_json(archivo: str) -> list:
    """Lee un archivo json y lo pasa a una lista de diccionarios

    Args:
        archivo (str): nombre del archivo que queremos leer

    Returns:
        list: lista de diccionarios cargada con el archivo
    """    
    with open(archivo, "r") as file:
        return json.load(file)

def aumento_precios(catalogo: list) -> list:
    """Recibe por parametros el catalogo original y mediante la funcion map aumenta un 8,4% los precios y devuelve una lista con los precios nuevos

    Args:
        catalogo (list): lista de diccionarios con alguno de sus campos "PRECIO"

    Returns:
        (list): catalogo con los nuevos precios aumentados
    """    
    return list(map(lambda insumo: {**insumo, "PRECIO": float(re.sub("\\$", "", insumo["PRECIO"])) * 1.084}, catalogo))
    # list(map(lambda insumo: float(re.sub("\\$", "", insumo["PRECIO"])) * 1.084, catalogo))   <- esto devolvia una lista con los precios aumentados

def cargar_a_csv(catalogo: list, archivo: str) -> None:
    """Carga el catalogo a un archivo csv

    Args:
        catalogo (list): lista de diccionarios 
        archivo (str): nombre del archivo csv donde lo vamos a cargar
    """    
    with open(archivo, "w", encoding= "UTF-8") as file:
        file.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")
        for insumo in catalogo:
            file.write(f"{insumo['ID']},{insumo['NOMBRE']},{insumo['MARCA']},{insumo['PRECIO']},{insumo['CARACTERISTICAS']}\n")

def descargar_de_txt(archivo: str) -> list:
    """Lee un archivo txt y guarda los datos en una lista

    Args:
        archivo (str): nombre del archivo que queremos leer

    Returns:
        list: lista con los datos del archivo txt
    """    
    with open(archivo, "r") as file:
        lista_marcas = []
        for linea in file:
            linea = linea.strip("\n")
            lista_marcas.append(linea)
    return lista_marcas

def mostrar_lista(lista: list, titulo: str) -> None:
    """Muestra una lista con un titulo a eleccion

    Args:
        lista (list): lista que vamos a mostrar
        titulo (str): encabezado de la lista
    """    
    print("|========================================|")
    print(f"|{titulo:^40s}|")
    print("|========================================|")
    for elemento in lista:
        print(f"|{elemento:^40s}|")
        print("|----------------------------------------|")

def agregar_producto(catalogo: list) -> None:
    """Se le va pidiendo al usuario que complete los datos de un producto y se lo agrega al catalogo

    Args:
        catalogo (list): catalogo original donde se va a agregar un insumo
    """    
    producto = {}
    producto['ID'] = str(int(catalogo[-1]['ID']) + 1)
    producto['NOMBRE'] = input("Ingrese un nombre para el producto: ")
    
    lista_marcas = descargar_de_txt("Labo 1 PP\\marcas.txt")
    mostrar_lista(lista_marcas,"MARCAS DISPONIBLES")
    while True:
        marca = input("A partir de estas, cual quiere que sea la marca para su producto: ")
        if marca in lista_marcas:
            producto['MARCA'] = marca
            break
        else:
            print("La marca no es valida, debe estar en la lista.")
    
    while True: 
        try:
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("Debe ingresar un precio, tiene que ser numerico.")
            continue
        else:
            break
        
    producto['PRECIO'] = f"${precio}"
    
    
    contador = 0
    flag_caracteristica = True
    while True:
        caracteristica = input("Ingrese caracteristica: ")
        if caracteristica == "" and flag_caracteristica:
            print("Debe ingresar una caracteristica obligatoriamente.")
            continue
        
        if contador == 0:
            producto['CARACTERISTICAS'] = caracteristica
            flag_caracteristica = False
        elif contador == 1:
            producto['CARACTERISTICAS'] = producto["CARACTERISTICAS"]+"~"+caracteristica
        elif contador == 2:
            producto['CARACTERISTICAS'] = producto["CARACTERISTICAS"]+"~"+caracteristica
            
        contador += 1
        seguir = input("Desea ingresar otra caracteristica?: ")
        if seguir == "n" or contador == 3:
            break
        
    catalogo.append(producto)

def guardar_en_archivo(catalogo: list) -> None:
    """Guarda a eleccion del usuario, en un archivo json o un archivo csv el catalogo que le pasamos por parametro, con un nombre elegido por el usuario

    Args:
        catalogo (list): lista de diccionarios 
    """    
    while True:
        extension = input("En que tipo de archivo desea guardar el catalogo? (csv | json): ")
        if extension == 'json' or extension == 'csv':
            break
    
    nombre_archivo = input("Ingrese el nombre del archivo (sin la extension): ")
    
    if extension == "json":
        with open(nombre_archivo+"."+extension, "w") as file:
            json.dump(catalogo, file, indent=2)
    else:
        with open(nombre_archivo+"."+extension, "w", encoding= "UTF-8") as file:
            file.write("ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS\n")
            for insumo in catalogo:
                file.write(f"{insumo['ID']},{insumo['NOMBRE']},{insumo['MARCA']},{insumo['PRECIO']},{insumo['CARACTERISTICAS']}\n")