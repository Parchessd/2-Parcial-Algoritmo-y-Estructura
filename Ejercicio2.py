from datetime import datetime, timedelta

class Producto:
    def __init__(self, nombre, fecha_expiracion, cantidad):
        self.nombre = nombre
        self.fecha_expiracion = fecha_expiracion
        self.cantidad = cantidad

class Nodo:
    def __init__(self, producto=None, siguiente=None):
        self.producto = producto
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, producto):
        nuevo_nodo = Nodo(producto, self.cabeza)
        self.cabeza = nuevo_nodo

    def remover_producto(self, nombre_producto):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.producto.nombre == nombre_producto:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def productos_que_expiran_en_24_horas(self):
        productos_expiran = []
        ahora = datetime.now()
        limite = ahora + timedelta(days=1)
        actual = self.cabeza
        while actual is not None:
            if actual.producto.fecha_expiracion <= limite:
                productos_expiran.append(actual.producto)
            actual = actual.siguiente
        return productos_expiran

    def remover_productos_expirados(self):
        ahora = datetime.now()
        anterior = None
        actual = self.cabeza
        while actual is not None:
            if actual.producto.fecha_expiracion <= ahora:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
            else:
                anterior = actual
            actual = actual.siguiente

class Mercado:
    def __init__(self):
        self.secciones = {}

    def agregar_seccion(self, nombre_seccion):
        if nombre_seccion not in self.secciones:
            self.secciones[nombre_seccion] = ListaEnlazada()

    def agregar_producto(self, nombre_seccion, producto):
        if nombre_seccion in self.secciones:
            self.secciones[nombre_seccion].agregar_producto(producto)
        else:
            nueva_lista = ListaEnlazada()
            nueva_lista.agregar_producto(producto)
            self.secciones[nombre_seccion] = nueva_lista

    def remover_producto(self, nombre_seccion, nombre_producto):
        if nombre_seccion in self.secciones:
            return self.secciones[nombre_seccion].remover_producto(nombre_producto)
        return False

    def productos_que_expiran_en_24_horas(self):
        productos_expiran = []
        for seccion in self.secciones.values():
            productos_expiran.extend(seccion.productos_que_expiran_en_24_horas())
        return productos_expiran

    def remover_productos_expirados(self):
        for seccion in self.secciones.values():
            seccion.remover_productos_expirados()
            
mercado = Mercado()
mercado.agregar_seccion("Lácteos")
mercado.agregar_seccion("Carnes")

producto1 = Producto("Leche", datetime(2023, 6, 26), 10)
producto2 = Producto("Yogurt", datetime(2023, 6, 25), 5)
producto3 = Producto("Carne", datetime(2023, 6, 27), 20)

mercado.agregar_producto("Lácteos", producto1)
mercado.agregar_producto("Lácteos", producto2)
mercado.agregar_producto("Carnes", producto3)

print("Productos que expiran en 24 horas:")
for producto in mercado.productos_que_expiran_en_24_horas():
    print(f"{producto.nombre} expira el {producto.fecha_expiracion}")

    mercado.remover_productos_expirados()
