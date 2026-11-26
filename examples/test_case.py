"""Exact checks of the fictional case, using cents and rational numbers."""
from fractions import Fraction as F
import unittest


def baskets(required):
    return sorted(
        (150*s + 200*l, 6*s + 10*l, s, l)
        for s in range(required+1) for l in range(required+1)
        if 6*s + 10*l >= required
    )


class PrealgebraChecks(unittest.TestCase):
    def test_ledger_and_inverse(self):
        self.assertEqual(-750+4800-1200, 2850)
        self.assertEqual(2850+1200-4800, -750)

    def test_order_and_signs(self):
        self.assertEqual((48-2*12, (48-2)*12), (24, 552))
        self.assertEqual((-400+1500-600+600, 20-(7-3), (20-7)-3), (1100, 16, 10))

    def test_equivalent_forms(self):
        self.assertEqual(F(3, 4), F("0.75"))
        self.assertEqual(F(7, 20)*100, 35)

    def test_recipe(self):
        self.assertEqual(F(3, 4)/3*5, F(5, 4))
        self.assertEqual(F(3, 4)/3*7, F(7, 4))

    def test_unit_price(self):
        self.assertEqual((F(150, 6), F(200, 10)), (25, 20))

    def test_unique_basket(self):
        rows = baskets(12)
        self.assertEqual(rows[0], (300, 12, 2, 0))
        self.assertGreater(rows[1][0], rows[0][0])
        self.assertEqual(baskets(16)[0], (350, 16, 1, 1))

    def test_reserve(self):
        self.assertEqual(2850-300-750, 1800)
        self.assertLess(2850-300-850, 1800)
        self.assertLess(2850-350-701, 1800)

    def test_chart(self):
        small, large = 2850-300, 2850-400
        self.assertEqual((small, large, small-large), (2550, 2450, 100))
        self.assertEqual((small-2400, large-2400), (150, 50))
        self.assertEqual(F(small-2400, large-2400), 3)

    def test_transfer(self):
        self.assertEqual(F(2, 3)/4*6, 1)
        self.assertEqual(-300+2700-900-210-290, 1000)
        self.assertGreater(2*120, 210)


if __name__ == "__main__":
    unittest.main()
