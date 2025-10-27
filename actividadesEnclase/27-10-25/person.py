# class.py

class Persona:
    def __init__(self, nombre, edad):
        # Atributos de la clase
        self.nombre = nombre
        self.edad = edad

    # Método que devuelve un saludo
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"

    # Método que verifica si es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18
