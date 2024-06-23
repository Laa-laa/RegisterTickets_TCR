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

    # def test_calculate_total_price(self):
    #     price = 5.0
    #     quantity = 3
    #     expected_total = 15.0
    #     order = TicketsService(price, quantity)
    #     actual_total = order.calculate_total_price()
    #     self.assertEqual(expected_total, actual_total)


if __name__ == '__main__':
    unittest.main()
