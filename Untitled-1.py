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
    
    def ImprimirLista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.data, end=" ")
            actual = actual.siguiente
    
   

# Crear una nueva lista enlazada
miLista = ListaSE()

# Agregar elementos al inicio de la lista
miLista.AgregarInicio(10)
miLista.AgregarInicio(20)

# Agregar elementos al final de la lista
miLista.AgregarFinal(40)
miLista.AgregarFinal(30)

# Imprimir la lista
miLista.ImprimirLista()