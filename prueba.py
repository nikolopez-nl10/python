
#cracion de 

productos = {
    
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']

}
stock = {
'8475HD': [387990,10], 
'2175HD': [327990,4], 
'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], 
'123FHD': [290890,32], 
'342FHD': [444990,7],
'GF75HD': [749990,2],
'UWU131HD': [349990,1], 
'FS1230HD':[249990,0], 
}

def stock_marca(marca):
    marca_disponible = set([j[0].lower()for j in productos.values()])
    if marca.lower()not in marca_disponible:
        print("marca no existe, las marcas que estan disponibles son :",','.join(marca_disponible))
        return
        total = 0



def busqueda_por_precio(p_min, p_max):
    resulatado = []
    for codigo in stock :
        precio, unidad = stock[codigo]
    if p_min <= precio <= p_max 
    





def actualizar_precio(codigo, p_nuevo):
    if codigo in stock:
        stock[codigo][0]= p_nuevo
        return True
    else :
        return False
    



while true:
    print("<<<<<<<<<MENU>>>>>>>>")
    print("stock por marca")
    print("busqueda por precio")
    print("actualizar precio")
    print("finalizar ")


opcion = int(input("ingrese la opcion desada"))
try:
     
    if opcion == 4:
        print("finalizando programa ")
        break
    elif opcion== "1":
        marca = int(input("ingrese la marca a buscar "))
        if marca in productos:
            print(f" la marca {marca} si est disponible en inventario ")
        else:
            print("marca no disponible ")

    elif opcion ==2:
        p_min = int(input(" ingrese el valor minimo"))
        p_max = int(input("ingrese el valor maximo"))
    
    elif opcion ==3:

        