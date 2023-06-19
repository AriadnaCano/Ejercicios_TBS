class Tienda:
    '''
    Clase tienda con parámetros comunes que indican el tipo de tienda y si está abierta (True/False)
    '''
    Tipo = "Electrodomésticos"
    Abierta = True

    def __init__(self, nombre_tienda:str, direccion_tienda:str, empleados:int, ventas_3:list):
        self.nombre = nombre_tienda
        self.direccion = direccion_tienda
        self.empleados = empleados
        self.ventas_3 = ventas_3
    '''
    atributos propios de cada tienda que aporta el usuario: nombre de la tienda, dirección, número de empleados y las ventas obtenidas
    en los últimos 3 meses
    '''
    
    def ventas_año(self):
        return sum(self.ventas_3)
    '''
    Método para devolver el total de las ventas (float)
    '''

    def venta_empleado(self):
            return sum(self.ventas_3) / self.empleados
    '''
    Método para devolver el total de ventas de cada empleado (float)
    '''
    
    def nombre_direcc (self):
        return self.nombre + " " + self.direccion
    '''
    Método para devolver el nombre de la tienda (str) junto con su dirección (str)
    '''
    def ult_mes (self):
        return self.ventas_3[-1]
    '''
    Método utilizado para mostrar las ventas del último mes (float)
    '''

    def marketing(self, param_entrada):
        if param_entrada < 1000:
            return sum(self.ventas_3) * 1.2
        elif param_entrada >= 1000:
            return sum(self.ventas_3) * 1.5
    '''
    Método para calcular los beneficios en base a capital invertido (float)
    '''

class Perro:
    '''
Clase perro, con parámetros comunes que indican el número (int) de patas, orejas, ojos y la velocidad.
'''
    Patas = 4
    Orejas = 2
    Ojos = 2
    Velocidad = 0
    def __init__(self, raza:str, color_pelo = "Marron", duenio=None):
        self.raza = raza
        self.pelo = color_pelo
        self.dueño = duenio
        
    '''
Argumentos variables dados por el usuario, indican la raza del perro (str), el color de pelo (str, por defecto Marrón) 
y el dueño (None por defecto)
'''
    
    def andar(self, aumento_vel):

        self.Velocidad = self.Velocidad + aumento_vel
        return self.Velocidad
    '''
Método que devuelve el aumento de velocidad del perro (int), teniendo por defecto un estado de velocidad 0. La velocidad la indica el usuario
'''
    
    def ladrar(self, ladrido):
        return "GUAU!" + " " + str(ladrido)
    
    def parada(self):
        self.Velocidad = 0
