import unittest
from person import Persona
  # Importamos la clase desde el otro archivo llamado person.py

class TestPersona(unittest.TestCase):

    def test_saludar(self):
        persona = Persona("Josue Torres", 22)
        self.assertEqual(persona.saludar(), "Hola, mi nombre es Joss")

    def test_es_mayor_de_edad(self):
        persona1 = Persona("David Torres", 22)
        persona2 = Persona("Juan Perez", 15)

        self.assertTrue(persona1.es_mayor_de_edad())   # Debe ser True
        self.assertFalse(persona2.es_mayor_de_edad())  # Debe ser False

if __name__ == "__main__":
    unittest.main()
