class Nodo:
    def __init__(self,valor):
        self.data = valor
        self.siguiente = None
# Fin de la clase Nodo
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
            
# Fin de la clase Lista


ListaSimple = ListaSE()
ListaSimple.AgregarInicio(5)
print(ListaSimple.cabeza.data)
ListaSimple.AgregarInicio(8)
print(ListaSimple.cabeza.data)
