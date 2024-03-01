class Nodo:
    def __init__(self,valor):
        self.data = valor
        self.siguiente = None

class ListaSE:
    def __init__(self):
        self.cabeza = None
    
    def AgregarInicio(self,valor):
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return 
        
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            
    def AgregarFinal(self,valor):
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None:
            self.cabeza= nuevo_nodo
        
        else:
            current = self.cabeza
            while current.siguiente is not None:
                current = current.siguiente
            current.siguiente = nuevo_nodo  # Mover esta línea fuera del ciclo while
    
    def EliminarInicio(self):
        if self.cabeza is None:
            print("Lista vacía. Ningún elemento puede ser eliminado")
        
        else:
            node=self.cabeza
            self.cabeza= self.cabeza.siguiente
            del node
    
    def EliminarFinal(self):
        if self.cabeza is None:
            print("Lista vacía. Ningún elemento puede ser eliminado")
        
        else:
            current = self.cabeza
            previos= None
            while current.siguiente is not None:
                previous= current
                current=current.siguiente
            previous.siguiente = None
            del current
    
    def ImprimirLista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.data, end=" ")
            actual = actual.siguiente

   def buscarElemento(self, nombreProducto):
        actual = self.cabeza
        while actual:
            if actual.data == nombreProducto:
                return True
            actual = actual.siguiente
        return False

    def contarElemento(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def ListaVacia(self):
        return self.cabeza is None

# Crear una nueva lista enlazada
miLista = ListaSE()

# Agregar elementos al inicio de la lista
miLista.AgregarInicio(10)
miLista.AgregarInicio(20)

# Agregar elementos al final de la lista
miLista.AgregarFinal(40)
miLista.AgregarFinal(30)

# Imprimir la lista


miLista.EliminarInicio()
miLista.EliminarFinal()

miLista.ImprimirLista()
