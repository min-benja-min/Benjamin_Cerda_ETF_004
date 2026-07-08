juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],

}

inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}


def stock_plataforma(plataforma):
    
    total = 0
    for id, datos in juegos.items():
        if plataforma.lower() == juegos[id][1].lower():
            total += inventario[id][-1]
    print(f"El total de juegos para la plataforma {plataforma} es de {total}.")
   

def busqueda_precio(p_min, p_max):

    lista = []
    for id, datos in inventario.items():
        if (p_min <= inventario[id][0] <= p_max) and inventario[id][-1] != 0:
            lista.append(f"{juegos[id][0]} - {id}")
    if len(lista) == 0:
        print("No hay juegos en ese rango de precios")
    print(lista) #me da error el .sort() para ordenar alfabeticamente:(



def actualizar_precio(codigo, nuevo_precio):
    while True:
        for id, datos in inventario.items():
            if codigo in inventario:
                inventario[codigo][0] = nuevo_precio
                print("Precio actualizado")
                return True
            else:
                print("El código no existe")
                return False

        nuevamente = input("Desea actualizar otro precio (s/n)?: ")
        if nuevamente.lower == "s":
            continue
        if nuevamente.lower == "n":
            break
            
# Validaciones item 4

def validarCodigo(cod):
    while cod == " " or cod == "" or (cod in inventario) or (cod in juegos):
        print("Intente nuevamente")
        cod = input("Ingrese el codigo: ")
        return False
    return True
    
        
def validarTitulo(tit):
    while tit == "" or tit == " ":
        print("Intente nuevamente")
        tit = input("Ingrese el titulo: ")
        return False
    return True

def validarPlataforma(plat):
    while plat == "" or plat == " ":
        print("Intente nuevamente")
        plat = input("Ingrese la plataforma: ")
        return False
    return True

def validarGenero(gen):
    while gen == "" or gen == " ":
        print("Intente nuevamente")
        gen = input("Ingrese el genero: ")
        return False
    return True

def validarClasificacion(clas):
    while clas.upper != "E" and clas.upper != "T" and clas.upper != "M":
        print("Intente nuevamente")
        clas = input("Ingrese el clasificacion: ")
        
    return True
        
def validarMultiplayer(mult):
    while mult.lower != "s" and mult.lower != "n":
        print("Intente nuevamente")
        mult = input("Es multipayer? (s/n): ")

    if mult.lower == "s":
        return True
    elif mult.lower == "n":
        return False
    
def validarEditor(edit):
    while edit == "" or edit == " ":
        print("Intente nuevamente")
        edit = input("Ingrese el editor: ")
        return False
    return True

def validarPrecio(prec):
    while prec <= 0:
        print("Debe ser mayor que cero")
        prec = int(input("Ingrese el precio: "))
        return False
    return True

def validarStock(stock): 
    while stock <= 0:
        print("Debe ser mayor que cero")
        stock = int(input("Ingrese el stock: "))
        return False
    return True
        

def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer,
editor, precio, stock):
    juegos[codigo] = [titulo, plataforma, genero, clasificacion, multiplayer, editor]
    inventario[codigo] = [precio,stock]
    print("Juego agregado")
    return True



def eliminar_juego(codigo):

    for cod, datos in juegos.items():
        if codigo in juegos:
            del juegos[codigo]
            del inventario[codigo]
            print("Juego eliminado")
            return True
        else:
            print("EL codigo no existe")
            return False



while True:
    try:
        print('''

========== MENÚ PRINCIPAL ==========
1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir
=====================================  
        ''')
        opc = int(input("Ingrese una opcion: "))
        match opc:
            case 1:
                plataforma = input("Ingrese el nombre de la plataforma: ")
                stock_plataforma(plataforma)
            case 2:

                try: 
                    precioMin = int(input("Ingrese el precio minimo: "))
                    precioMax = int(input("Ingrese el precio maximo: "))

                    #Comprobación valores p_min y p_max
                    while precioMin > precioMax:
                        print("El precio máximo debe ser mayor al precio minimo!")
                        precioMin = int(input("Ingrese el precio minimo: "))
                        precioMax = int(input("Ingrese el precio maximo: "))
                    while precioMin < 0 and precioMax < 0:
                        print("Los precios deben ser mayores o iguales a cero")
                        precioMin = int(input("Ingrese el precio minimo: "))
                        precioMax = int(input("Ingrese el precio maximo: "))
                except Exception as e:
                    print("Debe ingresar valores enteros", e)

                    
                busqueda_precio(precioMin, precioMax)
                
            case 3:
                codigo = input("Ingrese el codigo del juego: ")
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                while nuevo_precio < 0:
                    print("El precio debe ser mayor o igual a cero!")
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))

                actualizar_precio(codigo, nuevo_precio)
            case 4:
                codigo = input("Ingrese el codigo: ")
                if validarCodigo(codigo) == False:
                    print("Error al ingresar")
                    
                

                titulo = input("Ingrese el titulo: ")
                if validarTitulo(titulo) == False:
                    print("Error al ingresar")
                    

                plataforma = input("Ingrese el plataforma: ")
                if validarPlataforma(plataforma) == False:
                    print("Error al ingresar")
                    

                genero = input("Ingrese el genero: ")
                if validarGenero(genero)== False:
                    print("Error al ingresar")
                    

                clasificacion = input("Ingrese la clasificacion (E/T/M): ")
                if validarClasificacion(clasificacion) == False:
                    print("Error al ingresar")
                    

                multiplayer = input("Es multipayer? (s/n): ")
                if validarMultiplayer(multiplayer) == False:
                    print("Error al ingresar")
                     

                editor = input("Ingrese el editor: ")
                if validarEditor(editor) == False:
                    print("Error al ingresar")
                    

                precio = int(input("Ingrese el precio"))
                if validarPrecio(precio) == False:
                    print("Error al ingresar")
                    

                stock = int(input("Ingrese el stock"))
                if validarStock(stock) == False:
                    print("Error al ingresar")
                    

                if (validarCodigo and validarTitulo and validarPlataforma and 
                validarGenero and validarClasificacion and validarMultiplayer
                and validarEditor and validarPrecio and validarStock) == True:
                    
                    agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer,
editor, precio, stock)

            case 5:
                codigo = input("Ingrese el codigo del juego a eliminar: ")
                eliminar_juego(codigo)
            case 6:
                print("Programa finalizado")
                break
            case _:
                print("")


    except Exception as e:
        print("Error: ", e)

