import unittest
from A_calc import suma,resta,multiplicar,dividir
class TestCalc(unittest.TestCase):
    # Cada método dentro de esta clase que empiece con test_ será reconocido 
    # automáticamente como una prueba.
    def setUp(self):
        print("Preparando entorno...")

    def tearDown(self):
        print("Limpiando entorno...")
    # setUp() → se ejecuta antes de cada test. 
    # Sirve para preparar datos o inicializar objetos.
    # tearDown() → se ejecuta después de cada test. Sirve para limpiar recursos.
    def test_suma_basica(self):
        for num1 in range(10):
            for num2 in range(10):
                self.assertEqual(suma(num1, num2), num1+num2)
    def test_suma_negativos(self):
        self.assertEqual(suma(-5, -3), -8)
        self.assertEqual(suma(-5, 3), -2)

    def test_suma_grandes(self):
        self.assertEqual(suma(1000000, 2000000), 3000000)

    def test_suma_con_cero(self):
        self.assertEqual(suma(0, 5), 5)
        self.assertEqual(suma(5, 0), 5)
              
    def test_dividir(self):
        # Forma 1
        self.assertRaises(ZeroDivisionError, dividir, 50, 0)

        # Forma 2
        with self.assertRaises(ZeroDivisionError):
            dividir(50, 0)
if __name__ == "__main__":
    unittest.main()
    
# assertEqual(a, b)	Verifica que a == b
# assertNotEqual(a, b)	Verifica que a != b
# assertTrue(condición)	Verifica que la condición es verdadera
# assertFalse(condición)	Verifica que la condición es falsa
# assertIs(a, b)	Verifica que a y b son el mismo objeto
# assertIsNone(x)	Verifica que x es None
# assertIn(a, b)	Verifica que a está dentro de b
# assertRaises(Error, función, args...)	Verifica que se lanza una excepción