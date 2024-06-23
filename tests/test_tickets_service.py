import unittest
from main.tickets_service import TicketsService

class TestTicketsService(unittest.TestCase):

    def test_start_application(self):
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        TicketsService.start_application()

        sys.stdout = sys.__stdout__
        self.assertIn("Hello, World!", captured_output.getvalue().strip())

    # def test_calcul_prix_total(self):
    #     prix = 5.0
    #     somme = 3
    #     total_attendu = 15.0
    #     order = TicketsService(prix, somme)
    #     total_actuel = order.calcul_prix_total()
    #     self.assertEqual(total_attendu, total_actuel)

if __name__ == '__main__':
    unittest.main()