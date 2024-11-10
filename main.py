class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, colorNuevo):
        coloresPermitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if colorNuevo in coloresPermitidos:
            self.color = colorNuevo

class Auto:
    cantidad_creados = ""
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo          
        self.precio = precio         
        self.asientos = asientos    
        self.marca = marca        
        self.motor = motor            
        self.registro = registro   

    def cantidadAsientos(self):
        cant_asientos = 0

        for i in self.asientos:
            if not (i == None):
                cant_asientos += 1
        return cant_asientos
        
    def verificarIntegridad(self):
        if not self.registro == self.motor.registro:
            return "return Las piezas no son originales"
        
        for asiento in self.asientos:
            if not (asiento == None):
                if not self.registro == asiento.registro:
                    return "Las piezas no son originales"
        return "Auto original"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registroNuevo):
        self.registro = registroNuevo
    
    def asignarTipo(self, tipoNuevo):
        if "electrico" == tipoNuevo or "gasolina" == tipoNuevo:
            self.tipo = tipoNuevo