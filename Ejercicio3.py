
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

class ProductoAgotadoException(Exception):
    pass

class Mercado:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_y_vender_producto(self, nombre_producto, cantidad_vendida):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad < cantidad_vendida:
                    raise ProductoAgotadoException(f"No hay suficiente stock de {nombre_producto}.")
                producto.cantidad -= cantidad_vendida
                if producto.cantidad == 0:
                    self.productos.remove(producto)
                return producto
        raise ProductoAgotadoException(f"El producto {nombre_producto} no existe.")

    def __str__(self):
        return "\n".join(str(producto) for producto in self.productos)

try:
    mercado = Mercado()
    manzana = Producto("Manzana", 0.5, 10)
    banana = Producto("Banana", 0.3, 5)

    mercado.agregar_producto(manzana)
    mercado.agregar_producto(banana)

    print("Antes de la venta:")
    print(mercado)

    vendido = mercado.buscar_y_vender_producto("Manzana", 3)
    print(f"Producto vendido: {vendido}")

    print("Después de la venta:")
    print(mercado)

    mercado.buscar_y_vender_producto("Banana", 6)

except ProductoAgotadoException as e:
    print(e)
