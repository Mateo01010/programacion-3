class Producto:
    def __init__(self, nombre, tipo, precio, stock):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.__stock = 0
        self.set_stock(stock)
    
    def get_stock(self):
        return self.__stock
 
    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Stock inválido")
 
    def mostrar_datos(self):
        print("Nombre:",self.nombre,"\nTipo:",self.tipo,"\nPrecio:",self.precio,"\nStock:",self.__stock,"\n ")
  
    def vender(self, cantidad):
        if cantidad <= 0:
            print("Cantidad invalida")
        elif cantidad <= self.__stock:
            self.__stock -= cantidad
            print("Venta realizada")
        else:
            print("Stock insuficiente")
        print(" ")

Producto1 = Producto("fideos","comida",10000,10)
Producto1.vender(15)
Producto1.set_stock(-500)

#lo que evitamos es que haya stock negativo. El encapsulamiento controla que nadie modifique el atributo directamente desde afuera y la validacion en una regla logica que evalua si el dato es correcto

class Alimento(Producto):
    def __init__(self, nombre, precio, stock, vencimiento):
       super().__init__(nombre, "Alimento", precio, stock)
       self.vencimiento = vencimiento
    
    def mostrar_vencimiento(self):
        print("Vto:",self.vencimiento)

class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre,"Electronico",precio,stock)
        self.garantia_meses = garantia
    
    def mostrar_garantia(self):
        print("Garantia:", self.garantia_meses ,"meses")

Alimento1 = Alimento("papa", 1000, 5, 20)
Electronico1 = Electronico("monitor", 500, 10, 40)

#Alimento1.vender(3)
#Alimento1.mostrar_vencimiento()
#Electronico1.mostrar_datos()
#Electronico1.mostrar_garantia()

Productos = [Alimento1,Electronico1]
for producto in Productos:
    producto.mostrar_datos()

#con la herencia evite repetir mostrar_datos(). El atributo propio es vencimiento en alimento y garantia en electronico
#es posible porque lo hereda de la clase padre
#da un attributeError porque nunca se van a inicializar los atributos, entonces no se pueden usar
#cada objeto tiene el suyo propio
#get_stock usa return porque lo que hace es devolver un valor numerico y mostrar_datos() muestra los datos del producto por eso usa print
#la diferencia es que modificar el stock con un setter sobreescribe el stock actual por el nuevo y vender() hace una operación que resta al stock actual el numero que elegis

