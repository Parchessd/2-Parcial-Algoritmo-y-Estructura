class Cliente:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

        lass ColaPrioridad:
    def __init__(self):
        self.cola = []

    def encolar(self, cliente):
        self.cola.append(cliente)
        self.cola.sort(key=lambda x: x.prioridad, reverse=True)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            return None

    def esta_vacia(self):
        return len(self.cola) == 0
    
    class Mercado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = ColaPrioridad()

    def agregar_cliente(self, nombre_cliente, prioridad):
        cliente = Cliente(nombre_cliente, prioridad)
        self.clientes.encolar(cliente)

    def atender_cliente(self):
        if self.clientes.esta_vacia():
            print("No hay clientes para atender")
        else:
            cliente = self.clientes.desencolar()
            print(f"Atendiendo a {cliente.nombre}")

    def mostrar_cola(self):
        if self.clientes.esta_vacia():
            print("La cola está vacía")
        else:
            print("Cola de clientes:")
            for cliente in self.clientes.cola:
                print(f"{cliente.nombre} con prioridad {cliente.prioridad}")


mercado = Mercado("Supermercado")
mercado.agregar_cliente("Juan", 1)
mercado.agregar_cliente("Ana", 3)
mercado.agregar_cliente("Luis", 2)

mercado.mostrar_cola()  

mercado.atender_cliente()   
mercado.mostrar_cola()   

mercado.atender_cliente()   
mercado.atender_cliente()   
mercado.atender_cliente()   